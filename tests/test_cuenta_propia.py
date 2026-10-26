import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "cuenta_propia.py"


def run(*args):
    return subprocess.run(["python3", str(CLI), *args], text=True, capture_output=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class CuentaPropiaTests(unittest.TestCase):
    def make_green_case(self, root):
        case = root / "private-case"
        self.assertEqual(run("init", str(case), "--route", "modification-191-3").returncode, 0)
        document = case / "documents" / "passport.pdf"
        document.write_bytes(b"%PDF-1.4\nsynthetic\n%%EOF\n")
        data = json.loads((case / "case.json").read_text())
        for key, review in data["reviews"].items():
            review.update(status="complete", reviewed_on="2026-10-26", reviewer="reviewer", notes="Synthetic review evidence for this test.")
            if key in {"sources", "route"}:
                review["evidence"] = [{"url": "https://example.test/official", "section": "Synthetic section", "checked_on": "2026-10-26", "notes": "Synthetic official-source record."}]
        data["applicant"] = {"name": "Example", "nationality": "Example", "province": "Example"}
        data["portal"]["confirmed_on"] = "2026-10-26"
        data["documents"] = [{"id": "passport", "path": "documents/passport.pdf", "sha256": digest(document), "content_review": {"status": "complete", "reviewed_on": "2026-10-26", "reviewer": "reviewer", "notes": "Synthetic content review."}, "expires_on": "2099-01-01"}]
        data["requirements"] = [{"id": "identity", "title": "Identity", "basis": "official basis", "source_url": "https://example.test", "status": "applicable", "documents": ["passport"]}]
        (case / "case.json").write_text(json.dumps(data))
        return case, document

    def test_green_audit_and_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            case, document = self.make_green_case(Path(tmp))
            self.assertEqual(run("audit", str(case), "--json").returncode, 0)
            self.assertEqual(run("bundle", str(case)).returncode, 0)
            copied = next((case / "output").glob("01_passport_*"))
            self.assertEqual(copied.read_bytes(), document.read_bytes())
            self.assertEqual(json.loads((case / "output" / "manifest.json").read_text())["submission"], "not_submitted")

    def test_stale_hash_blocks_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            case, document = self.make_green_case(Path(tmp))
            document.write_bytes(b"%PDF-1.4\nchanged\n%%EOF\n")
            result = run("audit", str(case))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("bytes changed", result.stdout)
            self.assertNotEqual(run("bundle", str(case)).returncode, 0)
            self.assertFalse((case / "output").exists())

    def test_expiry_and_escape_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            case, document = self.make_green_case(root)
            data = json.loads((case / "case.json").read_text())
            data["documents"][0]["expires_on"] = "2020-01-01"
            (case / "case.json").write_text(json.dumps(data))
            self.assertIn("expired", run("audit", str(case)).stdout)
            data["documents"][0]["expires_on"] = ""
            data["documents"][0]["path"] = "../escape.pdf"
            (case / "case.json").write_text(json.dumps(data))
            self.assertIn("below documents/", run("audit", str(case)).stdout)

    def test_future_expiry_is_valid_and_symlinked_documents_are_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            case, document = self.make_green_case(Path(tmp))
            self.assertEqual(run("audit", str(case)).returncode, 0)
            outside = Path(tmp) / "outside"
            outside.mkdir()
            (outside / "passport.pdf").write_bytes(document.read_bytes())
            (case / "documents").rename(case / "real-documents")
            (case / "documents").symlink_to(case / "real-documents", target_is_directory=True)
            result = run("audit", str(case))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("symlinked documents", result.stdout)

    def test_repo_local_case_is_refused(self):
        result = run("init", str(ROOT / "do-not-create"), "--route", "initial-ex07")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("outside this public repository", result.stderr)

    def test_invalid_manifest_fails_without_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            case = Path(tmp) / "private-case"
            case.mkdir()
            (case / "case.json").write_text("{ not json")
            result = run("audit", str(case))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("invalid JSON", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_duplicate_bytes_need_explicit_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            case, document = self.make_green_case(Path(tmp))
            duplicate = case / "documents" / "passport-copy.pdf"
            duplicate.write_bytes(document.read_bytes())
            data = json.loads((case / "case.json").read_text())
            data["documents"].append({"id": "passport-copy", "path": "documents/passport-copy.pdf", "sha256": digest(duplicate), "content_review": {"status": "complete", "reviewed_on": "2026-10-26", "reviewer": "reviewer", "notes": "Synthetic content review."}, "expires_on": ""})
            data["requirements"][0]["documents"].append("passport-copy")
            (case / "case.json").write_text(json.dumps(data))
            result = run("audit", str(case))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate bytes", result.stdout)

    def test_inventory_hashes_before_reviews_and_submission_blocks_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            case, document = self.make_green_case(Path(tmp))
            data = json.loads((case / "case.json").read_text())
            data["reviews"]["sources"]["status"] = "pending"
            data["submission"]["status"] = "unknown"
            (case / "case.json").write_text(json.dumps(data))
            inventory = run("inventory", str(case), "--json")
            self.assertEqual(inventory.returncode, 0)
            self.assertIn(digest(document), inventory.stdout)
            self.assertNotEqual(run("audit", str(case)).returncode, 0)
            data["reviews"]["sources"]["status"] = "complete"
            (case / "case.json").write_text(json.dumps(data))
            self.assertNotEqual(run("bundle", str(case)).returncode, 0)
            self.assertFalse((case / "output").exists())

    def test_inventory_discovers_new_private_file_before_manifest_registration(self):
        with tempfile.TemporaryDirectory() as tmp:
            case = Path(tmp) / "private-case"
            self.assertEqual(run("init", str(case), "--route", "initial-ex07").returncode, 0)
            document = case / "documents" / "new-evidence.pdf"
            document.write_bytes(b"%PDF-1.4\nnew synthetic file\n%%EOF\n")
            result = run("inventory", str(case), "--json")
            self.assertEqual(result.returncode, 0)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["registered"], [])
            self.assertEqual(payload["unregistered"], [{"path": "documents/new-evidence.pdf", "bytes": document.stat().st_size, "sha256": digest(document)}])

    def test_bundle_refuses_registered_document_without_requirement_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            case, document = self.make_green_case(Path(tmp))
            extra = case / "documents" / "extra.pdf"
            extra.write_bytes(document.read_bytes())
            data = json.loads((case / "case.json").read_text())
            data["documents"].append({"id": "extra", "path": "documents/extra.pdf", "sha256": digest(extra), "duplicate_of": "passport", "content_review": {"status": "complete", "reviewed_on": "2026-10-26", "reviewer": "reviewer", "notes": "Synthetic content review."}, "expires_on": ""})
            (case / "case.json").write_text(json.dumps(data))
            result = run("bundle", str(case))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("not mapped", result.stdout)
            self.assertFalse((case / "output").exists())

    def test_non_utf8_manifest_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            case = Path(tmp) / "private-case"
            case.mkdir()
            (case / "case.json").write_bytes(b"\xff\xfe")
            result = run("audit", str(case))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("invalid JSON", result.stderr)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()

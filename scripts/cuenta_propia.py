#!/usr/bin/env python3
"""Offline technical preflight for a Spain cuenta propia application package.

This program neither determines immigration eligibility nor submits anything.
It only inventories, checks, and copies files after an agent or appropriate
reviewer has recorded substantive route, source, and content review.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import os
import shutil
import sys
from pathlib import Path

ROUTES = {"modification-191-3", "initial-ex07", "family-ex02"}
DEFAULT_EXTENSIONS = [".pdf", ".doc", ".jpg", ".tif", ".gif"]
DEFAULT_MAX_BYTES = 6_000_000
ROOT = Path(__file__).resolve().parents[1]
TODAY = dt.date.today()


def fail(message: str, code: int = 2) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(code)


def iso_date(value: object, label: str, errors: list[str], *, allow_empty: bool = False, future_ok: bool = False) -> dt.date | None:
    if value in (None, "") and allow_empty:
        return None
    if not isinstance(value, str):
        errors.append(f"{label} must be an ISO date")
        return None
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label} must be an ISO date")
        return None
    if parsed > TODAY and not future_ok:
        errors.append(f"{label} cannot be in the future")
    return parsed


def case_root(raw: str) -> Path:
    path = Path(raw).expanduser().resolve(strict=False)
    try:
        path.relative_to(ROOT)
    except ValueError:
        return path
    fail("CASE must be outside this public repository")


def safe_file(case: Path, relative: object, errors: list[str], label: str) -> Path | None:
    if not isinstance(relative, str) or not relative:
        errors.append(f"{label} needs a non-empty relative path")
        return None
    raw = Path(relative)
    if raw.is_absolute() or ".." in raw.parts:
        errors.append(f"{label} must be a relative path below documents/ without traversal")
        return None
    candidate = case / raw
    documents = case / "documents"
    if documents.is_symlink():
        errors.append(f"{label} cannot use a symlinked documents/ directory")
        return None
    cursor = case
    for part in raw.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            errors.append(f"{label} cannot use symlink path components")
            return None
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(documents.resolve(strict=True))
    except (OSError, ValueError, FileNotFoundError):
        errors.append(f"{label} must be a readable non-symlink file below documents/")
        return None
    if candidate.is_symlink() or not resolved.is_file():
        errors.append(f"{label} must be a readable non-symlink file below documents/")
        return None
    try:
        with resolved.open("rb"):
            pass
    except OSError:
        errors.append(f"{label} is not readable")
        return None
    return resolved


def complete_review(review: object, label: str, errors: list[str], *, evidence: bool = False) -> None:
    if not isinstance(review, dict) or review.get("status") != "complete":
        errors.append(f"{label} must be complete before technical preflight")
        return
    iso_date(review.get("reviewed_on"), f"{label}.reviewed_on", errors)
    if not isinstance(review.get("reviewer"), str) or not review["reviewer"].strip():
        errors.append(f"{label}.reviewer is required")
    if not isinstance(review.get("notes"), str) or not review["notes"].strip():
        errors.append(f"{label}.notes is required")
    if evidence:
        entries = review.get("evidence")
        if not isinstance(entries, list) or not entries:
            errors.append(f"{label}.evidence needs at least one dated official source")
            return
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict) or not all(isinstance(entry.get(key), str) and entry[key].strip() for key in ("url", "section", "checked_on", "notes")):
                errors.append(f"{label}.evidence[{index}] needs url, section, checked_on, and notes")
                continue
            iso_date(entry["checked_on"], f"{label}.evidence[{index}].checked_on", errors)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pdf_sane(path: Path) -> bool:
    """A deliberately lightweight binary check, not validation of PDF semantics."""
    with path.open("rb") as handle:
        head = handle.read(5)
        handle.seek(max(0, path.stat().st_size - 2048))
        tail = handle.read()
    return head == b"%PDF-" and b"%%EOF" in tail


def template(route: str) -> dict:
    return {
        "schema_version": 1,
        "route": route,
        "applicant": {"name": "", "nationality": "", "province": ""},
        "reviews": {
            "sources": {"status": "pending", "reviewed_on": "", "reviewer": "", "notes": "", "evidence": []},
            "route": {"status": "pending", "reviewed_on": "", "reviewer": "", "notes": "", "evidence": []},
            "content": {"status": "pending", "reviewed_on": "", "reviewer": "", "notes": ""},
        },
        "requirements": [],
        "documents": [],
        "portal": {
            "confirmed_on": "",
            "max_file_bytes": DEFAULT_MAX_BYTES,
            "extensions": DEFAULT_EXTENSIONS,
        },
        "submission": {"status": "not_submitted"},
    }


def load_case(case: Path) -> dict:
    manifest = case / "case.json"
    try:
        with manifest.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        fail("case.json does not exist; run init first")
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        fail("case.json is unreadable or invalid JSON")
    if not isinstance(data, dict):
        fail("case.json must contain an object")
    return data


def audit(case: Path, data: dict) -> tuple[list[str], list[str], list[dict]]:
    errors: list[str] = []
    warnings: list[str] = []
    inventory: list[dict] = []
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(data.get("route"), str) or data.get("route") not in ROUTES:
        errors.append("route is not supported")
    applicant = data.get("applicant")
    if not isinstance(applicant, dict) or not all(isinstance(applicant.get(k), str) and applicant[k].strip() for k in ("name", "nationality", "province")):
        errors.append("applicant needs non-empty name, nationality, and province")
    reviews = data.get("reviews")
    if not isinstance(reviews, dict):
        errors.append("reviews must be an object")
    else:
        complete_review(reviews.get("sources"), "reviews.sources", errors, evidence=True)
        complete_review(reviews.get("route"), "reviews.route", errors, evidence=True)
        complete_review(reviews.get("content"), "reviews.content", errors)
    portal = data.get("portal")
    extensions: set[str] = set()
    max_bytes = DEFAULT_MAX_BYTES
    if not isinstance(portal, dict):
        errors.append("portal must be an object")
    else:
        iso_date(portal.get("confirmed_on"), "portal.confirmed_on", errors)
        value = portal.get("max_file_bytes")
        if not isinstance(value, int) or value <= 0:
            errors.append("portal.max_file_bytes must be a positive integer")
        else:
            max_bytes = value
        raw_extensions = portal.get("extensions")
        if not isinstance(raw_extensions, list) or not raw_extensions or any(not isinstance(x, str) or not re.fullmatch(r"\.[A-Za-z0-9]+", x) for x in raw_extensions):
            errors.append("portal.extensions must be non-empty extensions such as .pdf")
        else:
            extensions = {x.lower() for x in raw_extensions}
    documents = data.get("documents")
    document_ids: set[str] = set()
    hashes: dict[str, list[str]] = {}
    if not isinstance(documents, list):
        errors.append("documents must be a list")
        documents = []
    for index, document in enumerate(documents):
        prefix = f"documents[{index}]"
        if not isinstance(document, dict):
            errors.append(f"{prefix} must be an object")
            continue
        doc_id = document.get("id")
        if not isinstance(doc_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", doc_id) or doc_id in document_ids:
            errors.append(f"{prefix}.id must be a unique lowercase identifier")
            continue
        document_ids.add(doc_id)
        path = safe_file(case, document.get("path"), errors, prefix)
        declared_hash = document.get("sha256")
        if not isinstance(declared_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", declared_hash):
            errors.append(f"{prefix}.sha256 must be a lowercase SHA-256")
        complete_review(document.get("content_review"), f"{prefix}.content_review", errors)
        expiry = iso_date(document.get("expires_on"), f"{prefix}.expires_on", errors, allow_empty=True, future_ok=True)
        if expiry and expiry < TODAY:
            errors.append(f"{prefix} is expired")
        if path:
            actual_hash = sha256(path)
            if actual_hash != declared_hash:
                errors.append(f"{prefix} bytes changed since its recorded SHA-256")
            suffix = path.suffix.lower()
            if extensions and suffix not in extensions:
                errors.append(f"{prefix} extension {suffix or '(none)'} is not allowed by portal")
            if path.stat().st_size > max_bytes:
                errors.append(f"{prefix} exceeds portal.max_file_bytes")
            if suffix == ".pdf" and not pdf_sane(path):
                errors.append(f"{prefix} fails the lightweight PDF header/EOF check")
            hashes.setdefault(actual_hash, []).append(doc_id)
            inventory.append({"id": doc_id, "path": str(document.get("path")), "bytes": path.stat().st_size, "sha256": actual_hash})
    requirements = data.get("requirements")
    required_refs: set[str] = set()
    requirement_ids: set[str] = set()
    if not isinstance(requirements, list) or not requirements:
        errors.append("requirements must be a non-empty list")
        requirements = []
    for index, requirement in enumerate(requirements):
        prefix = f"requirements[{index}]"
        if not isinstance(requirement, dict):
            errors.append(f"{prefix} must be an object")
            continue
        req_id = requirement.get("id")
        if not isinstance(req_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", req_id) or req_id in requirement_ids:
            errors.append(f"{prefix}.id must be a unique lowercase identifier")
        else:
            requirement_ids.add(req_id)
        if not all(isinstance(requirement.get(k), str) and requirement[k].strip() for k in ("title", "basis", "source_url")):
            errors.append(f"{prefix} needs title, basis, and source_url")
        status = requirement.get("status")
        if not isinstance(status, str) or status not in {"applicable", "conditional", "inapplicable"}:
            errors.append(f"{prefix}.status must be applicable, conditional, or inapplicable")
            continue
        refs = requirement.get("documents", [])
        if not isinstance(refs, list) or any(not isinstance(x, str) for x in refs) or len(refs) != len(set(refs)):
            errors.append(f"{prefix}.documents must be unique document IDs")
            refs = []
        if status == "applicable" and not refs:
            errors.append(f"{prefix} needs at least one document")
        if status in {"conditional", "inapplicable"} and not (isinstance(requirement.get("reason"), str) and requirement["reason"].strip()):
            errors.append(f"{prefix} needs a reason for {status}")
        if status == "conditional":
            errors.append(f"{prefix} is conditional; resolve it as applicable or inapplicable before bundling")
        for ref in refs:
            if ref not in document_ids:
                errors.append(f"{prefix} references unknown document {ref}")
            else:
                required_refs.add(ref)
    for digest, ids in hashes.items():
        if len(ids) > 1:
            declared = {d.get("id"): d.get("duplicate_of") for d in documents if isinstance(d, dict) and isinstance(d.get("id"), str)}
            if not all(declared.get(doc_id) in ids for doc_id in ids[1:]):
                errors.append(f"duplicate bytes for {', '.join(ids)} need duplicate_of mapping")
            else:
                warnings.append(f"duplicate bytes noted for {', '.join(ids)}")
    for doc_id in document_ids - required_refs:
        warnings.append(f"document {doc_id} is not mapped to a requirement")
    submission = data.get("submission")
    if not isinstance(submission, dict) or not isinstance(submission.get("status"), str) or submission.get("status") not in {"not_submitted", "submitted", "unknown"}:
        errors.append("submission.status must be not_submitted, submitted, or unknown")
    return errors, warnings, inventory


def emit(payload: dict, as_json: bool, *, scope: str = "technical preflight") -> None:
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    for severity in ("errors", "warnings"):
        for line in payload[severity]:
            print(f"{severity[:-1]}: {line}")
    for item in payload.get("documents", []):
        print(f"document: {item['id']} {item['bytes']} bytes {item['sha256']} {item['path']}")
    for item in payload.get("registered", []):
        print(f"registered: {item['id']} {item['bytes']} bytes {item['sha256']} {item['path']}")
    for item in payload.get("unregistered", []):
        print(f"new: {item['bytes']} bytes {item['sha256']} {item['path']} (register after review)")
    state = "GREEN" if scope == "technical preflight" else "COMPLETE"
    print(f"{scope}: " + (state if not payload["errors"] else "BLOCKED"))


def discover_documents(case: Path, errors: list[str]) -> list[dict]:
    """Find regular files without following links or reading their contents."""
    root = case / "documents"
    if root.is_symlink():
        errors.append("documents/ cannot be a symlink")
        return []
    if not root.is_dir():
        errors.append("documents/ does not exist or is not a directory")
        return []
    found: list[dict] = []
    for current, directories, files in os.walk(root, followlinks=False):
        current_path = Path(current)
        for name in list(directories):
            item = current_path / name
            if item.is_symlink():
                errors.append(f"discovery ignores symlinked directory {item.relative_to(case)}")
                directories.remove(name)
        for name in files:
            item = current_path / name
            relative = item.relative_to(case).as_posix()
            if item.is_symlink():
                errors.append(f"discovery ignores symlinked file {relative}")
                continue
            if not item.is_file():
                errors.append(f"discovery ignores non-regular file {relative}")
                continue
            try:
                found.append({"path": relative, "bytes": item.stat().st_size, "sha256": sha256(item)})
            except OSError:
                errors.append(f"discovery cannot read {relative}")
    return sorted(found, key=lambda item: item["path"])


def inventory_case(case: Path, data: dict) -> tuple[list[str], list[dict], list[dict]]:
    """Read only safe file metadata; deliberately independent from legal review."""
    errors: list[str] = []
    registered: list[dict] = []
    registered_paths: set[str] = set()
    documents = data.get("documents")
    if not isinstance(documents, list):
        return ["documents must be a list"], registered, []
    seen: set[str] = set()
    for index, document in enumerate(documents):
        label = f"documents[{index}]"
        if not isinstance(document, dict):
            errors.append(f"{label} must be an object")
            continue
        doc_id = document.get("id")
        if not isinstance(doc_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", doc_id) or doc_id in seen:
            errors.append(f"{label}.id must be a unique lowercase identifier")
            continue
        seen.add(doc_id)
        path = safe_file(case, document.get("path"), errors, label)
        if path:
            relative = path.relative_to(case).as_posix()
            if relative in registered_paths:
                errors.append(f"{label}.path duplicates a registered document path")
                continue
            registered_paths.add(relative)
            registered.append({"id": doc_id, "path": relative, "bytes": path.stat().st_size, "sha256": sha256(path)})
    discovered = discover_documents(case, errors)
    unregistered = [item for item in discovered if item["path"] not in registered_paths]
    return errors, sorted(registered, key=lambda item: item["id"]), unregistered


def command_init(args: argparse.Namespace) -> int:
    case = case_root(args.case)
    manifest = case / "case.json"
    if manifest.exists():
        fail("case.json already exists; init refuses to overwrite a case")
    if case.exists() and not case.is_dir():
        fail("CASE exists but is not a directory")
    case.mkdir(parents=True, exist_ok=True)
    (case / "documents").mkdir(exist_ok=True)
    manifest.write_text(json.dumps(template(args.route), indent=2) + "\n", encoding="utf-8")
    (case / "PRIVATE.md").write_text("# Private case folder\n\nDo not commit this folder or upload personal documents to a public repository.\n", encoding="utf-8")
    print(f"created private case scaffold: {case}")
    return 0


def command_check(args: argparse.Namespace, *, do_bundle: bool = False) -> int:
    case = case_root(args.case)
    data = load_case(case)
    if args.command == "inventory":
        errors, registered, unregistered = inventory_case(case, data)
        payload = {"errors": errors, "warnings": [], "registered": registered, "unregistered": unregistered}
        emit(payload, args.json, scope="inventory")
        return 0 if not errors else 1
    errors, warnings, inventory = audit(case, data)
    payload = {"errors": errors, "warnings": warnings, "documents": inventory}
    if do_bundle:
        if errors:
            emit(payload, False)
            return 1
        if not inventory:
            fail("bundle needs at least one document")
        unmapped = [warning for warning in warnings if warning.startswith("document ") and warning.endswith(" is not mapped to a requirement")]
        if unmapped:
            for warning in unmapped:
                print(f"error: {warning}")
            print("bundle: BLOCKED")
            return 1
        if data.get("submission", {}).get("status") != "not_submitted":
            fail("bundle requires submission.status to be explicitly not_submitted")
        output = case / "output"
        staging = case / "output.incomplete"
        if output.exists() or output.is_symlink() or staging.exists() or staging.is_symlink():
            fail("output already exists; bundle refuses to overwrite it")
        staging.mkdir()
        manifest_items = []
        try:
            for index, item in enumerate(sorted(inventory, key=lambda x: x["id"]), 1):
                source = safe_file(case, item["path"], [], "bundle")
                if source is None or sha256(source) != item["sha256"]:
                    fail("source bytes changed during preflight; bundle aborted")
                name = re.sub(r"[^A-Za-z0-9._() -]", "_", source.name)
                target = staging / f"{index:02d}_{item['id']}_{name}"
                shutil.copyfile(source, target)
                if sha256(target) != item["sha256"]:
                    fail("copied bytes did not match source; bundle aborted")
                manifest_items.append({"id": item["id"], "file": target.name, "bytes": item["bytes"], "sha256": item["sha256"]})
            bundle_manifest = {"created_on": TODAY.isoformat(), "documents": manifest_items, "technical_preflight": "green", "submission": "not_submitted"}
            encoded = json.dumps(bundle_manifest, indent=2, sort_keys=True) + "\n"
            (staging / "manifest.json").write_text(encoded, encoding="utf-8")
            (staging / "manifest.sha256").write_text(hashlib.sha256(encoded.encode()).hexdigest() + "  manifest.json\n", encoding="utf-8")
            os.replace(staging, output)
        except OSError as exc:
            fail(f"bundle stopped; inspect output.incomplete: {exc}")
        print(f"bundle created: {output}")
        return 0
    emit(payload, args.json)
    return 0 if not errors else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline technical preflight for a private cuenta propia case.")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="create an editable private case scaffold")
    init.add_argument("case")
    init.add_argument("--route", choices=sorted(ROUTES), required=True)
    inventory = sub.add_parser("inventory", help="list document hashes without reading contents")
    inventory.add_argument("case")
    inventory.add_argument("--json", action="store_true")
    check = sub.add_parser("audit", help="run technical preflight; 0 means technical checks only")
    check.add_argument("case")
    check.add_argument("--json", action="store_true")
    bundle = sub.add_parser("bundle", help="copy a green package unchanged; never submits")
    bundle.add_argument("case")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "init":
        return command_init(args)
    if args.command == "bundle":
        return command_check(args, do_bundle=True)
    return command_check(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(1)
    except OSError as exc:
        fail(f"filesystem error: {exc}")

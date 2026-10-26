---
name: spain-cuenta-propia
description: Prepare, verify, and when authorized submit a Spanish residencia y trabajo por cuenta propia case, including EX-26 modifications, initial EX-07, and separate family cases.
---

# Spain Cuenta Propia

Use for a Spanish self-employment residence case, especially `cuenta propia`, `EX-26`, `EX-07`, or moving from a work-authorized residence to self-employment.

## Start

1. Read `docs/routes-and-sources.md` and identify the route. Do not use a universal checklist.
2. Ask for or record the private case location, user-authorized sources, province, current permit/TIE, residence and work history, business facts, family members, deadlines, and mode: `prepare` or `prepare-and-submit`. For Ley 14/2013/DNV, record the original authorization/activity, nature and evidenced date of change, continuity versus changed business, and UGE coordination question.
3. Recheck current official sources on the filing date and record source URL, `checked_on`, legal section, and discrepancies in the private case.

## Evidence and preparation

Read `docs/document-review.md`. Build `templates/requirements-matrix.md` from the selected route. Each requirement needs a legal/official basis, applicability decision, evidence, dated substantive review, and a reason when conditional or inapplicable. Resolve every conditional requirement before bundling.

Retrieve original files only from sources the user authorizes. Review the whole passport, identity/name/NIE consistency, dates, signatures, originals, translations/apostilles when applicable, and financial evidence versus the stated facts and forecasts. Do not invent facts in an explanatory letter or business plan; use `templates/` only after evidence is traceable.

Run the local tool on a case stored outside this repository:

```bash
python3 scripts/cuenta_propia.py init /private/case --route modification-191-3
python3 scripts/cuenta_propia.py inventory /private/case
python3 scripts/cuenta_propia.py audit /private/case
python3 scripts/cuenta_propia.py bundle /private/case
```

The audit validates file and metadata integrity only. It cannot prove legal sufficiency, content, signatures, OCR accuracy, or portal acceptance. Read `docs/cli.md` before editing `case.json` and `docs/document-sources.md` when collecting evidence.

## Submission

Follow `docs/submission.md`, `docs/workflow.md`, and use the [ledger](templates/submission-ledger.md). Submit only when the user selected `prepare-and-submit` and the route, representation, and official portal are current. The person intervenes when CAPTCHAs, electronic certificates, AutoFirma, MFA, or physical signatures require it. External messages, payments, and new access require scope covering them.

After portal signing, only an official `resguardo` with REGAGE, time, applicant, form, province and reconciled attachments proves registration. If the portal errors after signing, mark outcome unknown and check records before retrying. Preserve original receipt bytes and hashes; paid tax and uploaded `aportación` are separate confirmations.

## References

- `docs/routes-and-sources.md` — legal routing and official URLs.
- `docs/workflow.md` — end-to-end sequence and stopping conditions.
- `docs/document-review.md` — evidence review protocol.
- `docs/document-sources.md` — practical collection map.
- `docs/cli.md` — case schema and command sequence.
- `docs/submission.md` — official portal sequence and recovery.
- `docs/search-intent.md` — public query language; no volume claim.

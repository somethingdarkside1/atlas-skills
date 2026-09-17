---
status: review
kind: build
blocked_by: ["core-model/01"]
---

# 03: Write the verification method

## Delivers
One reusable method that chooses useful checks from the deliverable, risks, and acceptance criteria.

Source: Matt TDD/code-review; original F04, F21-F22. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [x] Record exact input revision, checks actually run, results, limits, and human-only judgments.
- [x] Use checks that could fail for an incorrect result rather than descriptions that merely mirror implementation.
- [x] Include positive and relevant failure cases for code, factual/visual checks for a document, and limits of each observation.
- [x] Keep builder verification distinct from independent review and from platform approval.

## Delivered
### 2026-09-17
Branch `codex/shared-methods-03-04` from `origin/main` at `24b24ef`.

Made: [the verification method](../../methods/verification.md); `build-it` and `review-it` rows in [the method consumers](../../methods/README.md); [replayable fixtures](../../tests/fixtures/verification/README.md) with a late fee function carrying one seeded defect and an opening hours page with one false time; and [the evidence note](../../notes/2026-09-17-review-verification-and-prototype-methods.md), shared with task 04. The method returns the identity (revision or checksum line), each check with what was seen and its limit, open items, and any platform status quoted as reported.

Checked in scratch copies, following the method as a reviewer: a builder check that copies the code's formula passed 4 of 4, and a synthetic CI status reported success for that check only. `check_contract.py`, with values from the criteria, failed criterion 2 (4 days late gave 50, expected 25) and exited 1; after a scratch-only fix it passed 7 of 7 while the copied check failed. `check_page.py` found Saturday 09:00 to 17:00 on the page against 10:00 to 16:00 in the source and exited 1; notice order passed, declared contrast was 6.57, and a scratch color break to 2.99 failed. Phone layout was recorded as not run and noticeability as a human-only judgment. `python3 scripts/check-project.py` passed with 7 parts, 24 tasks, 111 documents, 663 local links, and no errors; `git diff --check` passed.

Not checked: rendering in a browser, a reviewer in a separate context, a real CI run, and loading from an installed consumer (task 05 and the work-skills migration). The author seeded the defects and ran every case in the same context.

Version: 735fe842c7c0 (12 files)

### 2026-09-18
Applied the review findings on `9f7d0bc`, same branch. The method now asks for an identity with its file list, paths from the project root in byte order, instead of a fixed command. It no longer uses the glossary's Avoid words, and its consumer triggers load only when the planned or delivered checks could pass for a wrong result, cannot be rerun, or rest on a platform status. The brief and map record the chosen minimum outputs. `check_page.py` now fails a day listed twice and reports a missing or unreadable notice color as a failed check instead of stopping.

Checked: every case was rerun in a fresh scratch copy that kept the repository paths. The late fee and page results were unchanged: contract check exit 1, then 0 after the scratch fix; mirror check 0, then 1; page check exit 1 on Saturday; contrast 6.57, break 2.99. A page listing Saturday twice, which passed before, now fails with exit 1; `background-color`, which crashed before, is read as 6.57; `#fff` fails as unreadable. Fixture identities in the evidence note were recomputed from repository paths. `python3 scripts/check-project.py` passed with 7 parts, 24 tasks, 111 documents, 666 local links, and no errors; `git diff --check` passed.

Not checked: the same limits as on 2026-09-17.

Files, in byte order from the repository root: `methods/README.md`, `methods/verification.md`, `notes/2026-09-17-review-verification-and-prototype-methods.md`, and the 9 files in `tests/fixtures/verification/`.

Version: e7fa9b5c70c7 (12 files)

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

---
status: review
kind: build
blocked_by: ["core-model/01"]
---

# 02: Write the diagnosis method

## Delivers
One reusable method for reproducing a symptom, testing competing explanations, and identifying a justified next action.

Source: Matt diagnosing-bugs; verification weakness in original F03. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [x] Record a failing signal or explain why reproduction is unavailable.
- [x] Separate observations from hypotheses and test the cheapest discriminating next check.
- [x] Bound unsuccessful investigation and retain the reproduction and uncertainty in the output.
- [x] Exercise a software failure and a non-code process or data-quality failure without requiring the same tooling.

## Delivered
Attempt started 2026-09-15 in `/Users/vitali/Documents/Projects/Skills Po`, branch `codex/shared-methods-02-diagnosis`, from fetched main `6737912`. The checkout and index were clean, no merge was active, and no resumable method branch or open PR existed. Accepted blocker output `208b197` and its acceptance record are accessible in this base.

Selected implementation: one plain canonical source at `methods/diagnosis.md`, with conditional consumer declarations. Its minimum output is the reproduction or limit, observations, tested explanations, remaining uncertainty, and next justified action. These are reversible implementation choices within the adopted boundary. Demonstrate a software failure, a data-quality failure, and a bounded investigation with missing evidence; retain exact inputs and observed results. Bundling and operation migration remain with their named tasks.

Delivered the [canonical diagnosis source](../../methods/diagnosis.md), [conditional consumer declaration](../../methods/README.md), and [replayable scratch fixtures](../../tests/fixtures/diagnosis/README.md). The [dated evidence record](../../notes/2026-09-15-review-diagnosis-method.md) identifies candidate bytes with SHA-256 hashes and records actual software, data, and inconclusive process demonstrations. Python 3.9.6 software checks exited 1 on the retained defective fixture and 0 after a scratch-only correction, with four contract cases. Direct row inspection accounted for the USD 60 data discrepancy; two evidence checks left the approval-timing report inconclusive.

`python3 scripts/check-project.py` passed with 7 parts, 24 tasks, 110 documents, 645 local links, and no errors; `git diff --check` passed. Structural checks do not prove behavior. Demonstrations were synthetic and run by the author in the same context; installed consumer wiring, independent validation, and release acceptance remain outside scope.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

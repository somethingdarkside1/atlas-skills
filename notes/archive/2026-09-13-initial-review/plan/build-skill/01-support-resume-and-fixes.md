---
status: todo
blocked_by: ["five-things/01"]
---

# 01: Support interrupted work and review fixes

## Delivers
A builder entry path for a new ready task, an interrupted attempt, and a current review finding, with an explicit delivery identity.

Priority and source: P1; F03-F04. See the [framework review](../../../../2026-09-13-review-atlas-framework.md).

## Check by
Start a task, interrupt it after a partial output, resume it, and then fix a review finding on that output.

## Done when
- [ ] An explicit task id is checked for eligibility and mode before mutation.
- [ ] Resuming reuses the appropriate attempt, files, and branch.
- [ ] An unresolved answer is persisted as a waiting condition with its question.
- [ ] Each completed delivery identifies its artifact revision and actual check results.

## Delivered
Pending implementation.

## Review
Pending review.

---
status: todo
blocked_by: ["01"]
---

# 02: Make GitHub task start recoverable

## Delivers
A shared GitHub reference and builder start sequence that resolves complete tracker state and prepares the workspace before progress is recorded.

Priority and source: P1; F02, F09, F23. See the [framework review](../../../../2026-09-13-review-atlas-framework.md).

## Check by
Use an isolated GitHub test repository or faithful API fixture to start a decided part and resume failures after claim, issue creation, push, and PR creation.

## Done when
- [ ] A normal start does not fail its clean-tree check because of its own map edit.
- [ ] Repository, account, parent, dependencies, branch, and PR are resolved explicitly with all pages read.
- [ ] Repeated execution reuses remote objects and records recovery after partial failure.
- [ ] Assignment remains ownership evidence, with progress represented by the agreed contract.
- [ ] The documented concurrency limit and claim-conflict behavior are verified.

## Delivered
Pending implementation.

## Review
Pending review.

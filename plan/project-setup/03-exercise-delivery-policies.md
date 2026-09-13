---
status: todo
kind: check
blocked_by: ["02", "work-skills/02"]
---

# 03: Exercise project-owned delivery policies

## Delivers
Run records showing identical Atlas acceptance behavior under different project commit, branch, PR, and merge policies.

Source: Original F02, F08-F10, F24. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] Exercise local commits, an isolated worktree, a PR left for a person, and an authorized merge in scratch projects.
- [ ] Existing user authorization is retained; a missing permission blocks only the dependent delivery action.
- [ ] Unrelated staged and unstaged changes survive, including edits in a file Atlas also touches.
- [ ] An accepted task remains accurately reported when a push or merge fails, and a changed integrated result receives fresh checks.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

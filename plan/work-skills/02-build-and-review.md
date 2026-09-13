---
status: todo
kind: build
blocked_by: ["core-model/03", "shared-methods/02", "shared-methods/03"]
---

# 02: Refine delivery and review operations

## Delivers
Revised build-it and review-it procedures that handle a new task, an interrupted attempt, verification failure, review findings, and acceptance.

Source: Original F02-F04, F08-F10, F21-F22; second-pass candidate fixes. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] The builder validates eligibility and resumes the identified attempt without discarding partial work.
- [ ] The reviewer receives a fixed target plus relevant standards and can report findings without performing a merge.
- [ ] Both procedures record owned changes and actual verification evidence, including unresolved human judgment.
- [ ] Review findings lead to a new delivery and fresh review; stale approval cannot complete changed work.
- [ ] Commits, branches, PR approval, and merge decisions are delegated to applicable project policy.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

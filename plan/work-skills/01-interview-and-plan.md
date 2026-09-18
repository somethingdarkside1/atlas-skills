---
status: todo
kind: build
blocked_by: ["06", "core-model/02", "shared-methods/01"]
---

# 01: Refine interview and planning operations

## Delivers
Revised interview-me and plan-it contracts and procedures, with a complete brief-only-to-tasks and replan route.

Source: Original F01, F11, F17, F19-F20. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] State required/conditional reads, owned changes, finish evidence, and recovery for both operations.
- [ ] A settled brief with zero tasks routes to planning; a small clear change can become one task.
- [ ] Persist brief revisions and settled minor choices; update existing parent work rather than duplicate it.
- [ ] Preserve task ids, cancellation history, incoming dependencies, and human acceptance edits when replanning.
- [ ] Use the shared method pointer and the common project-policy rule.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

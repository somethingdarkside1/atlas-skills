---
status: todo
kind: build
blocked_by: ["01"]
---

# 02: Define task evidence and transitions

## Delivers
A minimal versioned local task/brief contract with delivery and review evidence, stable ids, waiting, cancellation, and readiness rules.

Source: Original F01, F03-F04, F09, F11, F21; second-pass task-id and review-state proposals. See the [package brief](brief.md), the [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md), and the [evidence weight analysis](../../notes/2026-09-17-research-evidence-weight.md), which proposes a light default and asks that the first 0.2 runs be counted before the fields are fixed.

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] Give each transition a guard, owner, resulting state, and recovery action.
- [ ] Bind a review to an artifact revision and brief revision with a usable non-Git representation.
- [ ] A completed task means accepted work; integration is separately evidenced unless the task explicitly delivers integration.
- [ ] A dependent task requires both accepted blockers and access to their exact needed outputs.
- [ ] Exercise interruption, changes requested, changed scope, canceled blockers, empty plans, and two deliveries on one day.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

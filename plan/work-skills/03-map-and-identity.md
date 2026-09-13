---
status: todo
kind: build
blocked_by: ["core-model/03", "context-routing/01"]
---

# 03: Refine map maintenance and identity

## Delivers
A map-it procedure for validated rendering, splitting, and renaming that preserves task, decision, and part identity.

Source: Original F14-F16, F19. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] Validate missing references, duplicate ids, cycles, self-dependencies, and cross-file edges before deriving views.
- [ ] Separate redrawing a view from changing work decomposition.
- [ ] Resolve split parts and glossary entries consistently for every consumer.
- [ ] Recompute parent status only from the adopted nonempty accepted scope and record the owned repair.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

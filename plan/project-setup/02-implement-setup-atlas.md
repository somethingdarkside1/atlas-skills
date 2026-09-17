---
status: todo
kind: build
blocked_by: ["01", "core-model/02", "work-skills/06"]
---

# 02: Implement setup-atlas adoption

## Delivers
A separately invoked setup-atlas skill that creates missing homes and adopts the instruction pointer without destructive replacement.

Source: Original F06-F07 and authoring exceptions F27. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] Handle empty, populated, partial, legacy-context, and symlinked-instruction fixtures.
- [ ] Preserve project policy and custom prose; expose the exact adoption diff.
- [ ] Readiness errors point to the actual installed setup command.
- [ ] Repeat setup without creating duplicate blocks, parts, decisions, or questions.
- [ ] State that setup changes policy text only within the authorized adoption scope and does not perform Git delivery merely by configuring it.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

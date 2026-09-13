---
status: todo
blocked_by: ["02", "review-skill/02"]
---

# 03: Align automatic continuation with invocation

## Delivers
A documented, supported choice for explicit invocation and automatic continuation, with a bounded build-review run in each claimed harness.

Priority and source: P1; F12-F13. See the [framework review](../../notes/2026-09-13-review-atlas-framework.md).

## Check by
Run one successful delivery-review cycle, one failed build, one review retry, and one human-wait scenario through the chosen entry point.

## Done when
- [ ] Skill invocation policy and orchestration agree in every advertised supported harness.
- [ ] Each automatic step advances evidence or stops with the exact resumable target.
- [ ] Pending human action, unchanged state, and a run limit stop continuation without repeated review calls.
- [ ] README and metadata describe only the mode demonstrated by the recorded run.

## Delivered
Pending implementation.

## Review
Pending review.

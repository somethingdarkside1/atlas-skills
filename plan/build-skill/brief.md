---
part: build-skill
---

# Build skill

## Problem
The builder has no complete retry contract, mutates state before GitHub preflight, and can commit changes it does not own. See the [framework review](../../notes/2026-09-13-review-atlas-framework.md) for the source evidence.

## Outcome
One task can start, pause, resume, deliver, and answer review findings while preserving unrelated work and recoverable external state.

## Decisions
[0007](../../decisions/0007-branches-only-with-github.md): existing accepted constraint.

This is a review follow-up brief drafted on 2026-09-13. The existing decisions remain authoritative. Proposed changes are candidates for the [contract task](../five-things/01-settle-workflow-contract.md), which records the chosen rules before dependent implementation. The review's task breakdown is a proposed sizing, not a completed interview or sizing round.

## Out of scope
Publication or deployment implied solely by building a task, or a new general-purpose coding methodology.

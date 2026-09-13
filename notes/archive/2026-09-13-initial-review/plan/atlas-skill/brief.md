---
part: atlas-skill
---

# Atlas skill

## Problem
Initialization, status repair, handoff routing, and automatic continuation can contradict the state they read. See the [framework review](../../../../2026-09-13-review-atlas-framework.md) for the source evidence.

## Outcome
Repeatable adoption and routing that recommend an eligible action from current evidence, with supported and bounded automatic execution.

## Decisions
[0002](../../../../../decisions/0002-five-things-at-the-root.md): existing accepted constraint.
[0004](../../../../../decisions/0004-self-describing-files.md): existing accepted constraint.

This is a review follow-up brief drafted on 2026-09-13. The existing decisions remain authoritative. Proposed changes are candidates for the [contract task](../five-things/01-settle-workflow-contract.md), which records the chosen rules before dependent implementation. The review's task breakdown is a proposed sizing, not a completed interview or sizing round.

## Out of scope
Unattended operation in untested harnesses or a new scheduling platform.

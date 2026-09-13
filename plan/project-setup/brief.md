---
part: project-setup
---

# Project setup

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Adopt the five things safely and point Atlas at existing project delivery policy while keeping repeated setup idempotent.

## Decisions
[0012](../../decisions/0012-atlas-owns-work-projects-own-delivery.md): proposed release direction.
[0015](../../decisions/0015-setup-adopts-routing-observes.md): proposed release direction.

The package is ready to discuss from this brief. The core-model decision task adopts the recommended boundaries before dependent implementation. Proposed defaults guide the interview; they are not a record of answers the user has not given.

### Start prompt

> Read INDEX.md, plan/README.md, plan/project-setup/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Choose how to expose an unresolved policy choice; how managed-block versions coexist with custom edits; how non-Git projects stay simple.

### Reads, changes, and finish

- Read scope: Applicable AGENTS.md and CLAUDE.md; current project conventions; setup proposal 0015; migration contract.
- Owned changes: The setup-atlas skill, adoption templates, and example project-policy blocks.
- Package finished when: New, existing, partial, and linked-instruction projects are adopted without losing content or silently changing their delivery policy.
- Coordination: select one eligible task, record its branch and current work in Delivered, and keep shared contract edits with their named owner. Follow affected cross-package dependencies when the evidence requires it.

### Tasks

- [01: Settle setup and policy adoption](01-settle-adoption-contract.md)
- [02: Implement setup-atlas adoption](02-implement-setup-atlas.md)
- [03: Exercise project-owned delivery policies](03-exercise-delivery-policies.md)

## Out of scope
The hosted task adapter and unattended cross-skill orchestration are deferred from the first public revision. This package changes only its declared ownership; another package owns adjacent delivery or method behavior. Source publication of this plan does not count as implementation or release acceptance.

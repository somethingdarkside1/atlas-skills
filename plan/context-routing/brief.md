---
part: context-routing
---

# Context routing

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Use a small directory of meaningful pointers to load the relevant part and method while retaining the ability to expand across affected boundaries.

## Decisions
[0016](../../decisions/0016-pointers-before-label-taxonomy.md): proposed release direction.

The package is ready to discuss from this brief. The core-model decision task adopts the recommended boundaries before dependent implementation. Proposed defaults guide the interview; they are not a record of answers the user has not given.

### Start prompt

> Read INDEX.md, plan/README.md, plan/context-routing/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Choose whether existing part ids suffice; thresholds for splitting; what evidence triggers scope expansion. Measure rather than assume token savings.

### Reads, changes, and finish

- Read scope: INDEX.md; map and plan format; context-pointer research; a representative operation and fixture.
- Owned changes: Pointer schema/resolution, map split lookup, and focused-read evaluation cases.
- Package finished when: An agent finds required evidence with fewer loaded reference bytes when possible and catches the same cross-boundary defects as a broad-read baseline.
- Coordination: select one eligible task, record its branch and current work in Delivered, and keep shared contract edits with their named owner. Follow affected cross-package dependencies when the evidence requires it.

### Tasks

- [01: Implement focused context pointers](01-resolve-focus-pointers.md)
- [02: Measure focus and context cost](02-measure-context-cost.md)

## Out of scope
The hosted task adapter and unattended cross-skill orchestration are deferred from the first public revision. This package changes only its declared ownership; another package owns adjacent delivery or method behavior. Source publication of this plan does not count as implementation or release acceptance.

---
part: context-routing
---

# Context routing

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Use a small directory of meaningful pointers to load the relevant part and method while retaining the ability to expand across affected boundaries.

## Decisions
[0016](../../decisions/0016-pointers-before-label-taxonomy.md): accepted release direction.

The release boundaries were adopted through [core-model/01](../core-model/01-settle-boundaries.md) on 2026-09-15. Use the linked accepted decisions as settled input; the package-specific choices below remain with their named tasks, and implementation still requires accepted, accessible blocker outputs.

### Start prompt

> Read INDEX.md, plan/README.md, plan/context-routing/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Use existing part ids and pointers under decision 0016. Choose thresholds for splitting and concrete scope-expansion signals; measure retrieval completeness as well as context cost before proposing another classification.

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

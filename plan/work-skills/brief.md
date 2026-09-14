---
part: work-skills
---

# Work skills

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Give all eight Atlas operations explicit reads, owned changes, completion evidence, and recovery, with local canonical work and project-owned delivery.

## Decisions
[0012](../../decisions/0012-atlas-owns-work-projects-own-delivery.md): accepted release direction.
[0013](../../decisions/0013-local-tasks-first.md): accepted release direction.

The release boundaries were adopted through [core-model/01](../core-model/01-settle-boundaries.md) on 2026-09-15. Use the linked accepted decisions as settled input; the package-specific choices below remain with their named tasks, and implementation still requires accepted, accessible blocker outputs.

[0019](../../decisions/0019-acceptance-follows-output-and-scope.md) and [0020](../../decisions/0020-decide-only-the-selected-scope.md) settle acceptance and interview boundaries. Keep the direct one-task route for clear work, reuse applicable evidence after impact assessment, and update only homes whose facts change. [0018](../../decisions/0018-one-method-modular-skills.md) makes these operations parts of one product without authorizing unattended orchestration.

### Start prompt

> Read INDEX.md, plan/README.md, plan/work-skills/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Choose the smallest useful read scope and retry receipt per operation; decide how to report integration pending without redefining review.

### Reads, changes, and finish

- Read scope: Selected task and brief; core contract; applicable method; the operation source and its templates; second-pass candidate branch.
- Owned changes: Operation SKILL.md files, their metadata, and the project-format changes expressly owned by the task.
- Package finished when: The interview-plan-build-review cycle and the map/prototype/handoff routes run without hard-coded commits, branches, PRs, or merges in their method logic.
- Coordination: select one eligible task, record its branch and current work in Delivered, and keep shared contract edits with their named owner. Follow affected cross-package dependencies when the evidence requires it.

### Tasks

- [01: Refine interview and planning operations](01-interview-and-plan.md)
- [02: Refine delivery and review operations](02-build-and-review.md)
- [03: Refine map maintenance and identity](03-map-and-identity.md)
- [04: Refine prototype and handoff operations](04-prototype-and-handoff.md)
- [05: Cut over routing and remove provider coupling](05-cut-over-router-and-contracts.md)

## Out of scope
The hosted task adapter and unattended cross-skill orchestration are deferred from the first public revision. This package changes only its declared ownership; another package owns adjacent delivery or method behavior. Source publication of this plan does not count as implementation or release acceptance.

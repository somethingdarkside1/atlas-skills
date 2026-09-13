---
part: core-model
---

# Core model

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Define the boundary between Atlas work, reusable methods, project delivery, and evidence so every consumer can make the same state decision.

## Decisions
[0012](../../decisions/0012-atlas-owns-work-projects-own-delivery.md): proposed release direction.
[0013](../../decisions/0013-local-tasks-first.md): proposed release direction.
[0017](../../decisions/0017-evidence-before-release.md): proposed release direction.

The package is ready to discuss from this brief. The core-model decision task adopts the recommended boundaries before dependent implementation. Proposed defaults guide the interview; they are not a record of answers the user has not given.

### Start prompt

> Read INDEX.md, plan/README.md, plan/core-model/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Choose delivery identity with and without Git; how canceled blockers are handled; when a changed brief invalidates accepted work.

### Reads, changes, and finish

- Read scope: GLOSSARY.md; plan/README.md; decisions/0012 through 0017; initial findings F01-F04, F09, F11-F13, F17-F18, F21.
- Owned changes: The glossary, task/brief format, common operation contract, and format migration.
- Package finished when: A local task can be planned, delivered, reviewed, retried, canceled, and reopened without inferring completion from a GitHub field.
- Coordination: select one eligible task, record its branch and current work in Delivered, and keep shared contract edits with their named owner. Follow affected cross-package dependencies when the evidence requires it.

### Tasks

- [01: Settle the release boundaries](01-settle-boundaries.md)
- [02: Define task evidence and transitions](02-define-task-evidence.md)
- [03: Migrate the current project format](03-migrate-current-projects.md)

## Out of scope
The hosted task adapter and unattended cross-skill orchestration are deferred from the first public revision. This package changes only its declared ownership; another package owns adjacent delivery or method behavior. Source publication of this plan does not count as implementation or release acceptance.

---
part: validation
---

# Validation

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Establish repeatable structural and behavioral evidence for the method, failure recovery, installation, and claims of lower context cost.

## Decisions
[0017](../../decisions/0017-evidence-before-release.md): proposed release direction.

The package is ready to discuss from this brief. The core-model decision task adopts the recommended boundaries before dependent implementation. Proposed defaults guide the interview; they are not a record of answers the user has not given.

### Start prompt

> Read INDEX.md, plan/README.md, plan/validation/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Choose representative software and non-code cases; acceptable regression bar; how many independent runs are affordable and informative.

### Reads, changes, and finish

- Read scope: Current contracts and package acceptance; source skills; examples; relevant old failure findings.
- Owned changes: Check scripts, fixtures, test runner guidance, and dated run records.
- Package finished when: Cold-context runs cover normal work, interruption, failed verification, human judgment, stale review, adoption, and cross-medium delivery with recorded outcomes.
- Coordination: select one eligible task, record its branch and current work in Delivered, and keep shared contract edits with their named owner. Follow affected cross-package dependencies when the evidence requires it.

### Tasks

- [01: Extend structural contract checks](01-check-structural-contracts.md)
- [02: Create realistic behavioral fixtures](02-create-behavior-fixtures.md)
- [03: Run independent end-to-end acceptance](03-run-cold-context-acceptance.md)

## Out of scope
The hosted task adapter and unattended cross-skill orchestration are deferred from the first public revision. This package changes only its declared ownership; another package owns adjacent delivery or method behavior. Source publication of this plan does not count as implementation or release acceptance.

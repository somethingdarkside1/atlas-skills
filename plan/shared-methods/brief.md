---
part: shared-methods
---

# Shared methods

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Provide reusable interviewing, diagnosis, verification, and prototype methods with precise triggers and useful outputs, authored once and packaged for their consumers.

## Decisions
[0014](../../decisions/0014-shared-methods-travel-with-consumers.md): proposed release direction.

The package is ready to discuss from this brief. The core-model decision task adopts the recommended boundaries before dependent implementation. Proposed defaults guide the interview; they are not a record of answers the user has not given.

### Start prompt

> Read INDEX.md, plan/README.md, plan/shared-methods/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Choose the minimum method output; where domain modeling joins interviewing; whether a method has a demonstrated standalone invocation use.

### Reads, changes, and finish

- Read scope: Core contract; comparison research; relevant Matt reference methods; the consuming skill for the selected method.
- Owned changes: Four canonical method sources, their consumer declaration, and the generation/check path for bundled references.
- Package finished when: Each method works in at least two relevant contexts and every selectively installed consumer has its required reference.
- Coordination: select one eligible task, record its branch and current work in Delivered, and keep shared contract edits with their named owner. Follow affected cross-package dependencies when the evidence requires it.

### Tasks

- [01: Write the interviewing and domain method](01-interview-and-model.md)
- [02: Write the diagnosis method](02-diagnose-with-evidence.md)
- [03: Write the verification method](03-verify-by-medium.md)
- [04: Write the prototype method](04-prototype-to-learn.md)
- [05: Bundle method references for each consumer](05-bundle-method-references.md)

## Out of scope
The hosted task adapter and unattended cross-skill orchestration are deferred from the first public revision. This package changes only its declared ownership; another package owns adjacent delivery or method behavior. Source publication of this plan does not count as implementation or release acceptance.

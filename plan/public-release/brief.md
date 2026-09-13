---
part: public-release
---

# Public release

## Problem
The [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md) identifies responsibilities and failure paths that the initial skill-by-skill plan did not separate sufficiently. This work package owns a bounded part of the revised method.

## Outcome
Publish a clearly attributed, installable, verified Atlas release under Vitali Liouti, with accurate documentation and a maintainable contribution path.

## Decisions
[0013](../../decisions/0013-local-tasks-first.md): proposed release direction.
[0017](../../decisions/0017-evidence-before-release.md): proposed release direction.

The package is ready to discuss from this brief. The core-model decision task adopts the recommended boundaries before dependent implementation. Proposed defaults guide the interview; they are not a record of answers the user has not given.

### Start prompt

> Read INDEX.md, plan/README.md, plan/public-release/brief.md, and the first eligible task. Use concrete scenarios to challenge the unresolved choices, find accessible facts yourself, and reuse prior accepted answers. Record the chosen decisions and acceptance checks before implementing the selected task. Complete its evidence and follow the project delivery policy.

### Choices to settle

Choose the release version, supported harnesses and supported selective installs based on evidence; confirm final public copy and credit wording.

### Reads, changes, and finish

- Read scope: README.md; LICENSE; manifests; accepted contract and test results; source provenance; project delivery policy.
- Owned changes: Public documentation, package metadata, release checklist and tags, and the public repository presentation.
- Package finished when: A clean user profile can install the supported package, follow the guide, and reproduce the documented route at the released revision.
- Coordination: select one eligible task, record its branch and current work in Delivered, and keep shared contract edits with their named owner. Follow affected cross-package dependencies when the evidence requires it.

### Tasks

- [01: Write the public guide and provenance](01-write-public-guide-and-credit.md)
- [02: Verify clean-profile installation](02-verify-installation-matrix.md)
- [03: Publish the verified Atlas release](03-publish-verified-release.md)

## Out of scope
The hosted task adapter and unattended cross-skill orchestration are deferred from the first public revision. This package changes only its declared ownership; another package owns adjacent delivery or method behavior. Source publication of this plan does not count as implementation or release acceptance.

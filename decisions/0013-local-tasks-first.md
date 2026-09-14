---
part: core-model
date: 2026-09-13
status: accepted
---

# The first public revision uses local task files

The first public revision keeps canonical briefs and tasks in local files, with project-owned GitHub source hosting, PR delivery, and issue links for coordination. A future hosted task adapter must preserve Atlas identity, evidence, dependencies, and recovery; mapping issue or PR status alone cannot establish acceptance, and implementation waits for an adopter and lifecycle tests. Adopted on 2026-09-15 in [core-model/01](../plan/core-model/01-settle-boundaries.md), this supersedes [0001](0001-one-home-for-the-plan.md) for the revised release; legacy tracker authority remains intact until an explicit supported migration.

Considered: native GitHub tracking in core; a generic tracker framework now; bidirectional mirroring.
Revisit when: a real adopter needs hosted task tracking and can exercise the same lifecycle tests.

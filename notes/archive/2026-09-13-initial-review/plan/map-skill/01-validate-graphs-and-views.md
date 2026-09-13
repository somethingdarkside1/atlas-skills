---
status: todo
blocked_by: ["five-things/01"]
---

# 01: Validate graphs before drawing views

## Delivers
A repeatable validation and rendering path for part dependencies, task blockers, and glossary relationships, with meaningful invalid graph fixtures.

Priority and source: P2; F15, F19. See the [framework review](../../../../2026-09-13-review-atlas-framework.md).

## Check by
Check missing targets, duplicate ids, self-edges, cycles, multiword terms, and a valid map; regenerate the valid views twice.

## Done when
- [ ] Invalid dependencies include the exact offending ids or cycle path and a repair action.
- [ ] Rendered nodes, labels, classes, and edges agree with the declared source and orientation.
- [ ] Glossary relationship checks distinguish authored meaning from mere word occurrence.
- [ ] The valid regeneration is stable and all graph checks cover split-file inputs.

## Delivered
Pending implementation.

## Review
Pending review.

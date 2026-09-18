---
part: work-skills
date: 2026-09-17
status: accepted
---

# A delivery records its version in one line

Each Delivered entry ends with one `Version:` line, a short checksum of the delivered files (the same with or without git, and unlike a commit hash it can sit inside the commit it describes); a delivery that is not a file names what to look at and the date. `/review-it` recomputes it first, writes a matching `Reviewed:` line when it agrees, and when it does not, says the files changed since delivery and hands back to `/build-it`. This is the default weight of evidence under [0019](0019-acceptance-follows-output-and-scope.md): it identifies what was delivered and keeps no copy, and a project that wants fuller records says so in its own instructions. Accepted by Vitali on 2026-09-17 in the work-skills interview, answering choice 3 of the [whole-set review](../notes/2026-09-17-review-skills-as-a-whole.md); the checksum form follows the evidence-weight research on `codex/skills-patch-0-2`, and [core-model/02](../plan/core-model/02-define-task-evidence.md) owns the exact fields.

Considered: nothing extra (a stale review can pass); full revision records as in core-model/01 (too heavy for work that is not code); a commit hash (cannot name the commit that holds it).
Revisit when: a review passes something that changed after delivery and the line did not catch it, or ten real tasks show the line never catches anything.

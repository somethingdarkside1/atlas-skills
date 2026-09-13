---
status: todo
blocked_by: ["five-things/01", "build-skill/03"]
---

# 02: Make handoffs safe to resume

## Delivers
A uniquely identified handoff with enough state pointers to resume work, plus a read rule that lets current evidence supersede stale directions.

Priority and source: P1; F05, F08, F26. See the [framework review](../../../../2026-09-13-review-atlas-framework.md).

## Check by
Create two same-day handoffs, add a later prototype note, finish the earlier target, and resume from a fresh context with unrelated edits present.

## Done when
- [ ] The handoff locates the current task, attempt or branch, artifact, pending question, and next action where relevant.
- [ ] Relevant handoffs remain discoverable when another note is newer.
- [ ] A stale or completed target is detected without editing the historical note.
- [ ] The commit contains only its authorized owned changes and a repeated park retains prior notes.

## Delivered
Pending implementation.

## Review
Pending review.

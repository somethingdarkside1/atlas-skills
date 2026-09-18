# Decisions

One short file per choice that is hard to reverse, would surprise a future reader, and came from a real trade-off. If any of the three is missing, it is not a decision; it is a note or a line in the brief.

File name: `NNNN-<slug>.md`, numbered globally, never renumbered. The next number is one more than the highest here. The map's part sections link every decision that belongs to them, so browse by part there; `grep '^part:'` finds them by part here.

## Template

```md
---
part: wordmark
date: 2026-09-14
status: accepted
---

# One mark, not a family

The studio wanted a logo family (mark, monogram, pattern) and a launch in six weeks. One wordmark done well covers every surface listed in the brief, and a family would spend the six weeks on variants nobody asked for. We ship one mark and revisit when a second surface needs a symbol.

Considered: a full family (rejected for time); a symbol only (rejected because the name is unknown).
Revisit when: an app icon or a social avatar is needed, where a wordmark fails.
```

`status` is `proposed`, `accepted`, or `superseded`; a superseded decision adds `superseded_by: NNNN` and stays in place. The title is a full sentence saying what was decided. Keep the body to one to three sentences; Considered and Revisit when are one line each and may be omitted.

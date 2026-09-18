# Notes

Dated, write-once files. A note records what was true on a date: a handoff, a prototype verdict, research findings, a review. Leave a note alone once its day is over; a later correction is a new note that links the old one. Anything that stays true gets copied into the glossary, the map, the plan, or a decision.

File name: `YYYY-MM-DD-<kind>-<slug>.md`. When that name is taken, add `-2`, `-3`, and so on. A handoff's slug starts with the time as `HHMM` (`2026-09-15-handoff-1740-lockups-half-drawn.md`), so handoff names sort in the order they were written. A skill reads a note when the map, a task, or a handoff points to it. `/atlas` reads the newest handoff, and `/interview-me`, `/plan-it`, `/build-it`, and `/prototype-it` read it when it targets their part or task.

## Template

```md
---
date: 2026-09-14
kind: prototype
part: wordmark
---

# Wordmark in three weights

## Summary
Three sentences at most.

## Detail
Whatever the reader needs. Link the five things instead of repeating them.

## Copied into
Which home received the durable result, or "nothing durable".
```

`kind` is `handoff`, `prototype`, `research`, or `review`. `part` is a part id or `project`.

## Handoffs

A handoff's Summary ends with a `Next: /command <id>` line naming the command that resumes the target, never `/atlas`, and its Detail opens with `Target: <task id or part id>, <its status today>`. When the session was about the whole project, the line is `Target: project, <n> sketched, <n> decided, <n> building (<ids>), <n> done`, the shape of `/atlas` line one. A handoff is live while its target's status today equals the status on that line. Once they differ, the handoff is history. A live handoff is a hint, not an order: `/atlas` still routes a task in review and any open question first. Only the newest handoff is ever live.

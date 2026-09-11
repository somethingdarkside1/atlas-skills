# Notes

Dated, write-once files. A note records what was true on a date: a handoff, a prototype verdict, research findings, a review. Never edit a note after the day it was written. Anything that stays true gets copied into the glossary, the map, the plan, or a decision.

File name: `YYYY-MM-DD-<kind>-<slug>.md`. Only `/atlas` reads notes, and only the newest handoff.

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

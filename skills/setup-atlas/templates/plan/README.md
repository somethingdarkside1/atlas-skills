# Plan

One folder per part holds `brief.md` and numbered tasks.

```
plan/
  <part>/
    brief.md
    01-<slug>.md
    02-<slug>.md
```

## Ids and statuses

A task id is `<part>/<NN>`. Skills print and accept it in that shape everywhere: as an argument, on the `Next:` line, and in commit messages. Inside its own part, `blocked_by` may shorten it to `NN`.

| Status | Meaning | Set by |
|---|---|---|
| todo | Not started | `/plan-it` |
| doing | Being made, or sent back with findings or a question | `/build-it`, and `/review-it` on findings |
| review | Delivered; waiting for `/review-it`, or for you to tick the `(you)` boxes | `/build-it` |
| done | Reviewed clean | `/review-it` |
| canceled | Dropped by a re-plan; the file stays, with the reason | `/plan-it` |

A task is ready when it is todo and every task in its `blocked_by` list is done. A blocker may only name a task that exists and is not canceled. A part has a plan when it has at least one task that is not canceled. Task numbers are never reused or reordered; a re-plan edits or adds todo tasks, and cancels a task instead of deleting it. Part folders stay flat and are named by the part id, which is unique across the whole map.

**Which task is next.** The first part in map order with status building and a ready task. Else the first decided or done part with one. Then the lowest number in that part. `/build-it` and `/atlas` both use this rule.

## Brief

```md
---
part: wordmark
---

# Wordmark

## Problem
The studio name is set in a default font on every surface, so nothing looks like it belongs to the studio.

## Outcome
One wordmark that reads as the studio's own at every size from a favicon to a shopfront.

## Decisions
[0001](../../decisions/0001-one-mark-not-a-family.md): one mark, not a family.
Lowercase only; the name never appears in capitals.

## Out of scope
A symbol or icon. Colour beyond black and white.
```

The brief is written by `/interview-me`. While the interview is still running, the first line under the title reads `Draft: open questions remain on the map.`; the line goes when the part is decided. Decisions holds a link per decision file and one line per settled choice too small for a file.

## Task

```md
---
status: todo
blocked_by: [01, palette/02]
---

# 02: Build the lockups

## Delivers
The wordmark in horizontal and stacked lockups, each with clear-space rules, as SVG.

## Check by
Open `brand/wordmark/lockups.html` and check every lockup at 16, 64, and 400 pixels.

## Done when
- [ ] Horizontal and stacked lockups exist as SVG
- [ ] Clear space is defined as a multiple of the x-height
- [ ] (you) Both read cleanly at 16 pixels

## Delivered

## Review
```

Delivered and Review start empty. `/build-it` adds one dated entry per delivery (or per stop) under Delivered: what was made, where it lives, what was verified. `/review-it` adds one dated pass per run under Review: findings under each check (brief, conventions) with what they cite, or "clean".

`status` is one of the five in the table. `blocked_by` lists task numbers in this part, or `<part>/<NN>` for another part. A Done when box starts with `(you)` when only a person can look: `/build-it` leaves it unticked, you tick it yourself, and `/review-it` treats a ticked `(you)` box as confirmed. A canceled task carries one line under its title: `Canceled: <date>, <why>`. Keep the headings exactly as shown, in this order.

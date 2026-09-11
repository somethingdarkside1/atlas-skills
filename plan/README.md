# Plan

Tracker: files
Merge: review-it

The two lines above are set once by `/atlas` and read by `/plan-it`, `/build-it`, and `/review-it`.

**Tracker** is `files` or `github owner/name`. With `files`, one folder per part below holds `brief.md` and numbered tasks. With `github`, the brief is a parent issue labelled `atlas:part`, each task is a sub-issue labelled `atlas:task`, blockers are native dependencies, status is the issue state plus the Project's Status field, `build-it` assigns itself when it starts, Delivered and Review go in as comments, and `review-it` closes the parent when every task under it is done. Tasks join a milestone only when you name one.

**Merge** is `review-it` or `human`. On a git project `build-it` works on a branch named `<part>/<NN>-<slug>` and, with a GitHub tracker, opens a PR that closes the task. A clean review then merges with squash (`review-it`) or leaves the PR marked ready for a person (`human`). A task is done only once merged. Without git, `build-it` records where the result lives under Delivered and that is the whole trail.

Nothing else in the project changes between these settings.

```
plan/
  <part>/
    brief.md
    01-<slug>.md
    02-<slug>.md
```

A task is ready when every task in its `blocked_by` list is done. `/build-it` picks the lowest-numbered ready task. Part folders stay flat and are named by the part id, which is unique across the whole map.

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

## Out of scope
A symbol or icon. Colour beyond black and white.
```

## Task

```md
---
status: todo
blocked_by: [01, palette/02]
---

# 02: Build the lockups

## Delivers
The wordmark in horizontal and stacked lockups, each with clear-space rules, as SVG.

## Verify by
Open `brand/wordmark/lockups.html` and check every lockup at 16, 64, and 400 pixels.

## Acceptance
- [ ] Horizontal and stacked lockups exist as SVG
- [ ] Clear space is defined as a multiple of the x-height
- [ ] Both read cleanly at 16 pixels

## Delivered
Filled in by /build-it: what was made, where it lives, what was verified.

## Review
Filled in by /review-it: findings on each axis, or "clean".
```

`status` is `todo`, `doing`, or `done`. `blocked_by` lists task numbers in this part, or `<part>/<NN>` for another part. Keep the headings exactly as shown, in this order.

# Plan

Tracker: files
Merge: review-it

The two lines above are set once by `/atlas` and read by `/plan-it`, `/build-it`, and `/review-it`.

**Tracker** is `files` or `github owner/name`. With `files`, one folder per part below holds `brief.md` and numbered tasks. With `github`, the brief is a parent issue labelled `atlas:part`, each task is a sub-issue labelled `atlas:task`, blockers are native dependencies, status is the issue alone (todo is open and unassigned, doing is open and assigned, done is closed), the task id is the issue number, `build-it` assigns itself when it starts, Delivered and Review go in as comments, and `review-it` closes the parent when every task under it is done. Tasks join a milestone only when you name one.

**Merge** is `review-it` or `human` and matters only with a `github` tracker. There `build-it` works on a branch named `<part>/<NN>-<slug>` and opens a PR that closes the task; a clean review then merges with squash (`review-it`) or leaves the PR marked ready for a person (`human`), and a task is done only once merged. With `files`, `build-it` works in place on whatever is checked out, commits when the folder is a git repo, and Delivered says where the result lives.

Nothing else in the project changes between these settings.

```
plan/
  <part>/
    brief.md
    01-<slug>.md
    02-<slug>.md
```

A task is ready when every task in its `blocked_by` list is done, and a blocker may only name a task that exists. `/build-it` picks the lowest-numbered ready task or the highest-impact blocker. Task numbers are never reused or reordered; a re-plan edits, removes, or adds todo tasks only. Part folders stay flat and are named by the part id, which is unique across the whole map.

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

The brief is written by `/interview-me` when the part is decided. Decisions holds a link per decision file and one line per settled choice too small for a file.

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
- [ ] Both read cleanly at 16 pixels

## Delivered
Filled in by /build-it: what was made, where it lives, what was verified.

## Review
Filled in by /review-it: one dated pass per run, findings under each check (brief, conventions) with what they cite, or "clean".
```

`status` is `todo`, `doing`, or `done`. `blocked_by` lists task numbers in this part, or `<part>/<NN>` for another part. A Check by line starts with `(you)` when only a person can look. Keep the headings exactly as shown, in this order.

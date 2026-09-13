# Plan

Tracker: files
Merge: review-it

The two lines above are set once by `/atlas` and read by `/plan-it`, `/build-it`, and `/review-it`.

**Tracker** is `files` or `github owner/name`. With `files`, one folder per part below holds `brief.md` and numbered tasks. With `github`, the brief is a parent issue labelled `atlas:part`, each task is a sub-issue labelled `atlas:task`, blockers are native dependencies, Delivered and Review go in as issue comments, and the issue's state is the task's status (table below). `/review-it` closes the parent issue when its last task is done; under `Merge: human`, `/atlas` does. Tasks join a milestone only when you name one.

**Merge** is `review-it` or `human` and is read only with a `github` tracker. A clean review squash-merges the task's PR (`review-it`) or marks it ready and leaves it for a person (`human`), whose merge closes the issue. With `files` the line is ignored.

Nothing else in the project changes between these settings.

## Ids and statuses

A task id is `<part>/<NN>` with `files` and the issue number with `github`. Skills print and accept the id in that shape everywhere: as an argument, on the `Next:` line, and in commit messages. Inside its own part, `blocked_by` may shorten `<part>/<NN>` to `NN`.

| Status | Meaning | With `files` | With `github` |
|---|---|---|---|
| todo | Not started | `status: todo` | open, unassigned |
| doing | `/build-it` is on it, or sent a question back to the map | `status: doing` | open, assigned, no open PR |
| review | Delivered; waiting for `/review-it` or for your `(you)` boxes | `status: review` | open, assigned, PR open |
| done | Reviewed clean and, with `github`, merged | `status: done` | closed |

A task is ready when it is todo and every task in its `blocked_by` list is done. A blocker may only name a task that exists. A part has a plan when it has at least one task. Task numbers are never reused or reordered; a re-plan edits, removes, or adds todo tasks only. Part folders stay flat and are named by the part id, which is unique across the whole map.

**Which task is next.** The first part in map order with status building and a ready task; else the first decided part with one; then the lowest number in that part. `/build-it` and `/atlas` both use this rule.

## Git

Three environments. Every difference between them is written here and nowhere else.

- **No repo.** Skills write files and commit nothing. `/atlas` offers `git init` and reports `no repo` on every run until there is one.
- **A repo.** Every skill commits what it wrote, on the branch that is checked out, with the message `<skill> <id>: <what>` (for example `plan wordmark: 4 tasks`, `build wordmark/02: the lockups`). When a hook rejects the commit, the skill prints the hook's one line and stops. Skills push nothing except the branch a PR needs; you push. `/park-it` is the one exception to "what it wrote": it commits everything under the five things and `prototypes/`.
- **A repo with a `github` tracker.** `/build-it` needs a clean tree, branches from the default branch as `<part>/<NN>-<slug>` (NN the issue number), commits and pushes there, opens a PR whose body is `Closes #<NN>`, then checks the default branch out again. `/review-it` reviews the PR; clean under `Merge: review-it` it squash-merges, deletes the branch, and pulls the default branch; under `Merge: human` it marks the PR ready and stops. Every other skill commits on the branch that is checked out, which is the default branch once `/build-it` has returned to it.

Run one Atlas session per checkout at a time. Parallel work is what the `github` tracker and its branches are for.

```
plan/
  <part>/
    brief.md
    01-<slug>.md
    02-<slug>.md
```

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
- [ ] (you) Both read cleanly at 16 pixels

## Delivered
Filled in by /build-it: what was made, where it lives, what was verified.

## Review
Filled in by /review-it: one dated pass per run, findings under each check (brief, conventions) with what they cite, or "clean".
```

`status` is one of the four in the table. `blocked_by` lists task numbers in this part, or `<part>/<NN>` for another part. A Done when box starts with `(you)` when only a person can look: `/build-it` leaves it unticked, you tick it yourself, and `/review-it` treats a ticked `(you)` box as confirmed. Keep the headings exactly as shown, in this order.

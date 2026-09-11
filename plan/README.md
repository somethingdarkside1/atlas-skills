# Plan

Tracker: files

The line above is set once by `/atlas` and read by `/plan-it`, `/build-it`, and `/review-it`. `files` means one folder per part below, holding `brief.md` and numbered tasks. `github owner/name` means the brief is a parent issue labelled `atlas:part`, each task is a sub-issue labelled `atlas:task`, blockers are native dependencies, and status is the issue state plus the Project's Status field. Nothing else in the project changes between the two.

```
plan/
  <part>/
    brief.md
    01-<slug>.md
    02-<slug>.md
```

A task is ready when every task it lists under **Blocked by** is done. `/build` picks from ready tasks, lowest number first. Part folders stay flat and are named by the part id, which is unique across the whole map.

## Brief template

```md
# <Part name>

## Problem
What is wrong or missing, from the point of view of the person affected.

## Outcome
What is true once this part is done, in their words.

## Decisions
Choices already made, each linking its file in decisions/. No file paths, no snippets.

## Out of scope
What this part deliberately leaves alone.
```

## Task template

```md
# 01: <Imperative title: what to make, starting with a verb>

**Delivers:** the complete slice this task makes true, from the user's point of view.
**Blocked by:** none, or the tasks that gate this one: `02` in this part, `<part>/02` in another.
**Status:** todo | doing | done

- [ ] Acceptance criterion, each one checkable by looking, running, or asking
- [ ] Acceptance criterion

**Verify by:** the command, URL, or look that shows this task is done.

## Delivered
Filled in by /build: what was made, where it lives, what was verified.

## Review
Filled in by /review: findings on each axis, or "clean".
```

# Plan

One folder per part of the map. Each folder holds `brief.md` and numbered task files.

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
# 01: <Task title>

**Delivers:** the complete slice this task makes true, from the user's point of view.
**Blocked by:** none, or the tasks that gate this one: `02` in this part, `<part>/02` in another.
**Status:** todo | doing | done
**Issue:** empty until /publish fills it in with the GitHub issue number. When set, /build reads that issue's comments before starting.

- [ ] Acceptance criterion
- [ ] Acceptance criterion

## Delivered
Filled in by /build: what was made, where it lives, what was verified.

## Review
Filled in by /review: findings on each axis, or "clean".
```

## GitHub mirror

Filled in by `/publish` the first time it runs. Everything else in this folder works without it.

```md
Repo: owner/name
Project: the Project number, or none
```

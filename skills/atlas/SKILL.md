---
name: atlas
description: Print where the project stands in five lines and name the next command; changes nothing.
disable-model-invocation: true
---

# Atlas

Say where things stand and what to run next. Change nothing.

## Read first
- Which of `GLOSSARY.md`, `MAP.md`, `plan/README.md`, `decisions/README.md`, and `notes/README.md` exist.
- Parts: `grep -E '^## |^\*\*Status:\*\*|^Needs:|^Open questions:' MAP.md`, and the same for each file in `map/` when that folder exists. Then the mermaid diagram block in each of those files, to compare with the sections.
- Tasks: `grep -rH -E '^(status|blocked_by):' plan --include='[0-9]*.md'`, and the Ids and statuses section of `plan/README.md`. For a task in doing or review, also its Done when boxes and its Delivered and Review sections.
- Handoffs: `ls notes | grep -- '-handoff-' | tail -1` (names sort by date and time), then that file, whole. The rule for a live handoff is in `notes/README.md`.
- Decisions: `grep -rH '^part:' decisions --include='[0-9]*.md'`.
- The `## Atlas (atlas: N)` block and the `## Saving work` section in `CLAUDE.md` or `AGENTS.md`; `git status --short`, in a repo.

## Steps
1. A home is missing: print which, then `Next: /setup-atlas`, and stop. Done when every missing home is named.
2. Print five lines.
   One: parts by status, in this shape: `<n> sketched, <n> decided, <n> building (<ids>), <n> done`.
   Two: ready tasks by id, by the rule in `plan/README.md`, or `none`.
   Three: the newest handoff as `date slug`, followed by `live` when it is, or `none`.
   Four: problems, one per line, each with the command or the person that fixes it, or `none`: a diagram node, class, or `Needs:` id that disagrees with the sections (`/map-it`); a part that reads building while every one of its tasks is done or canceled, with at least one done, or a split part whose status disagrees with its sub-parts (`/map-it`); a blocker naming a task that does not exist or is canceled (`/plan-it <part>`); a task in doing with nothing under Delivered (`/build-it <id>`); a task in review that is waiting on you, meaning its newest pass has no findings, lists `For you to check:`, and a `(you)` box is still unticked (you: tick the boxes, or tell `/review-it <id>` what is wrong); a decision whose `part:` is not on the map (you); uncommitted changes in the five things (you: save them as `Saving work` says); no Atlas block in the project instructions, one older than `atlas: 2`, or no `Saving work` section (`/setup-atlas`); a `Tracker: github` line in `plan/README.md`, which this version does not read (you: tasks live in `plan/`).
   Five: `Next: /command <id>`, the first that applies. A task in review that is not waiting on you: `/review-it <id>`. A decided or building part with an open question: marked `(prototype)`, `/prototype-it <part>`; with no marker or marked `(answered ...)`, `/interview-me <part>`; a `(later: ...)` question never routes. A sketched part with a `(prototype)` question: `/prototype-it <part>`. A sketched part with an `(answered ...)` question: `/interview-me <part>`. A live handoff: its `Next:` line, with the note's date beside it. A task in doing: `/build-it <id>`. A ready task: `/build-it <id>`. A decided or building part with no plan: `/plan-it <part>`. The first sketched part in map order none of whose `Needs:` is still sketched: `/interview-me <part>`. An empty map: `/interview-me`. Every part done, or nothing left but your checks: `Next: nothing to run`, with the reason. Otherwise `/map-it`.
   Done when five lines are printed and the last starts with `Next:`.

## Output
- Five lines in the terminal. No file changes.

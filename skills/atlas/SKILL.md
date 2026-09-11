---
name: atlas
description: Print where the project stands in five lines and name the next command; on a fresh folder, create the five things.
disable-model-invocation: true
---

# Atlas

Say where things stand and what to run next; on a fresh folder, create the five things.

## Read first
- Whether `MAP.md`, `GLOSSARY.md`, `plan/README.md`, `decisions/README.md`, and `notes/README.md` exist.
- `grep -E '^## |^\*\*Status:\*\*|^Needs:|^Plan:' MAP.md map/*.md`.
- `grep -E '^(Tracker|Merge):' plan/README.md`; task state: `grep -H -E '^(status|blocked_by):' plan/*/*.md`, or `gh issue list --label atlas:task --state all --json number,state,assignees`, and open PRs.
- `ls notes/` for the newest note by date; read it only when its name says handoff.
- `grep -h '^part:' decisions/*.md`.
- The `## Atlas (atlas: N)` block in `CLAUDE.md` and `AGENTS.md`; `git rev-parse --is-inside-work-tree`; `git remote -v`; `git status --short`.

## Steps
1. Fresh folder (no `MAP.md`): create. Copy the templates in `templates/` beside this file to the root; when a `CONTEXT.md` exists, move its entries into `GLOSSARY.md` and delete it. Fill the map's name and paragraph from the README, or ask `What is this, in a sentence?` when there is none. Offer `git init` when there is no repo. Ask the tracker question only when a GitHub remote exists (`files` or `github owner/name`) and write the answer on the `Tracker:` line. Set `Merge: human` when `git shortlog -s` shows more than one author, else `review-it`. Append `templates/CLAUDE-block.md` to `CLAUDE.md` and to `AGENTS.md` where each exists; create both when neither does. Commit as `atlas: create the five things` when the folder is a git repo. Done when the five things exist and the block is in place; continue at step 3.
2. Every later run: never re-create, never re-ask. When the block's `atlas:` number is lower than the one in `templates/CLAUDE-block.md`, replace the block. Done when the block is current.
3. Repair, and name each repair on line four: a split part's status from its sub-parts (done when all are done, building when any is building, decided when all are at least decided, else sketched); a part whose tasks are all done and merged but whose status is not done, moved to done with its node class and its parent issue closed. Commit repairs as `atlas: repairs`. Done when the map agrees with the plan.
4. Print five lines. One: parts by status, naming the building ones. Two: ready tasks by id (todo with every blocker done), or `none`. Three: the newest note as `date kind title`, or `none`. Four: problems, one per line with the command that fixes each, or `none`: a diagram node, class, or `Needs:` id that disagrees with the sections (`/map-it`); a blocker naming a task that does not exist (`/plan-it <part>`); a decision whose `part:` is not on the map; uncommitted changes in the five things (`/park-it`); no git repo (`no repo`); open PRs under `Merge: human`. Five: `Next: /command <id>`, the first that applies: the newest note is a handoff, its `Next:` line with the note's date beside it; a task awaiting review, `/review-it <id>`; a ready task, `/build-it <id>`; a decided part without a plan, `/plan-it <part>`; a part carrying an `(answered ...)` open question, `/interview-me <part>`; a `(prototype)` question, `/prototype-it "<question>"`; a sketched part, `/interview-me <part>`; an empty map, `/interview-me`; otherwise `/map-it`. Done when five lines are printed and the last starts with `Next:`.
5. With the argument `go`: after the five lines, run the next command yourself when it is `/build-it` or `/review-it`, then run `/atlas go` again. Stop at any other command, and stop when a task has three review passes with findings, saying which. Done when the loop stops on a human's turn.

## Output
- On a fresh folder: the five things, the block in `CLAUDE.md` and `AGENTS.md`, one commit.
- Five lines in the terminal; on later runs, repairs to `MAP.md` and their commit when any were made.

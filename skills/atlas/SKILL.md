---
name: atlas
description: Print where the project stands in five lines and name the next command; on a fresh folder, create the five things.
disable-model-invocation: true
---

# Atlas

Say where things stand and what to run next; on a fresh folder, create the five things.

## Read first
- Whether `MAP.md` exists, then the format comment at the top of it.
- `grep -E '^## |^\*\*Status:\*\*|^Needs:|^Open questions:|^- ' MAP.md map/*.md` for parts, statuses, needs, and open questions.
- `plan/README.md`: the `Tracker:` and `Merge:` lines, the Ids and statuses section, and the Git section. Task state: `grep -H -E '^(status|blocked_by):' plan/*/*.md`, or `gh issue list --label atlas:task --state all --json number,state,assignees` with the open PRs.
- `ls notes/` for the newest note by filename; open it only when its kind is handoff.
- `grep -h '^part:' decisions/*.md`.
- The `## Atlas (atlas: N)` block in `CLAUDE.md` and `AGENTS.md`; `git rev-parse --is-inside-work-tree`; `git remote -v`; `git status --short`; `git log -1 --format=%cs -- GLOSSARY.md MAP.md map plan decisions notes`.

## Steps
1. Fresh folder (no `MAP.md`): create. Copy the templates in `templates/` beside this file to the root; when a `CONTEXT.md` exists, move its entries into `GLOSSARY.md` and delete it. Fill the map's name and paragraph from the README, or ask `What is this, in a sentence?` when there is none; `/interview-me` rewrites both later. Offer `git init` when there is no repo. When a GitHub remote exists, ask one round in the interview shape with two questions: the tracker (`files` or `github owner/name`) and, for `github`, the merge (`review-it`, or `human`, recommended when `git shortlog -s` shows more than one author); write the answers on the `Tracker:` and `Merge:` lines. Without a remote, the template's lines stand. Append `templates/CLAUDE-block.md` to `CLAUDE.md` and to `AGENTS.md` where each exists; create both when neither does. Commit as `plan/README.md` says: the five things and the two blocks; message `atlas: create the five things`. Done when the five things exist and the block is in place; continue at step 3.
2. Every later run: keep what exists and ask nothing. When the block's `atlas:` number is lower than the one in `templates/CLAUDE-block.md`, replace the block. Done when the block is current.
3. Repair, and name each repair on line four: a split part's status from its sub-parts, by the rule in the map's format comment; a part whose tasks are all done (and merged, with `github`) but whose status is not done, moved to done with its node class, its parent issue closed. Commit as `plan/README.md` says: `MAP.md` and `map/`; message `atlas: repairs`. Done when the map agrees with the plan.
4. Print five lines.
   One: parts by status, naming the building ones.
   Two: ready tasks by id, or `none`.
   Three: the newest note as `date kind slug` from its filename, followed by `live` when it is a handoff that is live by the rule in `notes/README.md`, or `none`.
   Four: problems, one per line, each with the command or the person that fixes it, or `none`: a diagram node, class, or `Needs:` id that disagrees with the sections (`/map-it`); a blocker naming a task that does not exist (`/plan-it <part>`); a decision whose `part:` is not on the map (you); uncommitted changes in the five things (`/park-it`); no repo (`git init`); an open PR under `Merge: human` (you).
   Five: the first that applies. A live handoff: its `Next:` line, with the note's date on the reason line. A task in review: `/review-it <id>`. A building or decided part with an open question: `/interview-me <part>`. A ready task: `/build-it <id>`, by the rule in `plan/README.md`. A decided part with no task: `/plan-it <part>`. A `(prototype)` question: `/prototype-it "<question>"`. The first sketched part in map order whose `Needs:` are all decided: `/interview-me <part>`. An empty map: `/interview-me`. Otherwise `/map-it`.
   Done when five lines are printed and the last starts with `Next:`.
5. With the argument `go`: after the five lines, when the next command is `/build-it` or `/review-it`, open the `SKILL.md` in the sibling folder of that name beside this one, follow its steps with that id, then start again at step 2. Stop at any other command, at a task with three passes carrying findings, and at a review that lists `For you to check:`, saying which on the reason line. Done when the loop ends on a `Next:` line only a person can act on.

## Output
- On a fresh folder: the five things, the block in `CLAUDE.md` and `AGENTS.md`, one commit.
- Five lines in the terminal; on later runs, repairs to `MAP.md` and their commit when any were made.

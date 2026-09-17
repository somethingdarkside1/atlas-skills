---
name: plan-it
description: Turn a decided part's brief into numbered tasks with blocking edges, each sized to one session, after one sizing round with the human; or add one task under an existing brief.
disable-model-invocation: true
---

# Plan it

Cut a decided part into tasks a session can finish and a person can check.

## Read first
- The Ids and statuses section and the task template in `plan/README.md`.
- `MAP.md`: the part's section (its status and `Needs:`).
- The brief, `plan/<part>/brief.md`, and the decisions it links.
- The newest handoff in `notes/`, when its `Target:` is this part: it holds a sizing round in flight.
- Every task's state, in this part and the others, because blockers cross parts: `grep -rH -E '^(status|blocked_by):' plan --include='[0-9]*.md'`. Then the whole file of every task you will change.

## Steps
1. If a home is missing, print `Next: /setup-atlas` and stop. No argument: the one decided part that has a brief and no plan, else ask which. A sketched part, or a brief that still carries its `Draft:` line: print `Interview it first.` and `Next: /interview-me <part>`, and stop. Done when the part and its brief are open.
2. One task only, when a second argument in quotes says what to make (`/plan-it <part> "<what to make>"`): draft that single task under the existing brief, show it, and ask `Write it? (yes)`. When it falls outside the brief's Outcome or inside its Out of scope, say so, print `Next: /interview-me <part>`, and stop. Then go to step 6. Done when the human has said yes.
3. Draft the tasks. Each passes three tests: one Delivers line and one Check by line a person could run alone; finishable in one sitting without waiting for an answer; nothing it delivers is half of something another task finishes. When in doubt, split. When the part has layers, the first task runs thinly through all of them; otherwise the first task is the one everything else waits on. Number in dependency order from the next free number, counting canceled tasks; never reuse or reorder a number. `blocked_by` names only tasks that exist and are not canceled, in this part or another (`<part>/<NN>`); when the brief depends on a part with no plan yet, carry that to the sizing round. A Done when box starts with `(you)` when only a person can look. Done when every task has Delivers, Check by, Done when boxes, and blockers that exist.
4. Re-plan, when tasks already exist: leave done and review tasks untouched, and edit or add todo tasks. A doing task changes only when you have asked and the human has said yes in this run, because the brief moved under it: edit it and it stays doing, or cancel it. Drop a task by canceling it, never by deleting it: set `status: canceled`, write `Canceled: <date>, <why>` under its title, and fix every blocker that named it in this run, in this part or another. When a task in doing, review, or done names the task you would cancel, change nothing, say which, and print `Next: /plan-it <part>` for when the human has decided. Done when no blocker points at a canceled task.
5. Run one sizing round in the interview format: the numbered list (title, blocked by, delivers), then questions on merge, split, order, what is missing, and any wait on an unplanned part, each with lettered options of one line and a `➡️`. Wait for the answers and apply them. Done when the human has answered and the list reflects it.
6. Write each new task as `plan/<part>/NN-<slug>.md` from the template, headings exactly as shown and in order, `status: todo`, with nothing under Delivered and Review. Edit an existing task in place, keeping its status, Delivered, and Review. Then check the whole graph: every blocker exists and is not canceled, no task blocks itself, and no chain of blockers comes back to where it started. Done when every task is on disk and the check is clean.
7. Save as the project's `Saving work` section says: the task files you wrote or fixed, in this part or another, and nothing else; message `plan <part>: <n> tasks`. Done when they are saved, or you have said why they are not.
8. Print the last line: `Next: /build-it <id>` for a task of this part in doing, else its lowest-numbered ready task; when there is neither, `Next: /atlas`.

## Output
- `plan/<part>/NN-<slug>.md` files; canceled tasks kept with their reason.
- One save, as the project says.

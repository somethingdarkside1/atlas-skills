---
name: plan-it
description: Turn a decided part's brief into numbered tasks with blocking edges, each sized to one session, after one sizing round with the human.
disable-model-invocation: true
---

# Plan it

Cut a decided part into tasks a session can finish and a person can check.

## Read first
- `grep -E '^(Tracker|Merge):' plan/README.md`, and the task template in `plan/README.md`.
- `MAP.md`: the part's section (its status, `Needs:`, and `Plan:`).
- The brief: `plan/<part>/brief.md`, or the parent issue (`gh issue view <n>`), and the decisions it links.
- The part's existing tasks, frontmatter only: `grep -H -E '^(status|blocked_by):' plan/<part>/*.md`, or the parent's sub-issues with their state and blockers.

## Steps
1. If `MAP.md` or `plan/README.md` is missing, print `Run /atlas first.` and stop. No argument: the one decided part with no `Plan:` yet, else ask which. A sketched part: print `Interview it first: /interview-me <part>` and stop. Done when the part and its brief are open.
2. Draft the tasks. Each passes three tests: one Delivers line and one Check by line a person could run alone; finishable in one sitting without waiting for an answer; nothing it delivers is half of something another task finishes. When in doubt, split. When the part has layers, the first task runs thinly through all of them; otherwise the first task is the one everything else waits on. Number in dependency order from the next free number; never reuse or reorder a number. `blocked_by` names only tasks that exist, in this part or another (`<part>/<NN>`); when the brief depends on a part with no plan yet, carry that to the sizing round. A Check by line starts with `(you)` when only a person can look. Done when every task has Delivers, Check by, Done when boxes, and blockers that exist.
3. Re-plan, when tasks already exist: leave done and doing tasks untouched; edit, remove, or add todo tasks only; delete a removed task's file (files) or close it with one comment (GitHub), and fix every blocker that named it in this run. Done when no blocker points at a removed task.
4. Run one sizing round in the interview format: the numbered list (title, blocked by, delivers), then questions on merge, split, order, what is missing, and any wait on an unplanned part, each with lettered options, costs, and a `➡️`. Wait for the answers and apply them. Done when the human has answered and the list reflects it.
5. Write. `Tracker: files`: `plan/<part>/NN-<slug>.md` from the template, headings exactly as shown and in order, `status: todo`. `Tracker: github`: one sub-issue per task under the parent, title without a number, label `atlas:task`, body holding Delivers, Check by, and Done when; then add the blocked-by dependencies with the native API once every issue has a number. Done when every task exists where the tracker says.
6. Commit when the folder is a git repo: only `plan/<part>/`; message `plan <part>: <n> tasks`; on a rejected hook, print its one line and stop. Done when `git status` shows none of them.
7. Print `Next: /build-it <lowest-numbered ready task>` as the last line.

## Output
- `plan/<part>/NN-<slug>.md` files, or sub-issues with dependencies.
- One commit, when the folder is a git repo.

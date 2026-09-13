---
name: build-it
description: Work one ready task in whatever medium it names, verify it, and record what was delivered on the task.
disable-model-invocation: true
---

# Build it

Do one task, prove it, write down what you made.

## Read first
- `plan/README.md`: the `Tracker:` and `Merge:` lines, the Ids and statuses section, and the Git section.
- Ready tasks: files, `grep -H -E '^(status|blocked_by):' plan/*/*.md`; GitHub, open unassigned `atlas:task` issues with no open blockers.
- The task, whole; its part's brief; the decisions the brief links; the format comment at the top of `MAP.md` and the part's section.
- The format comments of `GLOSSARY.md` and `decisions/README.md`, for anything the work needs to write there.
- Existing things of the kind Delivers names, for how this project makes them.

## Steps
1. If `MAP.md` is missing, print `Run /atlas first.` and `Next: /atlas`, and stop. Pick the task: the argument, else the next task by the rule in `plan/README.md`. No ready task: print `Nothing ready.` and `Next: /atlas`, and stop. Done when one task is open.
2. Mark it. Files: `status: doing`. GitHub: assign yourself. When the part reads decided, set its status line to `building` and its node class to `:::building`. Done when the task reads doing and the part reads building.
3. `Tracker: github` only: branch as the Git section says (clean tree, from the default branch, `<part>/<NN>-<slug>`). A dirty tree: print `Commit or stash your changes first.` and `Next: /build-it <id>`, and stop. Done when the branch is checked out.
4. Make what Delivers names, the way this project already makes that kind of thing, in the glossary's words. For code, run the project's own checks when they exist. A choice that passes the three tests in `decisions/README.md` becomes a decision file; a term the task needed becomes a glossary entry. Leave the brief, the other tasks, and the rest of the map as they are. When the brief is wrong or silent on something you need, write the question on the part's open questions in the map's shape, leave the task doing, print `The brief needs an answer: <question>` and `Next: /interview-me <part>`, and stop. Done when the thing exists where Delivers says.
5. Run Check by yourself when you can, and tick every Done when box you verified; `(you)` boxes stay for the human. Done when every box you could check is ticked.
6. Write Delivered: what was made, where it lives, how it was verified, which boxes you could not check and why, and any decision or term you wrote. GitHub: Delivered is a comment on the issue, and ticks are edits to the issue body. Files: set `status: review`. Done when Delivered reads as claims a reviewer can check and the task reads review.
7. Commit as `plan/README.md` says: the files you made, the task file, `MAP.md`, and any decision or glossary entry you wrote; message `build <id>: <what was made>`. GitHub: push, open the PR as the Git section says, and check the default branch out again. Done when `git status` shows none of your files and, on GitHub, the PR exists and the default branch is checked out.
8. Print `Next: /review-it <id>` as the last line.

## Output
- The delivered thing, where Delivered says.
- The task: status review, boxes ticked, Delivered filled (file or issue comment and PR).
- `MAP.md`: the part's status building, and an open question when the brief needed one.
- Decisions or glossary entries the work needed.
- One commit; on GitHub, a branch and a PR.

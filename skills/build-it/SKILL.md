---
name: build-it
description: Work one ready task in whatever medium it names, verify it, and record what was delivered on the task.
disable-model-invocation: true
---

# Build it

Do one task, prove it, write down what you made.

## Read first
- `grep -E '^(Tracker|Merge):' plan/README.md`.
- Ready tasks: files, `grep -H -E '^(status|blocked_by):' plan/*/*.md`, a task being ready when it is todo and every blocker is done; GitHub, open unassigned `atlas:task` issues with no open blockers.
- The task, whole; its part's brief; the decisions the brief links; the part's status line in `MAP.md`.
- Existing files of the kind Delivers names, for how this project makes them.

## Steps
1. If `MAP.md` or `plan/README.md` is missing, print `Run /atlas first.` and stop. Pick the task: the argument; else the first part in map order with status building and a ready task, else the first decided part with one, then the lowest number in it. No ready task: print `Nothing ready. Next: /atlas` and stop. Done when one task is open.
2. Mark it. Files: `status: doing`. GitHub: assign yourself. When the part reads decided, set its status line to `building` and its node class to `:::building`. Done when the task reads doing and the part reads building.
3. `Tracker: github` only: require a clean tree (else print `Commit or stash your changes first.` and stop), fetch, and branch from the default branch as `<part>/<NN>-<slug>` with NN the issue number. Done when the branch is checked out.
4. Make what Delivers names, the way this project already makes that kind of thing, in the glossary's words. For code, run the project's own checks when they exist. A choice that passes the three tests in `decisions/README.md` becomes a decision file; a term the task needed becomes a glossary entry. Never edit the brief, another task, or the map beyond step 2; when the brief is wrong, print `The brief is wrong: <why>. Next: /interview-me <part>` and stop. Done when the thing exists where Delivers says.
5. Run Check by yourself when you can, and tick every Done when box you verified; leave `(you)` boxes unticked. Done when every box you could check is ticked.
6. Write Delivered: what was made, where it lives, how it was verified, which boxes you could not check and why, and any decision or term you wrote. When you cannot finish without an answer, add an `Open question:` line, leave the task doing, and end with `Next: /build-it <id>`. GitHub: Delivered is a comment on the issue, and ticks are edits to the issue body. Done when Delivered reads as claims a reviewer can check.
7. Commit when the folder is a git repo: the files you made and the task file; message `build <id>: <what was made>`; on a rejected hook, print its one line and stop. GitHub: push, then open a PR whose body is `Closes #<NN>` and a link to the Delivered comment. Done when `git status` shows none of your files and, on GitHub, the PR exists.
8. Print `Next: /review-it <id>` as the last line.

## Output
- The delivered thing, where Delivered says.
- The task: status doing, boxes ticked, Delivered filled (file or issue comment).
- `MAP.md`: the part's status building.
- Decisions or glossary entries the work needed.
- One commit; on GitHub, a branch and a PR.

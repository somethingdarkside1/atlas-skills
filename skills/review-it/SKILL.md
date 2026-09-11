---
name: review-it
description: Check a task's result against its brief and the project's conventions, record findings on the task, and close or merge when clean.
disable-model-invocation: true
---

# Review it

Check what was delivered against what was asked and how this project does things, then close the loop.

## Read first
- `grep -E '^(Tracker|Merge):' plan/README.md`.
- Tasks awaiting review: doing tasks whose Delivered is newer than their last Review pass (files), or assigned open `atlas:task` issues with a Delivered comment after the last review comment (GitHub).
- The task, its part's brief, the decisions the brief links, `GLOSSARY.md`, and existing files of the same kind as the delivered thing.

## Steps
1. If `MAP.md` or `plan/README.md` is missing, print `Run /atlas first.` and stop. Pick the task: the argument, else the one awaiting review, else ask. Done when one task is open.
2. Review in a fresh context when the harness can give you one: hand a sub-agent the task id and this rule, "read the brief, the decisions, the glossary, Delivered, and the delivered thing; nothing else". Otherwise review inline and say so in the pass. Done when the reviewer has only those inputs.
3. Check one, the brief: open what Delivered points at, re-run Check by when you can, and test each Done when box against the brief's Outcome and Out of scope. Check two, the conventions: the glossary's words are used and none from an Avoid list; no accepted decision is contradicted; the thing is made the way existing things of that kind are made here (structure, naming, tone, style, and for code the project's documented standards). Done when every box is verified, marked `(you)`, or a finding.
4. List the `(you)` boxes under `For you to check:` with what to look at, and wait for the human's word; record `confirmed by you` on each. Done when no box is unaccounted for.
5. Write the Review pass: dated, one heading per check, each finding one sentence with one citation (the brief line or the glossary entry), or `clean`. Files: append it to the task's Review section. GitHub: one comment on the issue; on the PR, approve when clean, else request changes with a link to the comment. Done when the pass is on the task.
6. With findings: the task stays doing. Done when the builder can act on every finding without asking.
7. Clean, `Tracker: files`: set `status: done`. Clean, `Tracker: github`, `Merge: review-it`: squash merge the PR and delete the branch; a conflict with the default branch is one line and a stop. `Merge: human`: mark the PR ready and leave it. When every task of the part is done and merged, set the part's status line and node class to `done` and close the parent issue; under `Merge: human`, leave that to `/atlas`. Done when the task and, when last, the part read done.
8. Commit when the folder is a git repo: the task file and `MAP.md`; message `review <id>: clean` or `review <id>: <n> findings`; on a rejected hook, print its one line and stop. Done when `git status` shows none of them.
9. Print `Next: /build-it <id>` with findings, else `Next: /atlas`, as the last line.

## Output
- The task's Review section or issue comment, one dated pass.
- The task's status, and the part's when it was the last task.
- On GitHub, a PR approval or change request, and a merge under `Merge: review-it`.
- One commit, when the folder is a git repo.

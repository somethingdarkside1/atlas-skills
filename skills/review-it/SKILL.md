---
name: review-it
description: Check a task's result against its brief and the project's conventions, record findings on the task, and close or merge when clean.
disable-model-invocation: true
---

# Review it

Check what was delivered against what was asked and how this project does things, then close the loop.

## Read first
- `plan/README.md`: the `Tracker:` and `Merge:` lines, the Ids and statuses section, and the Git section.
- Tasks in review: `grep -l '^status: review' plan/*/*.md`, or assigned open `atlas:task` issues with an open PR.
- The task, its part's brief, the decisions the brief links, `GLOSSARY.md`, existing things of the same kind as the delivered thing, and the format comment at the top of `MAP.md` with the part's section.

## Steps
1. If `MAP.md` is missing, print `Run /atlas first.` and `Next: /atlas`, and stop. Pick the task: the argument, else the one task in review, else ask which. Done when one task is open.
2. Review in a fresh context when the harness can give you one: hand a sub-agent the task id and this rule, "read the brief, the decisions, the glossary, Delivered, the delivered thing, and existing things of the same kind; nothing else". Otherwise review inline and say so in the pass. Done when the reviewer has only those inputs.
3. Check one, the brief: open what Delivered points at, re-run Check by when you can, and test each Done when box against the brief's Outcome and Out of scope. Check two, the conventions: the glossary's words are used and none from an Avoid list; no accepted decision is contradicted; the thing is made the way existing things of that kind are made here (structure, naming, tone, style, and for code the project's documented standards). A ticked `(you)` box counts as confirmed by the human; an unticked one is listed. Done when every box is verified, listed for you, or a finding.
4. Write the pass: dated, one heading per check, each finding one sentence with one citation (the brief line or the glossary entry), or `clean`; then `For you to check:` with each unticked `(you)` box and what to look at, when any. Files: append it to the task's Review section. GitHub: one comment on the issue; on the PR, approve when clean, else request changes with a link to the comment. Done when the pass is on the task.
5. With findings: set the task to doing and end with `Next: /build-it <id>`. With only `(you)` boxes left: the task stays in review, and the last lines are `Tick the (you) boxes on <id> when you have looked.` and `Next: /review-it <id>`. Done when the builder or the human can act without asking.
6. Clean: files, `status: done`; GitHub, merge or hand over as the Git section says for the `Merge:` line (your merge closes the issue; a person's merge does the same later). When every task of the part is done and merged, set the part's status line and node class to `done` and close the parent issue; under `Merge: human`, `/atlas` does both once the last PR is merged. Done when the task and, when last, the part read done.
7. Commit as `plan/README.md` says: the task file and `MAP.md`; message `review <id>: clean` or `review <id>: <n> findings`. Done when `git status` shows none of them.
8. Print the last line from step 5, or `Next: /atlas` when clean.

## Output
- The task's Review section or issue comment, one dated pass.
- The task's status (files), and the part's when it was the last task.
- On GitHub, a PR approval or change request, and a merge under `Merge: review-it`.
- One commit, in a repo.

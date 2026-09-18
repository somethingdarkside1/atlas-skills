---
name: review-it
description: Check a task's result against its brief and the project's conventions, record findings on the task, and mark it done when clean.
disable-model-invocation: true
---

# Review it

Check what was delivered against what was asked and how this project does things, then close the loop.

## Read first
- The Ids and statuses section of `plan/README.md`, and the text after its task template.
- Tasks in review: `grep -rl '^status: review' plan --include='[0-9]*.md'`.
- The task, its part's brief, the decisions the brief links, `GLOSSARY.md`, the project instructions (`CLAUDE.md` or `AGENTS.md`), and existing files of the same kind as the delivered thing.

## Steps
1. If a home is missing, print `Next: /setup-atlas` and stop. Pick the task: the argument, else the one task in review, else ask which. A task that is not in review: say its status, print `Next: /atlas`, and stop. Done when one task is open.
2. Review in a fresh context when the harness can give you one: hand a sub-agent the task file's path and this rule, "read the task, its brief, the decisions the brief links, the glossary, the project instructions, the delivered thing, and existing things of the same kind; judge the result, not how it was built". Otherwise review inline and say so in the pass. Done when the reviewer has those inputs.
3. Compare first: recompute the newest Delivered entry's `Version:` checksum over its `Files:` line, as the task format in `plan/README.md` says. When it differs, or a file is gone, write a pass saying `Changed since delivery: <version then> is now <version now>`, set `status: doing`, and end with `Next: /build-it <id>` (steps 7 and 8), because the builder's checks no longer describe the thing. `Version: none` skips the compare. Check one, the brief: open what the newest Delivered entry points at, re-run Check by when you can, and test each Done when box against the brief's Outcome and Out of scope. Check two, the conventions: the glossary's words are used and none from an Avoid list (a word inside a quotation, a file name, or the name of an outside tool is not a finding); no accepted decision is contradicted; the thing is made the way existing things of that kind are made here (structure, naming, tone, style, and for code the project's documented standards). A ticked `(you)` box counts as confirmed by the human; an unticked one is listed; one the human says is wrong, in the argument or in chat, is a finding in their words. A wrong statement in Delivered that changes no delivered file and no box is not a finding: put the right statement in the pass as `Corrected: <what the entry should say>`. Done when every box is verified, listed for you, or a finding.
4. Write the pass as a dated entry (`### YYYY-MM-DD`) in the task's Review section: first `Reviewed: <the version you compared>`, then one line or short block per check, starting `Brief:` and `Conventions:`, each finding saying what is wrong, where (one citation: the brief line, the decision, the glossary entry, or the file and line), and what would fix it, or `clean`; then any `Corrected:` lines; then `For you to check:` with each unticked `(you)` box and what to look at, when any. Untick any box a finding contradicts. Done when the pass is on the task.
5. With findings: set `status: doing`, and the last line is `Next: /build-it <id>`. When a finding can only be fixed by changing the brief (the Outcome, the Out of scope, or a decision), also write it as a question on the part's open questions, and the last line is `Next: /interview-me <part>`. With only `(you)` boxes left: the task stays in review, and the last lines are `Tick the (you) boxes on <id> when you have looked, or tell /review-it what is wrong.` and `Next: /review-it <id>`. Done when the builder or the human can act without asking.
6. Clean: set `status: done`. When every other task of the part is done or canceled, set the part's status line and node class to `done`. Done when the task and, when last, the part read done.
7. Save as the project's `Saving work` section says: the task file and `MAP.md` (or the file in `map/` that holds the part); message `review <id>: clean`, `review <id>: <n> findings`, or `review <id>: for you to check`. Done when they are saved, or you have said why they are not.
8. Print the last line from step 5, or `Next: /atlas` when clean.

## Output
- The task's Review section, one dated pass.
- The task's status, and the part's when it was the last task.
- An open question on the part, when a finding needs the brief changed.
- One save, as the project says.

---
name: build-it
description: Work one ready task in whatever medium it names, or pick up one that came back with findings, verify it, and record what was delivered on the task.
disable-model-invocation: true
---

# Build it

Do one task, prove it, write down what you made.

## Read first
- The Ids and statuses section of `plan/README.md`.
- Task states: `grep -rH -E '^(status|blocked_by):' plan --include='[0-9]*.md'`.
- The task, whole, with anything already under Delivered and Review; its part's brief; the decisions the brief links; the part's section in `MAP.md`.
- The newest handoff in `notes/`, when its `Target:` is this task: it says which files were in flight.
- Existing files of the kind Delivers names, for how this project makes them.

## Steps
1. If a home is missing, print `Next: /setup-atlas` and stop. Pick the task: the argument; else a task in doing; else the next ready task by the rule in `plan/README.md`. A todo task with a blocker that is not done: print the blockers and `Next: /atlas`, and stop. A task in review, done, or canceled: say so, print `Next: /atlas`, and stop. Nothing to pick: print `Nothing ready.` and `Next: /atlas`, and stop. Done when one task is open.
2. Mark it: `status: doing`. When the part reads decided or done, set its status line to `building` and its node class to `:::building`. A task that was already doing: read what Delivered and the last Review pass say and carry on from there; the findings are the work list. Done when the task reads doing and the part reads building.
3. Make what Delivers names, the way this project already makes that kind of thing, in the glossary's words. For code, run the project's own checks when they exist. A choice that passes the three tests in `decisions/README.md` becomes a decision file, linked on the part's `Decisions:` line; a term the task needed becomes a glossary entry. Leave the brief, the other tasks, and the rest of the map as they are. When the brief is wrong or silent on something you need, write the question on the part's open questions and stop early (step 6) with `The brief needs an answer: <question>` and `Next: /interview-me <part>`. Done when the thing exists where Delivers says.
4. Run Check by yourself when you can, and tick every Done when box you verified; `(you)` boxes stay for the human. When the check fails, fix and run it again; when it still fails, tick nothing it covers and stop early (step 6) with `Next: /build-it <id>`. Done when every box you could check is ticked.
5. When you cannot finish without an answer from the human, stop early (step 6), with an `Open question:` line in that entry and `Next: /build-it <id>`. Otherwise write Delivered as a dated entry (`### YYYY-MM-DD`) below any earlier ones: what was made, where it lives, how it was verified (what you ran or looked at, and what you saw), which boxes you could not check and why, and any decision or term you wrote. Then set `status: review`. Done when Delivered reads as claims a reviewer can check and the task reads review.
6. Stopping early keeps the task in doing: write a dated Delivered entry saying what exists so far, where you stopped, and why (for a failed check, what you ran and what happened), then save as step 7 says, then print the lines that step named, the `Next:` line last. Done when a fresh session could carry on from the task file alone.
7. Save as the project's `Saving work` section says: the files you made, the task file, `MAP.md` (or the file in `map/` that holds the part), and any decision or glossary entry you wrote; message `build <id>: <what was made>`. Done when they are saved, or you have said why they are not.
8. Print `Next: /review-it <id>` as the last line.

## Output
- The delivered thing, where Delivered says.
- The task: status review, boxes ticked, a dated Delivered entry. After an early stop: status doing, and a dated entry saying where it stopped.
- `MAP.md`: the part's status building, a link to any new decision, and an open question when the brief needed one.
- Decisions or glossary entries the work needed.
- One save, as the project says.

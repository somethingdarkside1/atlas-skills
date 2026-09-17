---
status: review
kind: build
blocked_by: ["core-model/01"]
---

# 06: Patch the draft so an ordinary run works

## Delivers
A 0.2 patch of the draft skills, their templates, and the public front page: the faults that stop an ordinary run are fixed, hosted tracker text is gone, the saving rule has one home, and setup is its own skill.

Source: [Decision 0021](../../decisions/0021-patch-the-draft-first.md) and the [whole-set review](../../notes/2026-09-17-review-skills-as-a-whole.md), faults 1 to 7, N8, and the "Fix now" and "Remove" lists. See the [package brief](brief.md).

## Check by
Run each skill's Read first commands under zsh against a templates-only folder and a scratch copy of `examples/brand/`, and have a separate agent walk the skills against each other for stuck states and loops.

(you) Then one run with the 0.2 skills installed. The 2026-09-11 script names `/atlas go` and GitHub mode, which 0.2 removed, so use this one:

1. In an empty scratch folder with `git init`: `/setup-atlas`, then `/atlas`. Expect five homes, a `Saving work` section, and `Next: /interview-me`.
2. Copy `examples/brand/` to another scratch folder with `git init` and a first commit. `/atlas` should report `wordmark/02` as doing with nothing delivered, and send you to `/build-it wordmark/02`.
3. `/build-it wordmark/02`, `/review-it wordmark/02` (reject the `(you)` box once), `/build-it wordmark/02`, `/review-it wordmark/02`.
4. `/interview-me palette` and stop after one round with `/park-it`. In a fresh session, `/atlas` should name the handoff as live.
5. Finish the interview, then `/plan-it palette`, `/build-it`, `/review-it`, `/atlas`.
6. `/plan-it wordmark "export a favicon"`, then `/map-it`.

Record each command, what it wrote, and anything that broke or asked a needless question, as one `review` note.

## Done when
- [x] Every Read first command returns cleanly under zsh on a fresh project and on the brand copy, and none picks up an example block from a README.
- [x] Tasks carry todo, doing, review, done, and canceled from one table in `plan/README.md`, and every skill points to it.
- [x] `(you)` sits on Done when boxes in the template and in every skill that reads or writes it.
- [x] No skill or template names a hosted tracker, a PR, an approval, or a merge, or makes a branch, and `/atlas` has no `go`. The project-owned `Saving work` section is the one place that says where commits go.
- [x] The saving rule lives in one project-owned section, and each skill names only its files and its message.
- [x] `/atlas` changes nothing; `/setup-atlas` creates only what is missing, asks first, and leaves `CONTEXT.md` in place.
- [x] A fresh project starts with an empty map and glossary, and the router sends it to `/interview-me`.
- [x] A handoff is followed only while its target is still open, and a newer note of another kind does not hide it.
- [x] The README front page shows the loop, what each skill writes, and the skills table, and says plainly that nothing has been run end to end.
- [ ] (you) One full run on a scratch brand copy is recorded as a note.

## Delivered
### 2026-09-17
Attempt started in the worktree `skill-list-analysis-d40ccf`, branch `codex/skills-patch-0-2`, from `78af321` (main `24b24ef` plus the review note). The checkout was clean and matched fetched `origin/main`.

Made:
- `skills/setup-atlas/`, a new skill holding the project templates, split out of `/atlas` under [0015](../../decisions/0015-setup-adopts-routing-observes.md). It creates only missing homes, asks first, copies `CONTEXT.md` terms and leaves the file, writes the block once for linked instruction files, and adds a project-owned `Saving work` section.
- `/atlas` rewritten read-only: shell-safe reads, routing from files (a review waiting on you, open-question markers, doing and ready tasks, plans, an end state), and a live handoff ranked after reviews and open questions.
- The other seven skills patched along the review's "Fix now" and "Remove" lists: the `review` and `canceled` statuses, `(you)` on boxes, cancel instead of delete, the one-task route in `/plan-it`, resume and early stops that record and save in `/build-it`, the reject route and a wider reviewer context in `/review-it`, `not clear yet` verdicts in `/prototype-it`, owned saves and a `Target:` line in `/park-it`, graph checks and derived statuses in `/map-it`. GitHub mode, `go`, and every per-skill commit rule are gone.
- Templates: one ids and statuses table, empty map and glossary, the handoff rule, the `Saving work` section. `examples/brand/` brought to the same formats, with a `CLAUDE.md` and an `AGENTS.md` link.
- README front page restored for nine skills, the manifests at `0.2.0`, and the pointers in `INDEX.md`, `CLAUDE.md`, and `skills/README.md` (which now says how to test a read command).

Content identity: `skills/` tree `ec9f4d5547661e946260e44556f9256d016b4f8f`, `examples/brand/` tree `4864803d392dccc295da7c7a6ea18e5c6a26f57f` (compare with `git rev-parse <commit>:skills`).

Checked:
- Every `grep` and `ls` command named in a skill (12) was extracted and run under zsh against a folder holding only the templates and a copy of `examples/brand/`: no errors and no match from a README example. The same test on the first draft caught two leaks of my own, fixed before this entry.
- `python3 scripts/check-project.py`: 7 parts, 25 tasks, 114 documents, 689 local links, no errors. `claude plugin validate .` and `claude plugin validate .claude-plugin/plugin.json` passed. `bash -n scripts/link-skills.sh` passed. `git diff --cached --check` passed.
- No em or en dashes in the skills, the example, the README, or this session's notes. The only mention of a tracker is `/atlas` saying it no longer reads `Tracker: github`.

Not checked: the `(you)` run. No skill has been invoked. Semicolons remain as list separators, as in the first draft and across this repository.

## Review
### 2026-09-17
Examined the staged output above against this task's Delivers and Done when at base `f66c6f1`, in two passes by separate agents with no stake in the text, each walking scenarios through the skills rather than reading them one by one.

Pass one found 15 problems. The run-stopping ones: a doing task could not change after its brief moved; a rejected `(you)` box had no route back, so `/atlas` would repeat `/review-it` forever; `/build-it` stopped early without recording or saving. The rest: a handoff rule with two thresholds, same-day handoffs out of order, wrong `Next:` lines, "Needs decided" against "still sketched", a done part that gained a task left stuck, prototype routes ranked too low, `/plan-it` blind to other parts, no skill linking decisions on the map, a possible `/atlas` and `/setup-atlas` bounce, no end state, and the brand example out of step with the templates. All fixed.

Pass two confirmed all 15 fixes against file and step, then found 15 more. The run-stopping ones: a live handoff outranked a newer open question, and a handoff could carry `Next: /atlas`, each making `/atlas` repeat. The rest: a findings pass mistaken for waiting on you, a building part with only canceled tasks, `/plan-it` overwriting existing tasks, a re-interview adding a draft line to a finished brief, the diagram never read, split-part saves naming only `MAP.md`, and nits. All fixed. The final text had the mechanical checks rerun, not a third agent pass.

Conventions: plain words, no dashes, formats kept in the project's homes, and the draft's voice.

For you to check:
- The run in Check by, recorded as one note. This box is the acceptance gate.
- Two choices from your other session are left out on purpose, so they can land on top: the `Version:` line (draft decision 0022) and dropping the glossary diagram (draft 0023).

Known limits: the brand fixture still names `wordmark/candidates.svg`, which does not exist ([validation/02](../validation/02-create-behavior-fixtures.md)). Splitting a part that has work, renaming a part, and a check of a part's Outcome remain with tasks 03 and 02.

---
status: doing
kind: build
blocked_by: ["core-model/01"]
---

# 06: Patch the draft so an ordinary run works

## Delivers
A 0.2 patch of the draft skills, their templates, and the public front page: the faults that stop an ordinary run are fixed, hosted tracker text is gone, the saving rule has one home, and setup is its own skill.

Source: [Decision 0021](../../decisions/0021-patch-the-draft-first.md) and the [whole-set review](../../notes/2026-09-17-review-skills-as-a-whole.md), faults 1 to 7, N8, and the "Fix now" and "Remove" lists. See the [package brief](brief.md).

## Check by
Run each skill's Read first commands under zsh against a templates-only folder and a scratch copy of `examples/brand/`. Then (you) run the 2026-09-11 test script once on a scratch copy and record what broke as a note.

## Done when
- [ ] Every Read first command returns cleanly under zsh on a fresh project and on the brand copy, and none picks up an example block from a README.
- [ ] Tasks carry todo, doing, review, done, and canceled from one table in `plan/README.md`, and every skill points to it.
- [ ] `(you)` sits on Done when boxes in the template and in every skill that reads or writes it.
- [ ] No skill or template names a hosted tracker, a branch, a PR, an approval, or a merge, and `/atlas` has no `go`.
- [ ] The saving rule lives in one project-owned section, and each skill names only its files and its message.
- [ ] `/atlas` changes nothing; `/setup-atlas` creates only what is missing, asks first, and leaves `CONTEXT.md` in place.
- [ ] A fresh project starts with an empty map and glossary, and the router sends it to `/interview-me`.
- [ ] A handoff is followed only while its target is still open, and a newer note of another kind does not hide it.
- [ ] The README front page shows the loop, what each skill writes, and the skills table, and says plainly that nothing has been run end to end.
- [ ] (you) One full run on a scratch brand copy is recorded as a note.

## Delivered
Attempt started 2026-09-17 in the worktree `skill-list-analysis-d40ccf`, branch `codex/skills-patch-0-2`, from `78af321` (main `24b24ef` plus the review note). The checkout was clean and matched fetched `origin/main` before the note.

## Review
Pending.

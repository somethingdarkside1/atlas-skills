---
date: 2026-09-13
kind: review
part: project
---

# Second pass over the eight skills: one home per rule

## Summary
Two read-throughs of the skills, the five things, and the example found rules stated in two or three places with small differences, states that skills wrote but could not read back, and four words the glossary bans that the skills used. Every rule now has one home, waits are on disk, and the git story is written once. The long form, with tables, is `docs/second-pass.html`.

## Detail
What moved where: task ids, the four statuses, "which task is next", and the three git environments are in `plan/README.md`; the open-questions shape and its markers are in the map's format comment; a live handoff is defined in `notes/README.md`; the shapes every skill shares (step 1, the `Next:` line, the commit sentence, waits on disk, precedence) are in `skills/README.md`. Decisions 0009 (task id), 0010 (waits on disk, review status), and 0011 (the home wins) record the choices.

Fixed in the skills: `/build-it` commits the map and any decision or term it wrote, returns to the default branch after the PR, and sends a missing answer to the map instead of looping `/atlas go`; `/review-it` reads a `review` status instead of comparing dates, hands the sub-agent the existing things of the same kind, and leaves `(you)` boxes in the file; `/plan-it` and `/atlas` test for tasks, not for a `Plan:` line; `/atlas` honours `Needs:` when picking a sketched part and resumes only from a live handoff; `/interview-me` stops when a needed part is not decided and writes decisions in part scope only.

Fixed in the example: the three folder READMEs now carry their formats, task 01's pass is dated, `(you)` boxes are marked, and Palette's questions are a list.

Still to do, in order: the end-to-end test in files mode on the example; the same in GitHub mode on a real repo, which also checks that `gh` 2.100 can create sub-issues and blocked-by dependencies; `scripts/link-skills.sh` and `claude plugin validate . --strict`; a small `scripts/check.sh` that tests the mechanical invariants (unique part ids, blockers that exist, diagram matching sections) so `/atlas` line four rests on a script rather than a read; then the packaging part.

## Copied into
plan/README.md, notes/README.md, the MAP.md format comment, GLOSSARY.md, skills/README.md, CLAUDE.md, decisions/0009 to 0011, all eight SKILL.md files, README.md.

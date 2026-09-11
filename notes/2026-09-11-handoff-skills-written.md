---
date: 2026-09-11
kind: handoff
part: project
---

# Handoff: all eight skills written in one session

## Summary
One interview session settled the cross-cutting rules and every skill, then wrote all eight under `skills/`. Nothing has been run yet: every skill part on `MAP.md` is building until the end-to-end test passes. Next: `/atlas` on a scratch copy of `examples/brand/`, then the whole loop on a real project.

## Detail
What this session decided is in its homes: decisions 0005 (accepted), 0007, 0008; the `Needs:` line and derived diagrams in the `MAP.md` format comment; two modes and `Done when` / `Check by` in `plan/README.md`; Round and Prototype in `GLOSSARY.md`; the skill behaviour in each `SKILL.md`. Rules that live only in the skills and are worth knowing before testing:

- Every skill: step 1 stops with `Run /atlas first.`; failures are one line naming the fix; the last line is `Next: /command <id>`; it commits only what it wrote, on the current branch, when the folder is a git repo; `/park-it` commits the five things wholesale.
- Statuses have one owner each: interview moves sketched to decided, build moves decided to building and todo to doing, review moves doing to done and building to done; `/atlas` repairs derived and swept statuses; `/map-it` never moves one.
- The round shape: reply by number, skipped questions take the `➡️`, a `Taken by default:` receipt, up to eight questions.

How to test, in order: copy `examples/brand/` to a scratch folder with `git init`; run `/atlas`, `/interview-me palette`, `/plan-it palette`, `/build-it`, `/review-it`, `/atlas go`, `/park-it`, `/atlas`; then `/prototype-it` on a `(prototype)` question and `/map-it palette` for a split. Record what broke as one note (`kind: review`), fix the skill, and move its part to done. Then a real project, GitHub mode included.

After the test passes: `scripts/link-skills.sh`, `claude plugin validate . --strict`, push to `somethingdarkside1/atlas-skills`. Run one Atlas session per checkout at a time.

## Copied into
MAP.md (statuses), skills/README.md (checklist), README.md (status line and skills table).

# Atlas

## Atlas (atlas: 2)

This project uses Atlas. `GLOSSARY.md` holds the words, `MAP.md` the shape, `plan/` the work, `decisions/` the why, `notes/` the dated record. Read `GLOSSARY.md` and `MAP.md` before working and use their words. Each file starts with its own format; follow it, and when a skill and a format disagree, the format wins. Write hard-to-reverse choices to `decisions/`. Run `/atlas` to see what is next.

## This repo

The Atlas skill set plus the files that describe it, written with its own method. The block above is the one `/atlas` writes into every project.

## Layout

- `skills/<name>/SKILL.md`: one folder per skill, flat, no buckets. The skeleton, the shapes every skill shares, and the done-checklist are in `skills/README.md`. Templates a skill creates files from live beside it in `templates/`; `/atlas` owns the five things' templates.
- `examples/brand/`: a small finished project to run skills against. Copy it to a scratch folder first.
- `reference/` is gitignored. A local, unchanged copy of Matt Pocock's set can sit there for comparison; it is never committed.
- `README.md` is the docs page and the install page. `docs/` holds standalone HTML write-ups of a review or design pass; the dated record of the same pass is its note.

## Writing a skill

- One job per skill, as short as the job allows, numbered steps, each ending with a "done when" line.
- Every rule has one home. Formats live in the five things (the hidden comments and folder READMEs, copied from `skills/atlas/templates/`); the git and tracker rules live in `plan/README.md`; the shapes skills share live in `skills/README.md`. A skill points at the home and quotes nothing from it.
- Every skill opens with the same step 1, ends with the same `Next:` line, and commits with the same sentence; the exact shapes are in `skills/README.md`.
- Positive instructions by default. A negative is allowed only where it draws a boundary a positive cannot, and at most one per step.
- Every skill starts by reading the format comment of each of the five things it will edit.
- User-invoked skills carry `disable-model-invocation: true` and a three-line `agents/openai.yaml` with `policy.allow_implicit_invocation: false`.

## Prose

Plain words. No em dashes: use a comma, a colon, a period, or parentheses.

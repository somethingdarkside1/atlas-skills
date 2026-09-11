# Atlas

## Atlas (atlas: 1)

This project uses Atlas. `GLOSSARY.md` holds the words, `MAP.md` the shape, `plan/` the work, `decisions/` the why, `notes/` the dated record. Read `GLOSSARY.md` and `MAP.md` before working and use their words. Each file starts with its own format; follow it. Write hard-to-reverse choices to `decisions/`. Run `/atlas` to see what is next.

## This repo

The Atlas skill set plus the files that describe it, written with its own method. The block above is the one `/atlas` writes into every project.

## Layout

- `skills/<name>/SKILL.md`: one folder per skill, flat, no buckets. The skeleton and the done-checklist are in `skills/README.md`. Templates a skill scaffolds live beside it in `templates/`; `/atlas` owns the five things' templates.
- `examples/brand/`: a small finished project to run skills against. Copy it to a scratch folder first.
- `reference/` is gitignored. A local, unchanged copy of Matt Pocock's set can sit there for comparison; it is never committed.
- `README.md` is the docs page and the install page.

## Writing a skill

- One job per skill, under about 120 lines, numbered steps, each ending with a "done when" line.
- Positive instructions only. Say what to do, not what to avoid.
- Formats are never restated in a skill. They live in the five things themselves (hidden comments and folder READMEs) and in `skills/atlas/templates/`.
- Every skill starts by reading the five things it will touch, including the hidden format comment.
- User-invoked skills carry `disable-model-invocation: true` and a three-line `agents/openai.yaml` with `policy.allow_implicit_invocation: false`.

## Prose

Plain words. No em dashes: use a comma, a colon, a period, or parentheses.

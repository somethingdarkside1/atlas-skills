# Atlas

This repo is the Atlas skill set plus the files that describe it. It uses its own method: `GLOSSARY.md` holds the words, `MAP.md` the shape, `plan/` the work, `decisions/` the why, `notes/` the dated record. Read `GLOSSARY.md` and `MAP.md` before changing anything; use their words.

## Layout

- `skills/<name>/SKILL.md`: one folder per skill, flat, no buckets. Templates a skill scaffolds live beside it in `templates/`.
- `reference/mattpocock-skills/`: an unchanged MIT copy of the set Atlas was reshaped from. Read it for comparison; never edit it.
- `README.md` is the docs page and the install page.

## Writing a skill

- One job per skill, under about 120 lines, numbered steps, each ending with a "done when" line.
- Positive instructions only. Say what to do, not what to avoid.
- Formats are never restated in a skill. They live in the five things themselves (hidden comments and folder READMEs) and in `skills/atlas/templates/`.
- Every skill starts by reading the five things it will touch, including the hidden format comment.
- User-invoked skills carry `disable-model-invocation: true` and a three-line `agents/openai.yaml` with `policy.allow_implicit_invocation: false`.

## Prose

Plain words. No em dashes: use a comma, a colon, a period, or parentheses.

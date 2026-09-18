---
name: setup-atlas
description: Create the five things in a project, or only the ones that are missing, and add the Atlas block to the project instructions; safe to run again.
disable-model-invocation: true
---

# Set up Atlas

Give this project its five things without touching what is already there.

## Read first
- Which of `GLOSSARY.md`, `MAP.md`, `plan/README.md`, `decisions/README.md`, and `notes/README.md` exist.
- `README.md`, and `CONTEXT.md` when there is one.
- `CLAUDE.md` and `AGENTS.md`: whether each exists, whether they are one file (`ls -l` shows a link), and whether either holds an `## Atlas (atlas: N)` block or a `## Saving work` section.
- `git rev-parse --is-inside-work-tree`.

## Steps
1. Say what is there and what is missing, one line each, and ask `Create what is missing? (yes)` before writing anything; when there is no README, ask `What is this, in a sentence?` in the same message. Nothing missing, the block current, and a `Saving work` section in place: print `Already set up.` and `Next: /atlas`, and stop. On no: print `Next: /setup-atlas` for when you are ready, and stop. Done when the human has said yes.
2. Create only the missing homes from `templates/` beside this file: `GLOSSARY.md`, `MAP.md`, `plan/README.md`, `decisions/README.md`, `notes/README.md`. A home that exists stays exactly as it is. In a new `MAP.md` and `GLOSSARY.md`, fill the name and the paragraph from the README, or from the answer in step 1; `/interview-me` rewrites both later. Add no parts and no terms. Done when all five exist.
3. When a `CONTEXT.md` exists: copy each term it defines into `GLOSSARY.md` in the entry shape, leave `CONTEXT.md` where it is, and say which terms were copied and what stayed behind. Done when every copied term is named.
4. The block. `templates/CLAUDE-block.md` holds two sections, `## Atlas (atlas: N)` and `## Saving work`. Put them into the project instructions: into `CLAUDE.md` and `AGENTS.md` where each exists, once when they are one file, and when neither exists, into a new `CLAUDE.md` with `AGENTS.md` made a link to it (`ln -s CLAUDE.md AGENTS.md`), so the two cannot drift apart. An Atlas block with a lower number: replace that section alone, from its heading to the next `##`. A `## Saving work` section that exists is the project's own, so leave it; add the template's only where there is none. Done when each instruction file holds the current Atlas block once and a `Saving work` section.
5. No repo: offer `git init`, and carry on either way. Done when the human has answered.
6. Save as the project's `Saving work` section says: the files you created or changed; message `setup-atlas: the five things`. Done when they are saved, or you have said why they are not.
7. Print what was created, one line each, then `Next: /atlas` as the last line.

## Output
- The missing homes, the Atlas block, and the `Saving work` section in the project instructions.
- Terms copied from `CONTEXT.md`, when there was one.
- One save, as the project says.

---
name: park-it
description: Pause the session into a dated handoff note that the next /atlas resumes from, and commit everything in the five things.
disable-model-invocation: true
---

# Park it

Stop here in a way a fresh session can pick up.

## Read first
- The note template in `notes/README.md`.
- `git status --short`, for uncommitted changes in the five things and `prototypes/`.
- The argument, if any: what the next session is for.

## Steps
1. If `notes/` is missing, print `Run /atlas first.` and stop. Done when the folder is there.
2. Write `notes/YYYY-MM-DD-handoff-<slug>.md` from the template, `kind: handoff`, `part:` the part in hand or `project`. Summary: where things stand in three sentences at most, ending with a `Next: /command <id>` line in the exact shape the skills print. Detail: only what is not yet in a home: the round in flight and the answers so far, the task in doing and where it stands, anything said in chat a fresh session must know, and the argument's focus. Link the five things instead of repeating them. No secrets, keys, tokens, or personal data, and no chat quoted verbatim. Copied into: `nothing durable` unless something was. Done when the note holds nothing a home already holds.
3. Commit when the folder is a git repo: everything under `GLOSSARY.md`, `MAP.md`, `map/`, `plan/`, `decisions/`, `notes/`, and `prototypes/`, and nothing else; message `park: <slug>`; on a rejected hook, print its one line and stop. Done when `git status` shows none of those paths.
4. Print `Parked. Next: /atlas` as the last line.

## Output
- `notes/YYYY-MM-DD-handoff-<slug>.md`
- One commit of the five things, when the folder is a git repo.

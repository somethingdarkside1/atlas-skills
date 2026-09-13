---
name: park-it
description: Pause the session into a dated handoff note that the next /atlas resumes from, and commit everything in the five things.
disable-model-invocation: true
---

# Park it

Stop here in a way a fresh session can pick up.

## Read first
- The note template in `notes/README.md`, and what makes a handoff live.
- `git status --short`, for uncommitted changes in the five things and `prototypes/`.
- The argument, if any: what the next session is for.

## Steps
1. If `MAP.md` is missing, print `Run /atlas first.` and `Next: /atlas`, and stop. Done when the five things are there.
2. Write `notes/YYYY-MM-DD-handoff-<slug>.md` from the template, `kind: handoff`, `part:` the part in hand or `project`. Summary: where things stand in three sentences at most, then `Next: /command <id>` in the shape the skills print, as its own line. Detail: only what is not yet in a home: the round in flight and the answers so far, the task in doing or review and where it stands, anything said in chat a fresh session must know, and the argument's focus. Link the five things instead of repeating them. Keep secrets, keys, tokens, personal data, and verbatim chat out. Copied into: `nothing durable` unless something was. Done when the note holds nothing a home already holds.
3. Commit as `plan/README.md` says: everything under the five things and `prototypes/`; message `park: <slug>`. Done when `git status` shows none of those paths.
4. Print `Parked.` and then `Next: /atlas` as the last line.

## Output
- `notes/YYYY-MM-DD-handoff-<slug>.md`
- One commit of the five things, in a repo.

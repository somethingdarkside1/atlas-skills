---
name: park-it
description: Pause the session into a dated handoff note that the next /atlas resumes from, and save what this session's commands wrote.
disable-model-invocation: true
---

# Park it

Stop here in a way a fresh session can pick up.

## Read first
- The note template and the Handoffs rule in `notes/README.md`.
- `git status --short`, in a repo, for uncommitted changes in the five things and `prototypes/`.
- The task or part in hand, and its status today.
- The argument, if any: what the next session is for.

## Steps
1. If `notes/` is missing, print `Next: /setup-atlas` and stop. Done when the folder is there.
2. Write `notes/YYYY-MM-DD-handoff-HHMM-<slug>.md` from the template, with the time now as `HHMM` so handoffs sort in the order they were written: `kind: handoff`, `part:` the part in hand or `project`. Summary: where things stand in three sentences at most, ending with a `Next: /command <id>` line in the exact shape the skills print, naming the command that resumes the target, never `/atlas`. Detail opens with `Target: <task id or part id>, <its status today>` (for the whole project, `Target: project,` and the parts by status in the shape of `/atlas` line one), then holds only what is not yet in a home: the round in flight and the answers so far, the task in doing with the files in flight and where they are, anything said in chat a fresh session must know, and the argument's focus. Link the five things instead of repeating them. No secrets, keys, tokens, or personal data, and no chat quoted verbatim. Copied into: `nothing durable` unless something was. Done when the note holds nothing a home already holds.
3. Save as the project's `Saving work` section says: the note, and the files under the five things and `prototypes/` that this session's Atlas commands wrote and that are still unsaved; message `park: <slug>`. Every other uncommitted path goes into the note's Detail as a list, and stays as it is. Done when your files are saved and the rest is listed, or you have said why not.
4. Print `Parked.`, then `Next: /atlas` as the last line.

## Output
- `notes/YYYY-MM-DD-handoff-HHMM-<slug>.md`
- One save of this session's Atlas files, as the project says.

---
name: prototype-it
description: Make the smallest thing that answers one part's open question, take the human's verdict, and write it back to the map and a note.
disable-model-invocation: true
---

# Prototype it

Answer one question that talking could not, with a made thing nobody will keep.

## Read first
- The argument: the question, in plain words.
- `MAP.md`: the part whose open questions carry that question, marked `(prototype)`; its brief if it has one.
- The note template in `notes/README.md`.

## Steps
1. If `MAP.md` is missing, print `Run /atlas first.` and stop. If no part on the map carries the question, print `Name it on a part first: /interview-me <part>` and stop. Done when the part is known.
2. Make the smallest thing that answers the question, in the medium of the question: three SVG directions, one HTML file, a copy draft, a spreadsheet. No tests, no persistence, no error handling, nothing a task will link to (a task may copy from it). Put it in `prototypes/<part>-<slug>/` with the question as the first line of a `README.md` there. Done when the thing shows an answer.
3. Report in four lines: what was made, what it shows against the question, the verdict you recommend and why, what the prototype cannot show. Then wait for the human's verdict. When the question is one you can check yourself, the third line proposes the verdict and you ask only for a confirmation. Done when the human has stated or confirmed the verdict.
4. Write `notes/YYYY-MM-DD-prototype-<slug>.md` from the template: `kind: prototype`, the part, Summary is the verdict, Detail is what was tried and the path under `prototypes/`, Copied into names `MAP.md`. Done when the note exists.
5. On the map, rewrite the part's `(prototype) <question>` to `(answered, see notes/<file>) <verdict in a phrase>`. Done when the map shows the answer.
6. Commit when the folder is a git repo: the prototype folder, the note, and `MAP.md`; message `prototype <part>: <verdict in a phrase>`; on a rejected hook, print its one line and stop. Done when `git status` shows none of them.
7. Print `Next: /interview-me <part>` as the last line.

## Output
- `prototypes/<part>-<slug>/`
- `notes/YYYY-MM-DD-prototype-<slug>.md`
- `MAP.md`: the part's open question now carries the answer.
- One commit, when the folder is a git repo.

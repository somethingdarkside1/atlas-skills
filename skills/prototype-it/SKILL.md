---
name: prototype-it
description: Make the smallest thing that answers one part's open question, take the human's verdict, and write it back to the map and a note.
disable-model-invocation: true
---

# Prototype it

Answer one question that talking could not, with a made thing nobody will keep.

## Read first
- The argument: a part id, or the question in plain words. With no argument, the `(prototype)` questions on the map: `grep -n '^Open questions:.*(prototype' MAP.md`, and the same in `map/` when that folder exists.
- `MAP.md`: the part whose open questions carry the question, marked `(prototype)`; its brief if it has one.
- The note template in `notes/README.md`, and the newest handoff in `notes/` when its `Target:` is this part.

## Steps
1. If a home is missing, print `Next: /setup-atlas` and stop. Find the question: the part's one `(prototype)` question, or the one the argument's words match; when several fit, list them and ask which. If no part on the map carries it, print `Name it on a part first.` and `Next: /interview-me <part>`, and stop. Done when one question on one part is open.
2. Make the smallest thing that answers the question, in the medium of the question: three SVG directions, one HTML file, a copy draft, a spreadsheet. Tests, saved data, and error handling belong in it only when the question is about them. Nothing a task will link to (a task may copy from it, and what it copies gets built and reviewed like anything else). Put it in `prototypes/<part>-<slug>/`, adding `-2` when that folder is taken, with a `README.md` there: the question as the first line, and how long you will spend as the second (one sitting unless the human said otherwise). Done when the thing shows an answer, or the time is up.
3. Report in four lines: what was made, what it shows against the question, the verdict you recommend and why, what the prototype cannot show. A verdict is `yes`, `no`, or `not clear yet` with the next thing worth trying. Then wait for the human's verdict. When the question is one you can check yourself, the third line proposes the verdict and you ask only for a confirmation. Done when the human has stated or confirmed the verdict.
4. Write `notes/YYYY-MM-DD-prototype-<slug>.md` from the template, adding `-2` when the name is taken: `kind: prototype`, the part, Summary is the verdict, Detail is what was tried and the path under `prototypes/`, Copied into names `MAP.md`. Done when the note exists.
5. On the map, rewrite the part's `(prototype) <question>` to `(answered, see notes/<file>) <verdict in a phrase>`. With `not clear yet`, keep the `(prototype)` question and add `, see notes/<file>` after it. Done when the map shows the answer or the pointer.
6. Save as the project's `Saving work` section says: the prototype folder, the note, and `MAP.md` (or the file in `map/` that holds the part); message `prototype <part>: <verdict in a phrase>`. Done when they are saved, or you have said why they are not.
7. Print `Next: /interview-me <part>` as the last line, or `Next: /prototype-it <part>` when the verdict was `not clear yet`.

## Output
- `prototypes/<part>-<slug>/`
- `notes/YYYY-MM-DD-prototype-<slug>.md`
- `MAP.md`: the part's open question now carries the answer, or a pointer to what was tried.
- One save, as the project says.

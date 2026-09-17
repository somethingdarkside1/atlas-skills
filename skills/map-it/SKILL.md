---
name: map-it
description: Check the map, redraw the map diagrams from their sections, set derived statuses, and report drift; or split a sketched part into its own file.
disable-model-invocation: true
---

# Map it

Keep the pictures true to the sections, and give a grown part its own page.

## Read first
- The format comment at the top of `MAP.md`, then `MAP.md` whole: every `##` heading, its `**Status:**` line, its `Needs:` line.
- The format comment at the top of `GLOSSARY.md`, then its entries, and the files in `glossary/` when that folder exists.
- The files in `map/`, when that folder exists.
- Task states, for derived statuses: `grep -rH '^status:' plan --include='[0-9]*.md'`.

## Steps
1. If a home is missing, print `Next: /setup-atlas` and stop. Done when the map is open.
2. Check before drawing, across `MAP.md` and `map/`: a part id used twice; a `Needs:` id with no section; a part that needs itself; a chain of `Needs:` that comes back to where it started. Any of these: print each with the sections involved, change nothing, and end with `Next: /interview-me <part>` for the first part named. Done when the sections are sound.
3. Bare: regenerate the map diagram from the sections, by the rule in the format comment: `flowchart LR`; the four classDef lines; one node per `##` section with id equal to the heading lowercased with dashes, label equal to the heading, class equal to the status; one unlabelled edge per `Needs:` id, from the needed part to the part that needs it; no subgraphs. A map with no parts carries no diagram. Do the same in each `map/<part>.md` from its own sections. Done when the block in each file is replaced and renders.
4. Bare: set the derived statuses, and name each change in the report. A split part's status line from its sub-parts, by the rule in the format comment. A part that reads building while every one of its tasks is done or canceled, with at least one done: set it to done with its node class. Done when the map agrees with the plan.
5. Bare: report what the sections could not fix, one line each: more than nine sections in one file (name the part to split); a term named in a definition or a `_Not_` line that has no entry. Print `No drift.` when there is nothing. Done when the report is printed.
6. With a part id: split it. Only a sketched part with no brief can be split; for any other, print `Splitting a part that has a brief is not supported yet.` and `Next: /atlas`, and stop. Create `map/<part>.md` with `part: <part>` frontmatter, the part's body, one paragraph, its own diagram, and one `##` section per sub-part with status sketched, `Needs:`, and open questions. When the sub-parts were not given, ask for them in one round in the interview format (title, why now, lettered options of one line, `➡️`). Sub-part ids must be unique across the whole map. In `MAP.md` leave the part's status line and `See [map/<part>.md](map/<part>.md).` Done when the part reads the same in both files and every id is unique.
7. Save as the project's `Saving work` section says: only the files you changed; message `map: regenerated` or `map: split <part>`. Done when they are saved, or you have said why they are not.
8. Print `Next: /atlas` as the last line.

## Output
- `MAP.md` and `map/*.md`: diagrams regenerated, derived statuses set, or one new split file.
- A drift report in the terminal.
- One save, as the project says.

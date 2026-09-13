---
name: map-it
description: Redraw the map and glossary diagrams from their sections and report drift, or split a grown part into its own file.
disable-model-invocation: true
---

# Map it

Keep the pictures true to the sections, and give a grown part its own page.

## Read first
- The format comment at the top of `MAP.md`, then `MAP.md` whole: every `##` heading, its `**Status:**` line, its `Needs:` line.
- The format comment at the top of `GLOSSARY.md`, then its entries.
- `map/*.md`, if any exist.

## Steps
1. If `MAP.md` is missing, print `Run /atlas first.` and `Next: /atlas`, and stop. Done when the map is open.
2. Bare: regenerate the map diagram from the sections, exactly as the map's format comment says, in `MAP.md` and in each `map/<part>.md` from its own sections. Done when the block in each file is replaced and renders.
3. Bare: redraw the glossary diagram exactly as the glossary's format comment says. Done when every node is an entry and every entry that names another term has its edge.
4. Bare: report what the sections could not fix, one line each: a `Needs:` id with no section; a part id used twice across `MAP.md` and `map/*.md`; more than nine sections in one file (name the part to split); a term named in a definition or a `_Not_` line that has no entry. Print `No drift.` when there is nothing. Done when the report is printed.
5. With a part id: split it. Create `map/<part>.md` with `part: <part>` frontmatter, the part's body, one paragraph, its own diagram, and one `##` section per sub-part with status sketched, `Needs:`, and open questions. When the sub-parts were not given, ask for them in one round in the interview shape (title, why now, lettered options with costs, `➡️`). Sub-part ids must be unique across the whole map. In `MAP.md` leave the part's status line and `See [map/<part>.md](map/<part>.md).`; `/atlas` recomputes that status from the sub-parts, so a split part reads sketched until its sub-parts are interviewed: split while the part is still sketched where you can. Done when the part reads the same in both files and every id is unique.
6. Commit as `plan/README.md` says: the files you changed; message `map: regenerated` or `map: split <part>`. Done when `git status` shows none of them.
7. Print `Next: /atlas` as the last line.

## Output
- `MAP.md` and `map/*.md`: diagrams regenerated, or one new split file.
- `GLOSSARY.md`: diagram redrawn.
- A drift report in the terminal.
- One commit, in a repo.

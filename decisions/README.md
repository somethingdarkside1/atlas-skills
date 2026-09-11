# Decisions

One short file per choice that is hard to reverse, would surprise a future reader, and came from a real trade-off. If any of the three is missing, it is not a decision, it is a note or a line in the brief.

File name: `NNNN-<slug>.md`, numbered globally, never renumbered. Find the next number by looking at the highest one here.

## Template

```md
# <What was decided, as a full sentence>

**Part:** the map part this belongs to, or "project"
**Date:** YYYY-MM-DD

One to three sentences: the situation, the choice, and why.

Considered: the alternatives worth remembering, one line each. Omit when there were none.
Revisit when: the one change that would reopen this. Omit when nothing plausible would.
```

Add `status: superseded by 0012` as frontmatter when a later decision replaces this one. Leave the file in place; history is the point.

## Index

Kept current by `/interview` and `/map`. The map's part sections link the same files, so browse by part there and by number here.

| No. | Decision | Part | Status |
|---|---|---|---|
| 0001 | Local files are the truth; GitHub is a mirror | side-skills | accepted |
| 0002 | The five things live at the project root | five-things | accepted |
| 0003 | Diagrams are Mermaid inside the Markdown | map-skill | accepted |
| 0004 | Each home carries its own format | five-things | accepted |
| 0005 | One interview skill covers both levels | interview-skill | proposed |
| 0006 | Plain words over engineering jargon | five-things | accepted |

---
name: interview-me
description: Ask rounds of numbered questions until a part is decided, or draft and question the whole map, writing terms, decisions, and the brief as they land.
disable-model-invocation: true
---

# Interview me

Decide one part, or draw the whole project, by asking until nothing is left to guess.

## Read first
- `MAP.md`, whole, format comment first. The part's section is the state you work on; the `Needs:` lines say which parts must be decided before it.
- The format comment at the top of `GLOSSARY.md`, then its entries.
- The part's decisions: `grep -l '^part: <part>' decisions/*.md`, then those files, and the template in `decisions/README.md`.
- `plan/README.md`: the `Tracker:` line and the brief template.

## Steps
1. If `MAP.md` is missing, print `Run /atlas first.` and `Next: /atlas`, and stop. Done when the map is open.
2. Pick the scope. An argument that matches a part id: that part. An argument that matches nothing: add a `##` section for it (status sketched, one purpose line from the argument, `Needs: none.`, open questions to come) and a node in the diagram, then treat it as that part. No argument and the map has parts: list the sketched ones and ask "whole project or which part?". No argument and no parts: the project. A part whose `Needs:` names a part that is not decided: print `<part> needs <x> decided first.` and `Next: /interview-me <x>`, and stop. Done when one part or the project is named and its needs are met.
3. Project only: draft before asking. Look at what exists (the README, top-level folders, existing docs, the conversation) for a draft, not an audit. Write the map's paragraph, one section per part that passes the four tests (one purpose that fits a line; can be briefed once the parts it needs are decided; its status can move alone; a person could be handed it), their `Needs:` lines, the diagram, and the first glossary entries. Done when the map has at least one part and renders.
4. Ask in rounds. Each round opens with `Reply by number; anything you skip takes the ➡️.` and, when the last round had skips, `Taken by default: Qn, Qm.` Each question has a bold title, one line on why it matters now, lettered options one line each with its cost, then `➡️` naming the letter, why it wins, why the others lose, and what it costs. Ask every question whose prerequisites are settled, up to eight; past eight, ask the eight with the most hanging off them and say how many wait. Facts (what is on disk, what a tool reports) you find yourself before asking; decisions are the human's. Project scope goes breadth-first: every part named and given open questions before any is deepened, and nothing decided. Done when the round is posted and you are waiting.
5. While composing, watch the words. When the human's word conflicts with a glossary entry or one of its Avoid synonyms, ask which. When a new word will appear in a part name, the brief, or a task and has no entry, propose the entry. When two words are used for one thing across rounds, ask which. Where an edge between parts or a boundary between two terms is at stake, put one concrete case (a real surface, user, or input) in the question instead of an abstract option. Done when every question in the round rests on words the glossary owns.
6. After each round's answers and before the next round, write what settled. Both scopes: glossary entries (with `_Avoid_`, and `_Not_` when a case showed two terms confusable); the part's open questions in the map's shape (remove the answered, add the surfaced, and put an answer that belongs to another part into that part's open questions); `Needs:` lines; new sketched parts with their nodes. Part scope only: a decision file for each choice that passes the three tests in `decisions/README.md`, `accepted` unless the human said "for now" (`proposed`), and a new superseding file when an answer contradicts an accepted one; a `(answered ...)` question's verdict copied into a decision or kept for the brief, then the line removed. A re-interview asks about the part's `proposed` decisions first. Done when the files show it before the next round appears.
7. When a question can only be answered by making something, write it on the part with the `(prototype)` marker from the map's format, finish the rest of the round, leave the part sketched, and end with `Next: /prototype-it "<question>"`. Done when the map carries the question.
8. Project scope ends when every part has its open questions written and none is missing. Done when no part has an empty open-questions list.
9. Part scope ends when open questions is `none`. Write the brief from the template: with `Tracker: files`, `plan/<part>/brief.md`; with `Tracker: github`, a parent issue labelled `atlas:part` whose body is the brief with full URLs for decision links. Decisions in the brief holds a link per decision file and one line per settled choice too small for a file. Set the status line to `decided` and the node class to `:::decided`; set `Plan:` to the brief file or the issue (`/plan-it` points it at the folder). A decided or building part that was re-interviewed keeps its status and gets its brief rewritten. Redraw the glossary diagram by the rule in its format comment. Done when the brief exists and the part reads decided.
10. Commit as `plan/README.md` says: the files you wrote; message `interview <part>: <what changed>`. Done when `git status` shows none of them.
11. Print the last line: `Next: /plan-it <part>` after a part, `Next: /interview-me <first sketched part in map order whose Needs: are all decided>` after the project, `Next: /prototype-it "<question>"` when one is parked. Done when it is the last line of output.

## Output
- `GLOSSARY.md`: new or changed entries, diagram redrawn.
- `MAP.md`: the part's status, open questions, `Needs:`, `Plan:`, and node class; new sketched parts; on the project, the paragraph and the first diagram.
- `decisions/NNNN-<slug>.md` for each decision.
- `plan/<part>/brief.md`, or a parent issue, when a part is decided.
- One commit, in a repo.

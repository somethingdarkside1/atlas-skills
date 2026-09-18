---
name: interview-me
description: Ask rounds of numbered questions until a part is settled, or draft and question the whole map, writing terms, decisions, and the brief as they land.
disable-model-invocation: true
---

# Interview me

Settle one part, or draw the whole project, by asking until the next work is safe to plan.

## Read first
- `MAP.md`, whole, and the file in `map/` that holds the part when it was split. The part's section is the state you work on; the `Needs:` lines say which parts must be decided before it.
- The part's decisions: `grep -rl '^part: <part>' decisions --include='[0-9]*.md'`, then those files.
- The part's brief, when `plan/<part>/brief.md` exists, and the status lines of its tasks: `grep -rH '^status:' plan/<part> --include='[0-9]*.md'` when that folder exists.
- The newest handoff in `notes/`, when its `Target:` is this part: it holds the round in flight and the answers so far.
- The formats: the brief in `plan/README.md`, the decision in `decisions/README.md`, the entry shape in the comment at the top of `GLOSSARY.md`.

## Steps
1. If a home is missing, print `Next: /setup-atlas` and stop. Done when the map is open.
2. Pick the scope. An argument that matches a part id: that part. An argument that matches nothing: show the closest part ids and ask `New part, or one of these?`; on "new", add a `##` section for it (status sketched, one purpose line from the argument, `Needs: none.`, open questions to come) and a node in the diagram, then treat it as that part. No argument and the map has parts: list the sketched ones and ask "whole project or which part?". No argument and no parts: the project. A part whose `Needs:` name a part that is still sketched: say so, offer that part instead, and go on only when the human says to. Done when one part or the project is named.
3. Project only: draft before asking. Look at what exists (the README, top-level folders, existing docs, the conversation) for a draft, not an audit. Write the map's paragraph, one section per part that passes the four tests (one purpose that fits a line; can be briefed once the parts it needs are decided; its status can move alone; a person could be handed it), their `Needs:` lines, the diagram, and the first glossary entries. Done when the map has at least one part and renders.
4. Ask in rounds. Each round opens with `Reply by number; anything you skip takes the ➡️.` and, when the last round had skips, `Taken by default: Qn, Qm.` Each question has a bold title, one line on why it matters now, lettered options of one line each with the cost inside the line, then `➡️` naming the letter and why in one line. A question whose answer is hard to reverse carries `(your call)` in its title: skipped, it takes no default and comes back in the next round. Ask the frontier (every question whose prerequisites are settled) up to five; past five, ask the five with the most hanging off them and say how many wait. Facts (what is on disk, what a tool reports) you find yourself before asking; decisions are the human's. Project scope goes breadth-first: every part named and given open questions before any is deepened, and nothing decided. Done when the round is posted and you are waiting.
5. While composing, watch the words. When the human's word conflicts with a glossary entry or one of its Avoid synonyms, ask which. When a new word will appear in a part name, the brief, or a task and has no entry, propose the entry. When two words are used for one thing across rounds, ask which. Where an edge between parts or a boundary between two terms is at stake, put one concrete case (a real surface, user, or input) in the question instead of an abstract option. Done when no question in the round rests on a word the glossary does not own.
6. After each batch of answers and before the next round, write what settled: glossary entries (with `_Avoid_`, and `_Not_` when a case showed two terms confusable); a decision file for each choice that passes the three tests in `decisions/README.md`, `accepted` unless the human said "for now" (`proposed`), and a new superseding file when an answer contradicts an accepted one, each linked on the part's `Decisions:` line; the part's open questions (remove the answered, add the surfaced, and put an answer that belongs to another part into that part's open questions); `Needs:` lines; new sketched parts with their nodes. Part scope: from the first batch on, keep `plan/<part>/brief.md` current in the template's headings, so nothing settled lives only in chat. On a sketched part it is a draft, with `Draft: open questions remain on the map.` as the first line under its title; a brief that is already finished is updated in place and gets no draft line. Done when the files show it before the next round appears.
7. When a question can only be answered by making something, write it on the part as `(prototype) <question>`, finish the rest of the frontier, leave the part sketched, and end with `Next: /prototype-it <part>`. Done when the map carries the question.
8. Project scope ends when every part has its open questions written and none is missing. Done when no part has an empty open-questions line.
9. Part scope ends when the next work is safe to plan: every open question is answered, or parked as `(later: <what will settle it>)` because nothing planned now depends on it. Finish the brief and remove its `Draft:` line. Decisions in the brief holds a link per decision file and one line per settled choice too small for a file. Set the status line to `decided` and the node class to `:::decided`; set `Plan:` to the folder. A decided, building, or done part that was re-interviewed keeps its status and gets its brief rewritten; name every task the change touches and say `Next: /plan-it <part>` when any does. Redraw the glossary diagram (an edge from a term to each term its definition names; a node only when it has an edge). Done when the brief exists without a draft line and the part reads decided, or keeps the status it had before a re-interview.
10. Save as the project's `Saving work` section says: only the files you wrote; message `interview <part>: <what changed>`. Done when they are saved, or you have said why they are not.
11. Print the last line. After a part: `Next: /plan-it <part>` when it has no plan yet or the change touches a task, else `Next: /atlas`. After the project: `Next: /interview-me <part>` for the first sketched part in map order none of whose `Needs:` is still sketched. When a question is parked for a prototype: `Next: /prototype-it <part>`. Done when it is the last line of output.

## Output
- `GLOSSARY.md`: new or changed entries, diagram redrawn.
- `MAP.md`: the part's status, open questions, `Needs:`, `Plan:`, and node class; new sketched parts; on the project, the paragraph and the first diagram.
- `decisions/NNNN-<slug>.md` for each decision, linked on the part's `Decisions:` line.
- `plan/<part>/brief.md`: a draft from the first answers on, finished when the part is decided.
- One save, as the project says.

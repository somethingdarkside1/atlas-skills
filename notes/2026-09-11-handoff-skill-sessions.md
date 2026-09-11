---
date: 2026-09-11
kind: handoff
part: project
---

# Handoff: one interview session per skill

## Summary
The structure, vocabulary, formats, and packaging of Atlas are settled and committed. Eight skills remain to be written, each in its own interview session. This note is the brief for those sessions until `/atlas` and `/interview-me` exist to run them.

## Detail

### How to run a session
1. Open a fresh session in this folder.
2. Run Matt Pocock's `/mattpocock-skills:grill-with-docs` (installed as a plugin) and paste the session prompt for the skill below.
3. Answer the rounds. When the frontier is empty, write `skills/<name>/SKILL.md` and `agents/openai.yaml` using the skeleton in `skills/README.md`, run it against a copy of `examples/brand/`, record the result as a note, and move the part on `MAP.md` to done.
4. Add a decision only when the session made a choice that passes the three tests in `decisions/README.md`.

Session prompt: "Read CLAUDE.md, GLOSSARY.md, MAP.md, decisions/, plan/README.md, and skills/README.md. Interview me about the `<name>` part of MAP.md until its open questions are settled and every step of the skill has a done-when condition. Do not write the skill until I confirm."

### Order and what each session must settle
1. **interview-me**: how a round is formatted; how scope (project or part) is chosen; the exact moment a term, map change, or decision is written; when it hands to prototype-it; how it ends (part moves to decided).
2. **map-it**: the layout rules as instructions; when it may run without an interview; how it splits a part into `map/<part>.md`; how it regenerates the diagram from sections and checks node ids against headings.
3. **plan-it**: the brief without user stories for non-software work; how tasks are sized to one session; the granularity quiz; files mode versus GitHub mode (parent issue, sub-issues, dependencies, labels, milestone only when named).
4. **build-it**: how it picks the ready task; how it detects the medium (code, copy, configuration, assets); the three environments (no git, git with files, git with GitHub); branch naming, commit, PR; what it writes under Delivered.
5. **review-it**: the two axes for non-code work; what "conventions" means; where findings go (task section, PR review, or issue comment); the merge line; closing the parent and moving the part to done.
6. **atlas**: the five-line status; scaffold from `skills/atlas/templates/`; the tracker question; `git init` offer; merge recommendation; the checks it runs (decisions without a map link, blockers that name missing tasks); resuming from the newest handoff.
7. **prototype-it**: what "throwaway" means outside code; where the prototype lives; the verdict note; how the answer reaches the interview.
8. **park-it**: what the handoff note must contain; redaction; how `/atlas` recognises it as unread.

### Already settled, do not reopen
Decisions 0001 to 0006, the five things and their formats (`plan/README.md`, `decisions/README.md`, `notes/README.md`, the comments in `GLOSSARY.md` and `MAP.md`), skill names, the `Tracker:` and `Merge:` lines, the versioned `CLAUDE.md` block.

### After all eight
Run `scripts/link-skills.sh`, run `claude plugin validate . --strict`, pilot on a real project, then push to `somethingdarkside1/atlas-skills`. GitHub description: "Map it before you build it. Eight agent skills and five plain-Markdown files that take an idea from fuzzy to finished, in any domain. Inspired by Matt Pocock's skills."

## Copied into
MAP.md (atlas-skill section), skills/README.md.

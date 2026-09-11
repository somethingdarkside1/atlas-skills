<!--
FORMAT. Agents: read this before editing. It is not rendered.
- Level 1: one paragraph on what this thing is and who or what it touches, then the diagram.
- One ## section per part. The heading, lowercased with dashes, is the part id. Diagram node ids must match.
- Each part carries, in this order: **Status:** sketched | decided | building | done. One purpose line. Open questions. Decisions (links). Plan (link to plan/<part>/).
- Seven to nine parts per diagram at most. When a part outgrows a screen, move its body to map/<part>.md and leave the status line and a link.
- Colour by status with the four classes below. Regenerate the diagram from the sections, never the other way round.
-->

# Atlas

Atlas is a set of agent skills plus a file layout (the five things) that take an idea from fuzzy to finished in any domain. It touches a coding agent (Claude Code, Codex, Cursor and others via skills.sh), the project folder it runs in, and optionally GitHub issues.

```mermaid
flowchart TB
  classDef sketched fill:#f4f4f4,stroke:#999,color:#333
  classDef decided fill:#dbeafe,stroke:#2563eb,color:#1e3a8a
  classDef building fill:#fef3c7,stroke:#d97706,color:#78350f
  classDef done fill:#dcfce7,stroke:#16a34a,color:#14532d

  five-things["The five things"]:::decided
  packaging["Packaging and install"]:::sketched
  side-skills["/prototype /handoff /publish"]:::sketched
  subgraph core[Core loop]
    direction LR
    atlas-skill["/atlas"]:::sketched --> interview-skill["/interview"]:::sketched --> map-skill["/map"]:::sketched --> plan-skill["/plan"]:::sketched --> build-skill["/build"]:::sketched --> review-skill["/review"]:::sketched
  end

  five-things --> core
  five-things --> side-skills
  packaging --> core
```

## Five things

**Status:** decided
The file layout every project gets: `GLOSSARY.md`, `MAP.md`, `plan/`, `decisions/`, `notes/`, all at the root, each self-describing.
Open questions: none.
Decisions: [0002](decisions/0002-five-things-at-the-root.md), [0004](decisions/0004-self-describing-files.md), [0006](decisions/0006-plain-words-over-jargon.md).
Plan: none yet.

## Atlas skill

**Status:** sketched
`/atlas` reads the five things and says what to run next. On a fresh project it scaffolds them from templates and writes an eight-line block into `CLAUDE.md` or `AGENTS.md`.
Open questions: final name for the scaffold-and-route skill (`/atlas` folds setup and next). Whether it asks one question when there is no README.
Decisions: none yet.
Plan: none yet.

## Interview skill

**Status:** sketched
`/interview` runs rounds of numbered questions with recommended answers, writing terms, map changes, and decisions as they land. Scope is the whole project or one part.
Open questions: whether one skill handles both the foggy multi-session effort (Matt's wayfinder) and the single-session sharpening. Proposed yes, via the map's zoom.
Decisions: [0005 (proposed)](decisions/0005-one-interview-for-both-levels.md).
Plan: none yet.

## Map skill

**Status:** sketched
`/map` draws or redraws the diagram from the sections, zooms into one part, moves statuses, and splits a grown part into `map/<part>.md`.
Open questions: layout rules to bake in (direction, node limit, status classes). Whether it can run without an interview first.
Decisions: [0003](decisions/0003-mermaid-in-markdown.md).
Plan: none yet.

## Plan skill

**Status:** sketched
`/plan` turns a decided part into `plan/<part>/brief.md` and numbered task files with blocking edges, in one pass, then quizzes the human on granularity.
Open questions: task file fields. Whether the brief needs user stories for non-software projects.
Decisions: [0001](decisions/0001-local-files-are-the-truth.md).
Plan: none yet.

## Build skill

**Status:** sketched
`/build` works one ready task in whatever medium it needs, reading the brief, glossary, and decisions first, then records what it delivered on the task.
Open questions: how it detects the medium (code, copy, configuration, assets). Whether it commits.
Decisions: none yet.
Plan: none yet.

## Review skill

**Status:** sketched
`/review` checks a task's result on two axes: does it match the brief, and does it follow the project's conventions and vocabulary.
Open questions: what "conventions" means for a non-code project. Whether findings go to the task file or a note.
Decisions: none yet.
Plan: none yet.

## Side skills

**Status:** sketched
`/prototype` answers one question with a throwaway thing and files the verdict as a note. `/handoff` pauses into a dated note. `/publish` mirrors the plan to GitHub issues, one way, writing issue numbers back.
Open questions: how `/publish` maps tasks to issues, dependencies, and a Project. Whether PR conventions belong in `/build` or `/publish`.
Decisions: [0001](decisions/0001-local-files-are-the-truth.md).
Plan: none yet.

## Packaging

**Status:** sketched
Flat `skills/<name>/` folders, a Claude plugin manifest, a skills.sh listing, a README that doubles as the docs page, and the blog post.
Open questions: skill name collisions when installed flat next to other sets. Whether to keep Matt's copy vendored in `reference/` on the public repo.
Decisions: none yet.
Plan: none yet.

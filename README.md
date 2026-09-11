# Atlas

**Map it before you build it.** By [Vitali Liouti](https://github.com/somethingdarkside1). A small set of agent skills that take an idea from fuzzy to finished: interview it, map it, plan it, build it, review it. Works for a website, a CRM rollout, a brand system, or a codebase, because the method is the same and the files are plain Markdown.

Inspired by [Matt Pocock's skills](https://www.aihero.dev/skills), reshaped around one idea: everything the agent learns lands in five places you can read, diff, and draw.

> Status: work in progress. The structure is settled; the skills are being written one at a time.

## Install

```bash
npx skills add somethingdarkside1/atlas-skills
```

Claude Code users can also add it as a plugin:

```bash
claude plugin marketplace add somethingdarkside1/atlas-skills
```

## The five things

Run `/atlas` in any project folder and it creates these, each starting with its own format in a hidden comment so the agent always knows how to write it.

| Path | Holds | One-line rule |
|---|---|---|
| `GLOSSARY.md` | The words | One term per concept the project owns, no implementation detail |
| `MAP.md` | The shape | One diagram, one section per part, a status on every part |
| `plan/` | The work | One folder per part: a brief and numbered tasks with blocking edges. Or, if the project chose it, the repo's GitHub issues |
| `decisions/` | The why | One short file per decision that is hard to reverse |
| `notes/` | The dated record | Write once, never edit; anything durable is copied into a home |

If it is true today it lives in one of the first four. If it was true on a date, it is a note.

A project after a few sessions:

```
my-project/
  GLOSSARY.md               the words, with a diagram of how they relate
  MAP.md                    the shape: one diagram, one section per part, a status on each
  plan/
    README.md               where the plan is tracked, and the brief and task templates
    logo-system/
      brief.md
      01-choose-the-mark.md
      02-build-the-lockups.md
  decisions/
    README.md               the format and a numbered index
    0001-one-mark-not-a-family.md
  notes/
    README.md               the note template
    2026-09-14-prototype-mark-in-three-weights.md
```

## How the skills fit together

```mermaid
flowchart LR
  atlas["/atlas<br/>what is next?"]
  interview["/interview-me<br/>ask until settled"]
  map["/map-it<br/>draw and zoom"]
  plan["/plan-it<br/>brief and tasks"]
  build["/build-it<br/>one task"]
  review["/review-it<br/>brief and conventions"]
  prototype["/prototype-it<br/>answer one question"]
  handoff["/park-it<br/>pause to a note"]

  atlas --> interview --> map --> plan --> build --> review --> atlas
  interview -. hard question .-> prototype -.-> interview
  handoff -. any time .-> atlas
```

What each skill writes:

```mermaid
flowchart TB
  subgraph skills[Skills]
    direction LR
    atlas
    interview
    map
    plan
    build
    review
    prototype
    handoff
  end
  subgraph things[The five things]
    direction LR
    G[GLOSSARY.md]
    M[MAP.md]
    P[plan/]
    D[decisions/]
    N[notes/]
  end
  interview --> G & M & D
  map --> M
  plan --> P
  build --> P
  review --> P & N
  prototype --> N
  handoff --> N
  atlas -. reads all five .-> things
```

## The skills

| Skill | What it does | Why it exists |
|---|---|---|
| `/atlas` | Prints five lines (parts by status, ready tasks, newest note, the next command) and says what to run. On a fresh project it creates the five things and asks one question: track the plan in files or in GitHub issues. | You should never have to remember the method |
| `/interview-me` | Asks until a part is settled, writing terms, map changes, and decisions as they land | Sharp thinking before any building |
| `/map-it` | Draws or redraws the map, zooms into one part, moves statuses | The shape stays visible as it fills in |
| `/plan-it` | Turns a decided part into a brief and numbered tasks with blocking edges | Work that fits one session each |
| `/build-it` | Works one task in whatever medium it needs, then records what it delivered | The doing |
| `/review-it` | Checks a task's result against its brief and the project's own conventions | Catches drift before it compounds |
| `/prototype-it` | Makes a throwaway thing that answers one question, files the verdict as a note | Some questions need a runnable answer |
| `/park-it` | Pauses the session into a dated note the next session resumes from | Nothing gets lost in a temp folder |

## A worked example

[`examples/brand/`](examples/brand/) is a small brand project after two sessions: two parts on the map, one decided, three tasks, one decision, one note. Copy its shape, not its content.

## Credits

Inspired by Matt Pocock's [skills](https://github.com/mattpocock/skills), MIT.

## License

MIT. See [LICENSE](LICENSE).

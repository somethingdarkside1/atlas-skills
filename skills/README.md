# Skills

One folder per skill, flat. Each is written after its own interview session (see the newest handoff in `notes/`) and marked on `MAP.md`.

Planned: `atlas`, `interview-me`, `map-it`, `plan-it`, `build-it`, `review-it`, `prototype-it`, `park-it`.

## Skeleton

```
skills/<name>/
  SKILL.md
  agents/openai.yaml
  templates/            only if the skill scaffolds files
```

`SKILL.md`:

```md
---
name: <name>
description: <one line, human-facing, what it does>
disable-model-invocation: true
---

# <Name>

<One sentence: the job.>

## Read first
<Which of the five things to read, and which parts of them. State, not bodies, where possible.>

## Steps
1. <Step.> Done when <observable condition>.
2. ...

## Output
<What changed on disk or on GitHub when this skill finishes, as a list.>
```

`agents/openai.yaml`:

```yaml
interface:
  display_name: "<Name>"
  short_description: "<what it does>"
policy:
  allow_implicit_invocation: false
```

## Checklist before a skill is marked done

- Under about 120 lines, positive instructions only, one job.
- No format restated: the skill points at the file's own format comment or folder README.
- Reads the tracker and merge lines from `plan/README.md` when it touches the plan.
- Works in all three environments: no git, git with files, git with GitHub.
- Run once against `examples/brand/` (copied to a scratch folder) and once against a real project; both results recorded as a note.

# Skills

One folder per skill, flat. All eight were written in one interview session (see the newest handoff in `notes/`) and are marked on `MAP.md`: `atlas`, `interview-me`, `map-it`, `plan-it`, `build-it`, `review-it`, `prototype-it`, `park-it`.

## Skeleton

```
skills/<name>/
  SKILL.md
  agents/openai.yaml
  templates/            only if the skill creates files from templates
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

- As short as the job allows, positive instructions only, one job.
- Step 1 stops with `Run /atlas first.` when a file it needs is missing; every failure is one line naming the fix; the last line is `Next: /command <id>`.
- No format restated: the skill points at the file's own format comment or folder README.
- Reads the tracker and merge lines from `plan/README.md` when it touches the plan.
- Works in both modes: `Tracker: files` (in place, commit when the folder is a git repo) and `Tracker: github` (branch and PR from `/build-it` only).
- Run once against `examples/brand/` (copied to a scratch folder) and once against a real project; both results recorded as a note. Pending for all eight as of 2026-09-11.

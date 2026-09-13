# Skills

One folder per skill, flat: `atlas`, `interview-me`, `map-it`, `plan-it`, `build-it`, `review-it`, `prototype-it`, `park-it`. Each is marked on `MAP.md`.

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
<Which of the five things to read, and which parts of them. State, not bodies, where possible. Always the format comment of every file the skill edits.>

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

## Shapes every skill shares

These are the only rules that live here. Everything about the five things lives in the five things, and everything about git and the tracker lives in `plan/README.md`.

- **Step 1.** `If MAP.md is missing, print Run /atlas first. and Next: /atlas, and stop.` The same check in every skill except `/atlas`, which creates the five things together, so one file stands for all.
- **The last line.** Exactly `Next: /<command>` or `Next: /<command> <id>`, alone on the last line. A stop prints one reason line, then the Next line, and nothing after it. `/atlas` and a handoff note both parse this line, so it has one shape.
- **The commit step.** `Commit as plan/README.md says: <the files>; message <skill> <id>: <what>.` The environment rules (no repo, a repo, a GitHub tracker) are in that file's Git section and are quoted nowhere else.
- **Waits are on disk.** A skill that needs a person writes the state where the next run will find it (a task status, an open question on the map, a note) and ends with a Next line. Rounds (in `/interview-me`, `/plan-it`, `/map-it`, `/atlas` on a fresh folder) and the verdict in `/prototype-it` are conversations by design and are the only places a skill waits in chat.
- **Rounds.** The round shape is defined once, in `/interview-me` step 4. Other skills say "one round in the interview shape" and list its parts in a phrase.
- **Ids.** A task id is the shape `plan/README.md` gives it, everywhere.
- **Precedence.** When a skill and a home disagree, the home wins and the skill is wrong; fix the skill.
- **`/atlas go`.** Runs `/build-it` and `/review-it` by opening the `SKILL.md` in the sibling folder of that name and following it. Skills are installed as siblings by skills.sh, by the plugin, and by `scripts/link-skills.sh`, so the path holds.
- **Statuses have one owner.** `/interview-me` moves sketched to decided; `/build-it` moves decided to building and todo to doing to review; `/review-it` moves review to doing or done, and building to done; `/atlas` repairs derived and swept statuses; `/map-it` moves none.

## Checklist before a skill is marked done

- As short as the job allows, one job, positive by default with at most one boundary per step.
- Step 1 (every skill but `/atlas`), the last line, and the commit step use the shapes above, word for word.
- Points at the home for every format and rule; quotes none.
- Reads the format comment of every file it edits.
- Reads the tracker and merge lines from `plan/README.md` when it touches the plan, and works in both trackers.
- Run once against `examples/brand/` (copied to a scratch folder) and once against a real project; both results recorded as a note.

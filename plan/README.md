# Plan

Tracker: files

This is the active plan for the first public Atlas revision. Seven work packages own the work, each mapped to a part in [MAP.md](../MAP.md), with one brief and numbered tasks in a flat part folder. Under [decision 0021](../decisions/0021-patch-the-draft-first.md) the draft skills are patched first ([work-skills/06](work-skills/06-patch-the-draft.md)) and migration follows the skills. The prior 23-task plan is [archived](../notes/archive/2026-09-13-initial-review/README.md), and [MIGRATION.md](MIGRATION.md) accounts for every old task.

## Pick work

Use [PROMPTS.md](PROMPTS.md) for standalone package and continuation prompts. [COORDINATION.md](COORDINATION.md) links the GitHub package issues; they point to this plan and do not replace local task state. Reference a package issue from task PRs with `Refs`; close it only when the adopted package outcome is demonstrated.

| Package | First task | Result |
|---|---|---|
| [Core model](core-model/brief.md) | [01](core-model/01-settle-boundaries.md) | Adopt boundaries, evidence and migration |
| [Shared methods](shared-methods/brief.md) | [01](shared-methods/01-interview-and-model.md) | Interview, diagnose, verify, and prototype consistently |
| [Project setup](project-setup/brief.md) | [01](project-setup/01-settle-adoption-contract.md) | Adopt context and project-owned policy safely |
| [Work skills](work-skills/brief.md) | [06](work-skills/06-patch-the-draft.md) | Patch the draft, then implement the revised operation contracts |
| [Context routing](context-routing/brief.md) | [01](context-routing/01-resolve-focus-pointers.md) | Find relevant evidence with bounded, expandable reads |
| [Validation](validation/brief.md) | [01](validation/01-check-structural-contracts.md) | Demonstrate structural and behavioral correctness |
| [Public release](public-release/brief.md) | [01](public-release/01-write-public-guide-and-credit.md) | Document, install, and publish a verified release |

Task blockers are the execution order. The table is a directory, not a claim that every first task is ready. The adopted boundaries are in `core-model/01`; task 02 is the next core-model task once 01 has accepted evidence accessible to the attempt. Method tasks and some policy/documentation tasks can run independently once their blockers are done. Each package brief contains an interview start prompt, read scope, ownership, completion criterion, and unresolved choices.

Use the current project instructions and package prompts for work on this repository. The source Atlas skills are being migrated and are exercised in scratch fixtures; their older tracker and Git rules do not redefine this active plan.

## Work format for this repository

A brief has `part: <part-id>` frontmatter and Problem, Outcome, Decisions, and Out of scope sections. Decisions may include nested start prompts, open choices, scope, and task links for this work package. A planning brief can exist while a part is sketched; the decision task records when its direction is adopted.

A task file is `plan/<part>/NN-<slug>.md`. Its frontmatter has `status`, `kind`, and `blocked_by`. `kind` is `decision`, `build`, `check`, or `release`. Its sections are Delivers, Check by, Done when, Delivered, and Review in that order. Every acceptance item names observable evidence. Task ids are `<part>/<NN>`; local blockers may shorten that to `NN`. Quote ids in the blocker list. Keep numbers reserved when work is canceled or moved.

| State | Meaning in this plan |
|---|---|
| todo | Eligible to select after all blockers are accepted and their outputs are accessible |
| doing | An identified task attempt is in progress or has a recorded unresolved action |
| review | A delivered output awaits acceptance against its current scope |
| done | Required evidence and judgments support acceptance of the named output |
| canceled | Work was removed with its reason and incoming dependencies accounted for |

Read full task bodies when editing their meaning. Apply the [accepted evidence and dependency principles](../decisions/0019-acceptance-follows-output-and-scope.md) when canceling work or changing an artifact or brief. A repeated operation finds the existing task and output. Record the concrete workspace/branch and pending action in Delivered when work is interrupted. Review names the examined output and scope revision, checks, findings or acceptance, and outstanding human judgments.

The core-model package defines the distributable task contract and its migration. These repository planning conventions support doing that work; they are not a claim that the earlier source templates already implement it.

## Work and project workflow

[AGENTS.md](../AGENTS.md) owns this repository's commit, branch, worktree, push, PR, and merge instructions. Atlas work acceptance is distinct from integration. A task can explicitly deliver a merge or publication, in which case that outcome is part of its own acceptance. A dependent task also needs access to the exact accepted output it consumes.

## Complete a task

Read its brief and blockers, settle only unresolved material choices, and record the current attempt. Make the stated output, run its checks, and record evidence and limits. Review that output against the current brief, resolve findings, and update the task's accepted state. Then follow the separately authorized project workflow. Record an external delivery failure as such without silently changing the quality result or claiming integration succeeded.

Run `python3 scripts/check-project.py` after changing the active plan. Update the map when a package's adopted direction or progress changes. Keep historical plans and dated evidence out of active selection.

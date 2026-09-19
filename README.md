# Atlas

**Keep the work understandable.** By **[Vitali Liouti](https://github.com/somethingdarkside1)**.

Atlas is a project method implemented through nine agent skills. It connects scope, choices, tasks, results, and evidence in plain Markdown, so another session can find the work and continue it. Use the same organising method for software, research, documents, design, or an operational project, with checks suited to the actual medium.

Start with the **[simple guide](GUIDE.md)**. It explains the process, every skill, how to organise a project, and what happens when work changes or gets stuck. The [actual skill contracts](skills/README.md) are for authors and reviewers.

> **Status: development candidate, not a tagged release.** The operation set and format-3 templates have been revised under [work-skills/07](plan/work-skills/07-integrated-process-candidate.md). Its evidence distinguishes structural checks and isolated runs from supported host installation, the deferred human acceptance run, and public release. Package metadata remains at the existing 0.2.0 development version pending the release task's version choice.

## The normal route

Set up once, clarify only what is uncertain, plan the smallest useful work, build a task, then review it separately. A clear task under a settled brief can skip the interview. `/atlas` recommends the next useful action; it does not run a chain of commands.

| Skill | Purpose |
|---|---|
| `/setup-atlas` | Adopt a new or existing project without losing its work or delivery rules |
| `/atlas` | Inspect selected work and recommend an action or explain a wait |
| `/interview-me` | Resolve material uncertainty and record the brief and choices |
| `/plan-it` | Create or revise verifiable tasks with stable ids and real blockers |
| `/build-it` | Deliver or resume one task, check it, and record the result |
| `/review-it` | Assess the actual result and scope; record findings or acceptance |
| `/map-it` | Maintain responsibilities, views, and links without inventing completion |
| `/prototype-it` | Run a bounded experiment and record what it establishes |
| `/park-it` | Preserve missing context and exact pointers for resumption |

## Five homes

`GLOSSARY.md` owns project meanings. `MAP.md` owns responsibilities and decision prerequisites. `plan/` owns briefs, tasks, attempts, and acceptance. `decisions/` owns consequential choices and their rationale. `notes/` holds dated evidence and handoffs. The deliverable itself lives where the project needs it.

A part groups a meaningful responsibility or outcome. Its id remains stable when its display name or view changes. The map links to the work; it does not duplicate task state. A part becomes done only when the combined result satisfies its brief.

Atlas follows project instructions for saving, commits, branches, sharing, merges, and publication. A clean review does not grant new delivery permission.

## Installation and compatibility

The existing development installation routes are:

```bash
npx skills add somethingdarkside1/atlas-skills
claude plugin marketplace add somethingdarkside1/atlas-skills
claude plugin install atlas-skills@atlas-skills
```

Claude plugin names may be namespaced, such as `/atlas-skills:atlas`; use the installed names. [Clean-profile installation](plan/public-release/02-verify-installation-matrix.md) remains a release requirement. Generated method references are included in consumer folders and checked locally; that alone does not establish host-level installation support.

Existing projects keep their current records until `/setup-atlas` explicitly adopts the candidate formats. See [migration guidance](skills/setup-atlas/MIGRATION.md). Hosted task authority is not silently converted into local files. The full package is the default; selective installation depends on an already adopted project and the required templates/resources.

## Examples and development

[examples/brand/](examples/brand/) is the preserved earlier teaching fixture, including intentionally missing outputs. Copy it before a run; it is useful for migration and recovery rather than a clean candidate acceptance result. Candidate fixtures and observations are described in the [validation record](plan/work-skills/07-integrated-process-candidate.md).

[INDEX.md](INDEX.md) routes repository work to its brief and tasks. [AGENTS.md](AGENTS.md) owns delivery policy, and [the active plan](plan/README.md) retains the release obligations.

```bash
python3 scripts/check-project.py
python3 scripts/bundle-methods.py --check
python3 scripts/test-evidence.py
python3 scripts/test-packaging.py
```

These checks do not prove agent behavior. Run meaningful isolated scenarios when an instruction changes, then record the actual results and limits.

## Research and credit

- [Atlas and Matt: the segmented comparison](notes/2026-09-19-research-atlas-matt-segmented-framework.md)
- [Simplicity and finalisation](notes/2026-09-19-research-matt-simplicity.md)
- [First agent run of the 0.2 draft](notes/2026-09-18-review-first-agent-run-of-0-2.md)

Atlas is authored by Vitali Liouti, with inspiration and attributed adaptations from [Matt Pocock's skills](https://github.com/mattpocock/skills). Shared method sources and generated copies retain the required attribution and MIT notices. Original Atlas work remains identified as such.

MIT. See [LICENSE](LICENSE).

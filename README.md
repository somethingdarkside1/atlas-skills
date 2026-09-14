# Atlas

**Keep the project understandable across sessions.** Atlas is an integrated project method by **[Vitali Liouti](https://github.com/somethingdarkside1)**, implemented through modular skills. Five plain-Markdown homes keep the words, shape, work, reasons, and dated record together.

**Public development status:** the repository contains eight draft skills and the plan for their next revision. The revised operations, separate setup, and reusable method bundles are work in progress. This public source is a development plan; a validated tagged release has separate acceptance gates.

## The direction

Atlas operations create and assess work. Shared interviewing, diagnosis, verification, and prototype methods supply the reasoning. Project instructions own commits, branches, worktrees, pushes, PRs, and merges.

The adopted first-revision direction keeps briefs and tasks in local files. A project can use GitHub for source, PRs, and issue links for coordination under its own delivery policy. Native GitHub task tracking and automatic cross-skill continuation are deferred while the local lifecycle is established and tested.

The product direction is a coherent full-package experience with modular operations and methods loaded when needed. Clear small work can use one task under an existing brief; installation claims, including selective installation, depend on the release checks. See the [product decision](decisions/0018-one-method-modular-skills.md).

| Home | Purpose |
|---|---|
| `GLOSSARY.md` | Project words and useful distinctions |
| `MAP.md` | Parts, their shape, and decision dependencies |
| `plan/` | Briefs, tasks, blockers, delivery evidence, and review |
| `decisions/` | Consequential choices and their rationale |
| `notes/` | Dated observations, experiments, and handoffs |

A method produces useful reasoning or evidence. An operation owns the corresponding state change. Review establishes acceptance of a specific result; the project workflow governs its integration. These boundaries let the same method serve a code repository, a design project, or a folder without Git.

## Finalize the framework

Start at **[INDEX.md](INDEX.md)**. It routes a focus to the appropriate brief and authoritative files. The **[active plan](plan/README.md)** has seven work packages and 24 tasks:

1. **Core model:** settle boundaries, task evidence, and migration.
2. **Shared methods:** author interviewing, diagnosis, verification, and prototyping once.
3. **Project setup:** adopt existing context and project-owned policy safely.
4. **Work skills:** give all eight operations clear reads, changes, finish, and recovery.
5. **Context routing:** use bounded, expandable reads and measure their cost.
6. **Validation:** prove normal and failure paths with real artifacts and fresh contexts.
7. **Public release:** document, package, install, and publish the verified revision.

Read the adopted boundaries in [core-model/01](plan/core-model/01-settle-boundaries.md), then select eligible work from the local task states. Copy a package starter from [the agent prompts](plan/PROMPTS.md) and use [the package issues](plan/COORDINATION.md) to coordinate PRs. Each package includes a concrete interview start prompt, unresolved choices, owned files, dependencies, and acceptance criteria. The earlier plan is [preserved and mapped](plan/MIGRATION.md), including the deferred GitHub work.

## Read the analysis

- [Architecture, reusable methods, and project-policy review](notes/2026-09-13-review-methods-and-project-policy.md)
- [Primary-source research on methods, packaging, and focused reads](notes/2026-09-13-research-methods-and-delivery.md)
- [Initial framework review: 28 finding groups and every skill](notes/2026-09-13-review-atlas-framework.md)
- [What to learn from Matt Pocock, and where his framework also has gaps](notes/2026-09-13-research-matt-pocock-comparison.md)

The proposed advantage is a reliable shared work record, medium-appropriate methods, and recoverable transitions between sessions. The validation package must establish that advantage through observed outcomes. A smaller instruction file or a directory of labels alone does not prove lower cost or better work.

## Development and installation

Read [AGENTS.md](AGENTS.md) for this repository's delivery policy and [skills/README.md](skills/README.md) before changing a skill. Run:

```bash
python3 scripts/check-project.py
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
bash -n scripts/link-skills.sh
```

The existing `0.1.0` manifests package the earlier draft. For deliberate draft evaluation in a scratch project, the repository installation paths are:

```bash
npx skills add somethingdarkside1/atlas-skills
claude plugin marketplace add somethingdarkside1/atlas-skills
claude plugin install atlas-skills@atlas-skills
```

Claude plugin commands use names such as `/atlas-skills:atlas`. Marketplace registration and plugin installation are separate actions; see [the official installation guide](https://code.claude.com/docs/en/discover-plugins). Clean-profile installation and all advertised invocation paths remain [release work](plan/public-release/02-verify-installation-matrix.md). The draft's explicit-only metadata conflicts with its automatic `go` instructions; the revised release plan keeps routing manual until that boundary is tested.

## Credit and license

Atlas is authored and published by Vitali Liouti, with inspiration from [Matt Pocock's skills](https://github.com/mattpocock/skills). The comparison notes identify the mechanisms being considered. Adapted source retains its required attribution and notices; original Atlas work remains identified as such.

MIT. See [LICENSE](LICENSE).

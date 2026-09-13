# Decisions

A decision records a consequential choice with its rationale and the alternatives that matter. A choice can deserve a decision because it is hard to reverse, material in impact, or surprising without context. Keep ordinary reversible choices in the brief.

## Format

Files are `NNNN-<slug>.md`, globally numbered and retained. Frontmatter has `part`, `date`, and `status: proposed | accepted | superseded`; a superseded decision also names `superseded_by`. Use a sentence title and one to three body sentences, with optional one-line Considered and Revisit when entries. A proposed decision guides discussion and becomes authoritative after its adoption is recorded.

## Current proposal index

| Decision | Owner | Subject |
|---|---|---|
| [0012](0012-atlas-owns-work-projects-own-delivery.md) | core-model | Work, reasoning, and project workflow have separate owners |
| [0013](0013-local-tasks-first.md) | core-model | Local task files for the first public revision |
| [0014](0014-shared-methods-travel-with-consumers.md) | shared-methods | Author once and bundle required method references |
| [0015](0015-setup-adopts-routing-observes.md) | project-setup | Separate adoption and read-only routing |
| [0016](0016-pointers-before-label-taxonomy.md) | context-routing | Focus through resolvable pointers before adding labels |
| [0017](0017-evidence-before-release.md) | public-release | Public source and validated release are distinct milestones |

The [core-model decision task](../plan/core-model/01-settle-boundaries.md) settles these proposed defaults. Existing decisions 0001 through 0008 describe the earlier source method and remain historical constraints until a selected revision explicitly supersedes them. Their original part ids resolve through the table below for current work ownership.

| Historical part | Current owner |
|---|---|
| five-things | core-model |
| atlas-skill | project-setup and work-skills |
| interview-skill | shared-methods and work-skills |
| map-skill | context-routing and work-skills |
| plan-skill | core-model and work-skills |
| build-skill | work-skills and project-setup |
| review-skill | work-skills and validation |
| side-skills | shared-methods and work-skills |
| packaging | public-release |

Numbers 0009, 0010, and 0011 are reserved for the prior second-pass branch, preserved as `codex/second-pass-reference`. They cover task ids, durable waiting/review, and precedence of homes. Review their intent during migration; the branch is reference material rather than current runtime support. The next new decision after this proposal set is 0018.

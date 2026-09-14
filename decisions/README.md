# Decisions

A decision records a consequential choice with its rationale and the alternatives that matter. A choice can deserve a decision because it is hard to reverse, material in impact, or surprising without context. Keep ordinary reversible choices in the brief.

## Format

Files are `NNNN-<slug>.md`, globally numbered and retained. Frontmatter has `part`, `date`, and `status: proposed | accepted | superseded`; a superseded decision also names `superseded_by`. Use a sentence title and one to three body sentences, with optional one-line Considered and Revisit when entries. A proposed decision guides discussion and becomes authoritative after its adoption is recorded.

## Current release decisions

| Decision | Owner | Subject |
|---|---|---|
| [0012](0012-atlas-owns-work-projects-own-delivery.md) | core-model | Work, reasoning, and project workflow have separate owners |
| [0013](0013-local-tasks-first.md) | core-model | Local task files for the first public revision |
| [0014](0014-shared-methods-travel-with-consumers.md) | shared-methods | Author once and bundle required method references |
| [0015](0015-setup-adopts-routing-observes.md) | project-setup | Separate adoption and read-only routing |
| [0016](0016-pointers-before-label-taxonomy.md) | context-routing | Focus through resolvable pointers before adding labels |
| [0017](0017-evidence-before-release.md) | public-release | Public source and validated release are distinct milestones |
| [0018](0018-one-method-modular-skills.md) | core-model | An integrated product with modular operations |
| [0019](0019-acceptance-follows-output-and-scope.md) | core-model | Exact evidence, affected acceptance, and accessible dependencies |
| [0020](0020-decide-only-the-selected-scope.md) | core-model | Bounded interviews and adopted scope |

The [core-model decision task](../plan/core-model/01-settle-boundaries.md) records adoption on 2026-09-15 and links the rationale and worked examples. Decisions 0012 and 0013 supersede 0007 and 0001 for the revised release; 0020 replaces the exhaustive stopping rule in 0005 and existence-as-adoption rule in 0008 while retaining their interview and brief ownership. Historical bodies and ids remain available, other earlier decisions remain applicable, and executable source migration is still pending. Original part ids resolve through the table below for current work ownership.

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

Numbers 0009, 0010, and 0011 are reserved for the prior second-pass branch, preserved as `codex/second-pass-reference`. They cover task ids, durable waiting/review, and precedence of homes. Review their intent during migration; the branch is reference material rather than current runtime support. The next new decision is 0021.

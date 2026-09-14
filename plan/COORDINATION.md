# GitHub package coordination

The seven issues below coordinate discussion and PRs for the existing work packages. Local briefs and task files remain the authority for scope, blockers, evidence, and progress. Issue creation does not begin implementation or accept a proposed decision.

| Package | GitHub issue | Current brief | Prompt |
|---|---|---|---|
| core-model | [#2: Settle Atlas work, evidence, and project-workflow boundaries](https://github.com/somethingdarkside1/atlas-skills/issues/2) | [Brief](core-model/brief.md) | [Start](PROMPTS.md#core-model) |
| shared-methods | [#3: Build reusable interview, diagnosis, verification, and prototype methods](https://github.com/somethingdarkside1/atlas-skills/issues/3) | [Brief](shared-methods/brief.md) | [Start](PROMPTS.md#shared-methods) |
| project-setup | [#4: Adopt projects with a separate setup-atlas operation](https://github.com/somethingdarkside1/atlas-skills/issues/4) | [Brief](project-setup/brief.md) | [Start](PROMPTS.md#project-setup) |
| work-skills | [#5: Refine the eight Atlas operation contracts](https://github.com/somethingdarkside1/atlas-skills/issues/5) | [Brief](work-skills/brief.md) | [Start](PROMPTS.md#work-skills) |
| context-routing | [#6: Implement and measure focused context routing](https://github.com/somethingdarkside1/atlas-skills/issues/6) | [Brief](context-routing/brief.md) | [Start](PROMPTS.md#context-routing) |
| validation | [#7: Prove the revised Atlas workflow with independent evidence](https://github.com/somethingdarkside1/atlas-skills/issues/7) | [Brief](validation/brief.md) | [Start](PROMPTS.md#validation) |
| public-release | [#8: Document, install, and publish the verified Atlas release](https://github.com/somethingdarkside1/atlas-skills/issues/8) | [Brief](public-release/brief.md) | [Start](PROMPTS.md#public-release) |

## Use the right dependency level

Select work by the current task `blocked_by` fields and the availability of accepted outputs. Package issues deliberately have no package-wide blocking graph: a package can start early work while another task in that package waits on a later integration. Treat the dependency tables in issue bodies as creation-time navigation snapshots.

Run `python3 scripts/check-project.py` for current structural readiness, then inspect actual blocker evidence. Start with `core-model/01` if still unresolved. Opening these issues does not change any local task state.

## PR and issue lifecycle

Use a focused PR for an implemented task or coherent accepted slice. Link it with `Refs #<package issue>` so merging one task does not close the whole package. Reuse the existing task branch and PR when resuming work. Record implementation progress and acceptance in the local task; use issue discussion for coordination and pointers to evidence.

Close a package issue when the adopted scope's required tasks have accepted evidence, the brief's overall outcome is demonstrated, and integration required by the project is verified. Record removed scope and repaired dependencies in the local plan. Keep the issue open for partial delivery or pending acceptance. A release issue closes only after its public-release evidence is complete.

The prompts documentation PR delivers these entry points and links. Implementation PRs are created when they have actual changes to review. [PROMPTS.md](PROMPTS.md) includes separate task, resume, review/integration, and release instructions.

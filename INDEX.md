# Start here

For using Atlas, read [the simple guide](GUIDE.md). This is a directory of repository context pointers. Current state belongs to the five things; the rows here route to it. Read the brief and one task for the selected part, then expand only where their dependencies or the actual change require it.

| Focus | Use when | Read next |
|---|---|---|
| Orientation | Starting a session or selecting work | [Map](MAP.md), [active plan](plan/README.md) |
| Core model | Changing task states, evidence, completion, or ownership | [Core model brief](plan/core-model/brief.md), [glossary](GLOSSARY.md) |
| Shared methods | Improving interviewing, diagnosis, verification, or experiments | [Shared methods brief](plan/shared-methods/brief.md) |
| Project setup | Adopting an existing project or defining the delivery boundary | [Project setup brief](plan/project-setup/brief.md), [project instructions](AGENTS.md) |
| Work skills | Changing a skill's reads, writes, finish, or recovery behavior | [Work skills brief](plan/work-skills/brief.md), [skill authoring](skills/README.md) |
| Context routing | Changing discovery, labels, split parts, or read scope | [Context routing brief](plan/context-routing/brief.md) |
| Validation | Testing lifecycle, methods, installation, or context cost | [Validation brief](plan/validation/brief.md) |
| Public release | Preparing public documentation, packaging, credit, or a release | [Public release brief](plan/public-release/brief.md) |
| Design rationale | Comparing delivery ownership and reusable methods | [Architecture review](notes/2026-09-13-review-methods-and-project-policy.md) |
| Earlier work | Tracing the 28 findings or the unmerged second pass | [Initial review](notes/2026-09-13-review-atlas-framework.md), [migration table](plan/MIGRATION.md) |

## Expand the scope when evidence requires it

Follow a task's blockers, changed interfaces, accepted decisions, and applicable nested project instructions. Include both sides of an affected boundary. A focus label helps find an entry point; it never authorizes ignoring relevant evidence or project policy. For an unknown area, inspect the map and the nearest relevant files before adding another label.

## Start a work package

Use [the copy-and-paste prompts](plan/PROMPTS.md) to start, resume, or review work. [Package issues](plan/COORDINATION.md) coordinate GitHub discussion and PRs while local tasks own progress.

Open its brief and first eligible task. Use the brief's start prompt to settle its unresolved choices through concrete examples. Record decisions and update task acceptance before implementation when the package calls for an interview. Existing user answers and accepted decisions count; ask only about remaining material uncertainty.

The skill sources are the integrated process candidate under [work-skills/07](plan/work-skills/07-integrated-process-candidate.md), built on the 0.2 patch. Work on this repository from its current project instructions and package briefs, and exercise evolving Atlas skills in scratch fixtures until their contracts pass validation.

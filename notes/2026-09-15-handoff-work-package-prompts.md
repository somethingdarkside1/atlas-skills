---
date: 2026-09-15
kind: handoff
part: project
---

# Work-package issues and agent prompts

## Summary
Seven GitHub package coordination issues now point to the active local plan, and eleven standalone prompts cover starting packages, selecting a task, resuming work, reviewing/integrating a PR, and publishing a verified release. The local task files remain authoritative and their states are unchanged. Start with core-model/01 using the core-model prompt if that decision task is still unresolved.

## Detail

Use [PROMPTS.md](../plan/PROMPTS.md) for copy-and-paste instructions and [COORDINATION.md](../plan/COORDINATION.md) for issues #2 through #8. Each issue embeds its package prompt and links all current local tasks. Task dependencies remain in files, since whole-package issue dependencies would block work that can start earlier.

The prompts branch is `codex/atlas-work-prompts`. Package starters prepare one task's PR; the separate integration and release prompts carry their respective scoped authorization when invoked. Reference a package issue with `Refs` for partial work. A package issue closes only when its full adopted outcome and required integration have evidence.

Validation covers the project checker, eleven complete prompt blocks, seven package-to-issue mappings, issue readback, and links to all 24 active tasks. No skill implementation, task acceptance, behavioral evaluation, or tagged release is claimed by this documentation change. Existing proposed decisions remain proposed. The prompts PR and GitHub merge state provide the authoritative delivery record for these files.

## Copied into

[PROMPTS.md](../plan/PROMPTS.md), [COORDINATION.md](../plan/COORDINATION.md), [plan/README.md](../plan/README.md), [INDEX.md](../INDEX.md), and [README.md](../README.md).

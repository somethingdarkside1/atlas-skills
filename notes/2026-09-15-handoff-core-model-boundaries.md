---
date: 2026-09-15
kind: handoff
part: core-model
---

# Core boundary interview awaiting answers

## Summary
Selected core-model/01, which had no blockers or previous local attempt. Three user choices remain pending; decisions 0012 through 0017 remain proposed. This note preserves a design walkthrough, not behavioral validation or accepted policy.

## Detail

Resume in `/Users/vitali/Documents/Projects/Skills Po` on `codex/core-model-01-boundaries`, based on `f3e9e7ceb5942ae69ca9efd1f04927f62dca61a5`. Initial worktree and index were clean, no merge was active, and fetched main matched. The package [issue #2](https://github.com/somethingdarkside1/atlas-skills/issues/2) had no comments and the repository had no open PRs.

Read the current instructions, index, map, plan format, core brief and all three core tasks, glossary clusters, decisions 0012 through 0017, historical decisions 0001 through 0008, applicable initial findings, architecture review, and affected package briefs. Historical decisions 0001 and 0007 conflict with the proposed local-first and project-owned workflow directions; an adopted replacement must explicitly account for that scope while retaining history. Detailed contracts and migrations belong to tasks 02 and 03.

### Proposed scenario results

| Case | Operation completion and acceptance | Integration, readiness, and authorization |
|---|---|---|
| Code PR passes review but a maintainer owns merge | Build can finish with identified output and checks. Review can finish with acceptance or findings. Acceptance can complete for a task delivering the reviewed change. | Merge stays pending. A dependent task needs access to the accepted revision in a project-permitted workspace. A conflict resolution changes the output and requires affected checks and acceptance to be reassessed. |
| Prepared PDF passes checks but has not reached its recipient | A task promising a prepared PDF can be accepted. A task promising recipient receipt still lacks required evidence. | Sending is a separate authorized action unless explicitly part of the task outcome. Changing English-only scope to bilingual affects acceptance; the English review remains historical evidence. |
| Non-Git prototype produces inconclusive observations | An experiment task can meet its criteria by recording observations and limits. An unresolved preference cannot be recorded as a settled decision. | No Git action is invented. Preserve an exact output and scope identity. A mutable filename or date alone does not distinguish two deliveries or support fresh review. |

A method supplies reasoning and observations; its calling operation owns persistence and task transitions. An index pointer locates a home; it cannot grant authorization or override that home's evidence. These are proposed interpretations for the interview.

### Pending choices

1. Adopt decisions 0012 through 0017 as proposed, or identify revisions or deferrals: separate work and delivery ownership, local task files, bundled shared methods, separate setup and read-only routing, pointers before labels, and evidence before tagged release.
2. Require retrievable exact output and scope identity with Git or a preserved non-Git snapshot/version and content hash, and permit dependent work before integration when accepted output is accessible and project policy permits it. The alternative offered requires integration first. Task 02 owns the exact fields.
3. Reassess affected acceptance after scope changes, preserve prior reviews, and record an impact assessment for harmless edits. A canceled blocker leaves dependent work blocked until explicit dependency replacement or removal with scope rationale. The alternative offered reassesses every accepted task after any brief change.

No answer or adoption is inferred from elapsed time. After answers, record actual choices, rationale, and scope in the current decision and glossary homes, update relevant briefs, verify all four task criteria, and run `python3 scripts/check-project.py`. Commit, push, and open a focused PR with `Refs #2`; the current request requires separate authorization for merge or release. Do not start task 02 or 03 without the user's selection or continuation instruction.

## Copied into

[core-model/01](../plan/core-model/01-settle-boundaries.md) records the current attempt and pending acceptance. No durable design choice has been adopted.

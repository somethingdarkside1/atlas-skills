---
status: review
kind: decision
blocked_by: []
---

# 01: Settle the release boundaries

## Delivers
An adopted decision set for the first public revision and a worked acceptance/integration example.

Source: New architecture review; original F09, F12, F14, F17, F24. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
(you) Settle the remaining choices using the scenarios below, then record the accepted decisions.

## Done when
- [x] Use a code PR, a document delivery, and a non-Git prototype to test the proposed ownership boundary.
- [x] Record which of decisions 0012 through 0017 are accepted, revised, or deferred, using prior user answers as settled input.
- [x] Resolve the four material distinctions: work vs delivery, acceptance vs integration, method vs operation, pointer vs authority.
- [x] Update the relevant briefs and glossary so dependent tasks can proceed without reopening settled choices.

## Delivered
Attempt started 2026-09-15 in `/Users/vitali/Documents/Projects/Skills Po`, branch `codex/core-model-01-boundaries`, from `f3e9e7ceb5942ae69ca9efd1f04927f62dca61a5`. The checkout and index were clean, no merge was active, and fetched `origin/main` matched the starting revision. Package issue #2 had no answers and no open PR existed.

The user authorized proceeding after the recommendations and GitHub/product questions. The [adoption record](../../notes/2026-09-15-review-core-model-adoption.md) records the delegated choices, rationale, exact supersession scope, and worked code PR, PDF, and non-Git prototype cases. Decisions 0012 through 0017 are accepted with clarifications; 0018 through 0020 record integrated product positioning, evidence principles, and bounded interviews. Relevant briefs, glossary, map, plan guidance, and the public introduction are updated.

`python3 scripts/check-project.py` passed with 7 parts, 24 tasks, 109 documents, 637 local links, and no errors before final review; `git diff --check` passed. These are structural checks, and the scenarios are design walkthroughs rather than executed agent behavior. The historical interview handoff and comparison note remain preserved. Task 02's detailed contract, task 03's migration, and other packages' implementations are outside this delivery.

Pending project action: commit the identified output, review it against the unchanged task criteria and adopted brief, then record acceptance, push, and open a focused PR with `Refs #2`. Merge and release require separate session authorization.

## Review
Output delivered for review against the four unchanged criteria above and the adopted [brief](brief.md). The user's instruction to proceed supplies adoption of the assistant-recommended choices; it is not represented as individual answers the user did not give. Final review will identify the committed output and scope revision, check historical preservation and the worked cases, and record acceptance or findings before project delivery.

---
status: done
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

Decision output revision: `208b19750d7926369cc0b60a8ff421a4c346c066`. Acceptance is recorded below. Project delivery: the task branch was pushed and [PR #10](https://github.com/somethingdarkside1/atlas-skills/pull/10) was opened with `Refs #2`. The remaining project action is PR review; merge and release require separate session authorization. The next eligible core-model task is 02 for a workspace with access to this accepted output, and it has not been started.

## Review
Accepted on 2026-09-15 against output `208b19750d7926369cc0b60a8ff421a4c346c066`, compared with starting revision `f3e9e7ceb5942ae69ca9efd1f04927f62dca61a5`. Scope is `plan/core-model/brief.md` and this task's Delivers, Check by, and Done when at output revision `208b19750d7926369cc0b60a8ff421a4c346c066`; the original four criteria were retained. The user's instruction to proceed authorized adoption of the assistant-recommended choices, as explicitly recorded in the adoption note.

| Criterion | Examined evidence and result |
|---|---|
| Three media | Adoption note's worked cases cover a reviewed and an integrated code fix, PDF preparation and receipt, and non-Git prototype observations. Pass as design walkthroughs. |
| Decision dispositions | Decisions 0012 through 0017 explicitly accepted with scope clarifications, 0018 through 0020 record the additional choices, and historical supersessions retain their bodies and ids. Pass. |
| Four material distinctions | Decisions and work/method glossary separate work, project delivery, acceptance, integration, operation completion, readiness, authorization, methods, and pointers. Pass. |
| Current homes | All seven affected briefs consume adopted boundaries while retaining later choices; core map direction is decided, with implementation still pending. Pass. |

Primary-agent review and a separate read-only agent review of the committed output found no actionable content findings. `python3 scripts/check-project.py` passed at that output with 7 parts, 24 tasks, 109 documents, 637 local links, and no errors. A temporary scope check compared the candidate with the starting revision and confirmed all 23 other task files and the selected task's criteria were unchanged, historical decision bodies were retained, skills/examples/archive were unchanged, and supersession targets resolved. The actual staged diff passed `git diff --cached --check` and matched the examined content before commit.

Limits: this accepts the decision delivery, not the replacement skills, behavior, installation, efficiency, complete core-model package, or integration. No human judgment remains pending within this selected decision scope. The follow-up acceptance commit changes only this task's status and delivery/review receipt; the accepted decision artifacts and scope remain at the named output revision. Project delivery is separate and must be reported from its actual result.

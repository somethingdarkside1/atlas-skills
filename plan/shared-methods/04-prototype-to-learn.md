---
status: review
kind: build
blocked_by: ["core-model/01"]
---

# 04: Write the prototype method

## Delivers
One reusable experiment method with a bounded question, distinguishing observation, evidence, limits, and verdict.

Source: Matt prototype UI/LOGIC; original F25-F26. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [x] Support UI preference, logic behavior, and a non-code experiment through conditional guidance.
- [x] Use tests, persistence, or error handling when they are necessary to answer the question.
- [x] Distinguish measured facts, preference decisions, and inconclusive results.
- [x] Keep the retained evidence and normal verification requirements for any copied production material.

## Delivered
### 2026-09-17
Branch `codex/shared-methods-03-04` from `origin/main` at `24b24ef`, in the worktree `.claude/worktrees/agent-a933746b554247f62`.

Made: [the prototype method](../../methods/prototype.md); a `prototype-it` row in [the method consumers](../../methods/README.md); [replayable fixtures](../../tests/fixtures/prototype/README.md) for a library hold rule, two renewal form layouts, and two renewal email subject lines; and [the evidence note](../../notes/2026-09-17-review-verification-and-prototype-methods.md), shared with task 03. The method labels each result as a measured fact, a preference, or not clear yet, and its verdicts match the draft `prototype-it` wording: `yes`, `no`, or `not clear yet`, plus the chosen option when options were compared.

Checked in scratch copies, following the method: `python3 holds.py` showed the state after each action, refused two illegal actions, and found the book on the shelf while a member waited after `hold Ben, return, hold Ana, cancel Ben`; `python3 holds.py pass-on` found no such state in all 1472 legal sequences of up to six actions. The proposed verdict is `yes`, for the person to confirm, and the exhaustive search is in the prototype because the question covers every sequence. `python3 measure_options.py` counted 5 fields before the first button in option A and 2 in option B; the agent did not view the page, recommended B, and left the verdict to the person. The subject lines measured 39 and 61 characters, and with no send history the verdict is `not clear yet`, with a split send as the next experiment. `python3 scripts/check-project.py` passed with 7 parts, 24 tasks, 111 documents, 663 local links, and no errors; `git diff --check` passed.

Not checked: a person's actual preference or confirmation, a rendered view of the form options, any code copied into production work (none was copied, so that rule is shown only in the method text), and loading from an installed `prototype-it` (task 05 and the work-skills migration). The author wrote and ran every case in the same context.

Version: 583851dcfed0 (8 files)

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

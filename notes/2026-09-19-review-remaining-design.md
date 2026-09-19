---
date: 2026-09-19
kind: review
part: project
---

# Remaining design changes before finalising the skills

## Summary

Vitali accepted separate build and review invocation and checking a part's combined Outcome before completion. The remaining design needs focused refinement rather than more commands or a new workflow. Glossary enforcement is a proposed change; simpler entry, careful adoption, evidence freshness, and useful resumption already follow the adopted plan.

## Detail

### Examined scope

Read the executable skills and their formats at `3f6aa5b`, the owning tasks, decisions 0012 through 0025 as relevant, and the [simplicity assessment](2026-09-19-research-matt-simplicity.md). A separate agent checked glossary, setup, evidence, and identity boundaries against the same local sources. This is a static design assessment, not behavioral acceptance.

### Accepted in this session

- Q3: `/build-it` names `/review-it` as the next command; review remains separately invoked for the first release. This confirms the existing explicit invocation direction.
- Q4: a part with accepted logo exports but a missing promised usage guide remains open. The completed tasks keep their acceptance and the missing work is identified. [0026](../decisions/0026-part-completion-checks-the-combined-outcome.md) records the rule. It must reach both review and map maintenance: current [map-it](../skills/map-it/SKILL.md) can independently infer done from task statuses alone.

### Recommendations and their owners

| Change | Why it matters | Status and owner |
|---|---|---|
| Let the glossary resolve meaning rather than reject harmless wording | [Interview](../skills/interview-me/SKILL.md) asks for entries for new words, and [review](../skills/review-it/SKILL.md) rejects Avoid synonyms. An ordinary word in a task can cause terminology work without changing any decision. | Proposed [0027](../decisions/0027-glossary-checks-meaning-not-every-word.md), Q5 pending. Shared-methods/01 and work-skills/01 and 02 own the consumers. |
| Keep the ordinary path small | A clear task under an existing brief should need the relevant inputs and real checks. Current skills often send any missing home to setup, and [plan-it](../skills/plan-it/SKILL.md) asks for confirmation even when the request already authorizes the one-task change. | Existing [0020](../decisions/0020-decide-only-the-selected-scope.md) and [authoring boundary](../skills/README.md). Implement required reads and reuse existing answers in work-skills/01 and 02. |
| Adopt existing project content and policy without overwriting it | [Setup](../skills/setup-atlas/SKILL.md) promises existing homes stay unchanged, then imports terms into the glossary, replaces an older instruction block wholesale, and treats a missing exact Saving work heading as missing policy. | Existing [0015](../decisions/0015-setup-adopts-routing-observes.md). Project-setup/01 and 02 own an explicit adoption diff, preservation, and repeatability. |
| Recheck what changed in the result or requirements | A file checksum alone does not change when the brief adds monochrome compatibility. Preserve old acceptance as history, then assess and recheck affected claims. Retain the accepted light evidence default rather than introducing mandatory snapshots. | Existing [0019](../decisions/0019-acceptance-follows-output-and-scope.md) and [0022](../decisions/0022-one-version-line-per-delivery.md). Core-model/02 must reconcile the retention wording and define minimal output and scope identity. |
| Resolve current work before following a handoff or changing a label | A task can remain doing across several attempts, so matching status does not prove a note is current. A newer unrelated handoff should not hide the relevant one. A renamed heading must not silently break task or dependency identity. | Existing [handoff task](../plan/work-skills/04-prototype-and-handoff.md) and [identity task](../plan/work-skills/03-map-and-identity.md). Use the current record and preserve stable references. |

These recommendations do not add another layer of tracking. Task state remains in the plan, formats remain in their homes, and project instructions retain delivery policy. No runtime procedure has changed in this assessment. Once the glossary choice is settled, the next useful evidence comes from implementing and exercising these boundaries rather than extending the design catalogue.

### Verification and limits

The accepted/proposed labels were checked against the actual Q3 and Q4 answers. Task acceptance remains unchanged, and the new combined-outcome cases are unchecked. The project structural checker and diff whitespace check validate the planning changes; they do not show that the executable draft implements them. The proposed glossary change remains pending a user answer.

## Copied into

[0026](../decisions/0026-part-completion-checks-the-combined-outcome.md) records accepted part completion, [0027](../decisions/0027-glossary-checks-meaning-not-every-word.md) holds the proposed glossary change, and the [work-skills brief](../plan/work-skills/brief.md), [review task](../plan/work-skills/02-build-and-review.md), [map task](../plan/work-skills/03-map-and-identity.md), and [map](../MAP.md) hold the corresponding current scope and acceptance cases.

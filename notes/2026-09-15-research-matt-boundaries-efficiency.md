---
date: 2026-09-15
kind: research
part: core-model
---

# Matt's skills and Atlas efficiency

## Summary

Matt Pocock's current skill sources provide a useful model for small, composable operations and a direct path for small work. Atlas can retain that economy while proposing stronger evidence and resumption contracts, but its replacement contracts remain unaccepted and unvalidated. These findings inform the pending boundary interview; they do not adopt its decisions.

## Detail

### Scope and sources

Read five upstream skill files from Matt Pocock's public repository on 2026-09-15, alongside Atlas's [package brief](../plan/core-model/brief.md), [selected task](../plan/core-model/01-settle-boundaries.md), [plan format](../plan/README.md), and decisions 0012 through 0017. The upstream links below use moving `main`: the browsing service returned their contents, but a commit lookup failed, so this note does not establish a pinned upstream revision. The ignored local comparison directory has no independent Git metadata; an enclosing Atlas commit must not be presented as its upstream revision. No full collection audit or behavior benchmark was performed.

### Observed upstream instructions

- [ask-matt](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/ask-matt/SKILL.md) distinguishes work that fits one session from work needing multiple sessions. Small work can proceed directly to implementation; larger work receives a spec and dependency-bearing tickets. It also distinguishes reusable vocabulary methods from the main workflow and offers several context-continuation options. This is evidence for a deliberate small-work route, not a measured performance result.
- [grilling](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md) asks independent questions in rounds, assigns fact discovery to agents, and waits on decisions. Its stopping rule reaches every decision branch and requires confirmation of shared understanding. This gives explicit control but does not itself bound the interview to the material choices of a selected deliverable.
- [grill-with-docs](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/grill-with-docs/SKILL.md) is a minimal wrapper invoking grilling and domain-modeling. It demonstrates composition by delegation. This file alone does not establish portable execution when a host lacks the named Skill tool or a selectively installed dependency.
- [implement](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/implement/SKILL.md) invokes TDD where possible, calls for recurring focused checks and a final full suite, reviews, then commits to the current branch. Its brevity leaves workspace preparation and review input details to surrounding context.
- [code-review](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/code-review/SKILL.md) resolves a fixed comparison point, checks for a nonempty `git diff <fixed-point>...HEAD`, and separates standards from specification review through parallel agents. It skips automated-tool concerns and reports missing specification evidence explicitly. Its specified diff excludes uncommitted changes. Combined with implement's review-before-commit order, this creates a static contract gap unless another instruction supplies the working changes to review. No execution was performed to determine how a particular agent would handle that gap.

### Recommendations for Atlas, pending user choice

1. Preserve a direct small-work route: one selected task, the relevant brief, necessary methods, and proportionate checks. Do not require a fresh interview, decomposition, or new architecture decision when the existing scope already settles them. Promote work to a package only when independent outputs or unresolved dependencies justify it.
2. Bound the interview by the selected outcome. Investigate accessible facts, ask only questions that change scope, acceptance, authorization, or consequential design, and defer unrelated branches explicitly. Stop when material choices for this task are settled; do not interpret silence or a recommendation as acceptance.
3. Keep evidence small but exact. Identify the output and applicable scope, record checks and outstanding judgment, and report integration separately when relevant. The same logical record should support a code tree, a document version, or a prototype artifact. Dates and mutable branch names alone cannot identify reviewed content.
4. Make review inputs explicit before composing methods. A review must identify the candidate, comparison baseline where applicable, and scope. It must cover the changes that will actually be delivered, including relevant uncommitted content. Changed content or requirements should trigger an impact assessment and affected checks, rather than an automatic full review or unconditional reuse.
5. Load methods on demand and keep each rule in one home. Update durable documents only when their facts change; retain a concise task record rather than copying the same result into several summaries. The proposed local method packaging needs installation tests before it can claim portability.
6. Treat parallel review as a choice justified by the task's risk and independence of review questions. A tiny reversible edit may need direct inspection and one focused check; a substantial behavior change may benefit from independent specification and standards review. Required project checks still apply.

These are design recommendations, not observed advantages of the current Atlas skills. [Decision 0012](../decisions/0012-atlas-owns-work-projects-own-delivery.md) proposes the ownership boundary, [0014](../decisions/0014-shared-methods-travel-with-consumers.md) proposes method packaging, [0015](../decisions/0015-setup-adopts-routing-observes.md) proposes separate setup, and [0016](../decisions/0016-pointers-before-label-taxonomy.md) proposes focused reads. The current plan explicitly identifies the executable skills as the earlier draft.

### Evidence needed before claiming efficiency

Compare equivalent tasks under the same model, host, starting state, and acceptance criteria: a small code correction, a multi-session change, a document delivery, and a non-Git prototype. Include interrupted resumption and changed candidate or scope cases. Record success against criteria, unsupported completion claims, missed changes, user decision rounds, context read, tool calls, and elapsed time; report repeated-run variation and all failures. Lower token use alone is not sufficient if needed evidence is missed. No token savings, speedup, or reliability ranking is established by this source inspection.

## Copied into

Nothing durable. The recommendations remain input to the pending core-model/01 interview; no decision or task acceptance state was changed.

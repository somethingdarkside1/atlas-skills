---
name: review-it
description: Assess a task against its current scope and project conventions, recording acceptance, findings, or outstanding judgment.
disable-model-invocation: true
---

# Review it

Judge the delivered result independently of the builder's explanation.

Read the task, its applicable brief and decisions, current delivery identity, plan working and acceptance rules, project conventions, and the actual result. Inspect relevant surrounding material and affected dependencies. Use a fresh reviewer context when available and useful; supply the exact candidate and criteria. Otherwise review directly and state that limit.

1. Resolve the requested delivery and scope, including working changes. Compare their current identities with the delivery using [evidence.py](evidence.py) or the project's equivalent. Changed content or requirements need impact assessment and renewed affected evidence, not automatic rejection or automatic reuse. If the required candidate is unavailable, name what must be recovered.
2. Check the brief and task criteria, then the project's applicable conventions. Rerun meaningful checks and inspect the result; use [verification](verification.md) when evidence is incomplete or unclear, and [diagnosis](diagnosis.md) for an unexplained failure that prevents a justified conclusion. Distinguish a documented requirement from a stylistic suggestion. Glossary wording matters when it changes meaning or breaks an explicit requirement.
3. Record the examined output and scope, observed checks, and each material finding with its location, effect, and correction. Correct harmless reporting errors in the review. Preserve valid evidence and bind human judgments to the version they concern. An unanswered human check stays pending; a prior tick is not confirmation of materially changed work.
4. Apply the plan's result: findings return the task to doing with a specific next action; a scope choice goes to interview-me; only human judgment outstanding leaves review waiting; clean supported acceptance makes the task done. A repeat with no changed evidence or answer reports its existing result without another identical pass.
5. When current work for the part is accepted, assess the combined Outcome under the plan format. Keep valid task acceptance if the plan missed work; record Remaining work and send it to plan-it. Mark the part done only with a linked combined acceptance record. Save the task and any affected map pointers under project policy. Project delivery follows its own authorization and is never implied by a clean review.

Finish with the acceptance, actionable finding, or precise wait. A fixed finding gets a new delivery and affected review, rather than an instruction to restart everything.

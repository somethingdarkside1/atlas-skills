# Diagnosis

Use when a reported failure needs an explanation to choose the next action. Start with the existing signal and the smallest useful check; expand when competing explanations remain. A known correction with sufficient evidence can return directly to the caller's normal verification.

## Inputs

Identify the expected and observed behavior, examined output or input revision, relevant context and constraints, and prior attempts. Reuse a still-applicable reproduction. Set an investigation bound appropriate to the question, such as two discriminating checks or ten minutes, before probing. Accessible facts are investigated; a material missing human decision remains pending.

## Process

1. Establish the signal. Run the smallest available reproduction that reaches the reported failure, recording expected versus actual behavior and the exact input and environment. In software this may be a failing command; in data or a process it may be reconciliation of specific records or an observed handoff. Reduce unrelated inputs only while preserving the symptom. For intermittent failures, record attempts and failures under named conditions; a clean attempt alone does not disprove the report. If reproduction is unavailable, record what was tried, what is missing, and the evidence needed to proceed. Done when an observed failure or explicit reproduction limit is available.
2. Separate observations from explanations. Label direct observations and their sources, then rank plausible competing hypotheses with a prediction that would support or weaken each. Use as many as the evidence warrants. A report or plausible story remains unconfirmed until checked. Choose the cheapest available check whose possible outcomes distinguish the leading explanations, including a result that supports neither. Done when the next probe has explicit predicted outcomes, a cost within the bound, and an unchanged comparison basis.
3. Run that check and update the explanations. Record the actual action and result, including errors or unavailable checks, before choosing another probe. Change one relevant condition at a time where possible; state confounders when isolation is unavailable. For software use the real failure path or label a stand-in's limits. For data compare keys, units, provenance, and row counts as relevant; for a process inspect the relevant sequence and handoff evidence. For a timing regression compare measurements under equivalent conditions. Done when the result supports or weakens the predictions, or leaves them unresolved.
4. Return a justified next action. Stop when evidence supports a bounded correction, the investigation bound is reached, required evidence is unavailable, or checks cease to add information. An unsuccessful investigation returns its reproduction, uncertainty, and the next discriminating check or exact missing input; extending the bound needs a stated reason and usable new evidence. A supported cause is limited to the examined conditions. If the caller applies a correction, it reruns the original signal and its normal required checks against that changed output. Done when the caller can act or resume from the returned evidence without treating diagnosis completion as a fix or acceptance.

## Return to the caller

Return a compact record containing:

- Scope and identity: question, examined files or records and revision, environment, and investigation bound.
- Signal: expected and actual result, runnable reproduction or inspection steps, and reproduction limits.
- Evidence: observations separate from hypotheses, each probe's prediction, actual result, and effect on the explanations.
- Conclusion: supported explanation or inconclusive result, remaining uncertainty and human judgments, and the next justified action with its required input.

Include only the evidence needed to reproduce or assess the signal; remove secrets from retained excerpts. Identify any temporary probes and what was removed or retained. The caller selects the durable home and owns changes to tasks, artifacts, acceptance, and project delivery.

## Attribution

Adapted from Matt Pocock's [diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md), inspected from the local reference labeled 1.2.3. The source inspired the reproduction, falsifiable prediction, and targeted probe discipline. Atlas adds proportional bounds, non-code evidence, and a caller-owned return. The upstream URL is a locator, not a pinned revision; the [task evidence](https://github.com/somethingdarkside1/atlas-skills/blob/72e890a/notes/2026-09-15-review-diagnosis-method.md) identifies the inspected bytes.

MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

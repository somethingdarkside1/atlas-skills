---
status: todo
kind: build
blocked_by: ["core-model/01"]
---

# 02: Write the diagnosis method

## Delivers
One reusable method for reproducing a symptom, testing competing explanations, and identifying a justified next action.

Source: Matt diagnosing-bugs; verification weakness in original F03. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] Record a failing signal or explain why reproduction is unavailable.
- [ ] Separate observations from hypotheses and test the cheapest discriminating next check.
- [ ] Bound unsuccessful investigation and retain the reproduction and uncertainty in the output.
- [ ] Exercise a software failure and a non-code process or data-quality failure without requiring the same tooling.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

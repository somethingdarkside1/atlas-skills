---
status: todo
kind: check
blocked_by: ["01", "02", "work-skills/05", "project-setup/03", "context-routing/02"]
---

# 03: Run independent end-to-end acceptance

## Delivers
Dated independent cold-context results for the revised method and a real project, with regressions traced back to owning tasks.

Source: Release evidence gate 0017; meaningful behavioral validation. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] An independent agent or fresh session receives a realistic task and minimum raw inputs without the expected answer.
- [ ] Runs cover all four methods, ordinary delivery, retries, human judgment, changed evidence, setup recovery, and project delivery variants.
- [ ] Record model/harness, revision, steps, actual outcomes, limits, and unresolved failures.
- [ ] Compare relevant results against the initial draft or second-pass baseline before claiming improvement over Matt or earlier Atlas.
- [ ] Required failures are fixed and rechecked before public release is unblocked.
- [ ] (you) Vitali completes the scratch-brand route from [work-skills/06](../work-skills/06-patch-the-draft.md) on the prepared candidate, with observations recorded and failures resolved. This is the deferred human check under [0025](../../decisions/0025-finish-simple-skills-before-the-human-run.md), not a substitute for independent agent evidence.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

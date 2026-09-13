---
status: todo
kind: build
blocked_by: ["01", "02", "03", "04"]
---

# 05: Bundle method references for each consumer

## Delivers
A single authored source per method, explicit consumer-to-method mapping, and deterministic generated references inside selectively installable skills.

Source: Selective-install gap and method/discovery research. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] A consumer loads only the method branch its trigger requires.
- [ ] Every distributed reference records its canonical source/version and matches generated content.
- [ ] Single-skill installation includes every hard reference without assuming sibling skills are installed.
- [ ] The generation check detects stale copies and has a meaningful fixture for a missing reference.
- [ ] Standalone method skills are added only if an independent invocation case and host test justify them.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

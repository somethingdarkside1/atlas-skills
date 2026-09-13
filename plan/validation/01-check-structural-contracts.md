---
status: todo
kind: build
blocked_by: ["core-model/02"]
---

# 01: Extend structural contract checks

## Delivers
An automated check suite for active task and part graphs, links, format versions, method packaging, metadata, and migration integrity.

Source: Original F15, F18, F27-F28; current repository checker is a starting point. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] Extend scripts/check-project.py with adopted invariants rather than exact prose snapshots.
- [ ] A meaningful invalid fixture demonstrates each graph and stale-reference failure.
- [ ] Generated method copies and installation dependencies are checked.
- [ ] Current and legacy fixture handling follow the declared migration support.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

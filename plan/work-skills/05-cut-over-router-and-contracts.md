---
status: todo
kind: build
blocked_by: ["01", "02", "03", "04", "project-setup/02", "shared-methods/05"]
---

# 05: Cut over routing and remove provider coupling

## Delivers
A read-only atlas router and a consistent complete operation set using the adopted local formats and project-owned delivery policy.

Source: Original F01-F13, F23-F24, F27; all provider-coupling tasks in the initial plan. See the [package brief](brief.md) and [architecture review](../../notes/2026-09-13-review-methods-and-project-policy.md).

## Check by
Run the scenarios below against a scratch copy or the exact candidate revision and record the observed outputs, checks, and limits.

## Done when
- [ ] All operations declare and follow the same read/change/finish/recovery contract.
- [ ] Normal atlas inspection leaves the project unchanged and prioritizes current valid evidence over notes.
- [ ] Initialization routes to setup; repair is an explicit owned action.
- [ ] Core skills and portable plan formats contain no hosted tracker implementation or automatic commit/merge policy.
- [ ] Explicit invocation remains supported; go is removed or clearly deferred until a compatible independently tested design exists.
- [ ] Publish the legacy GitHub migration notice and exact compatibility boundary.

## Delivered
Pending. Record the selected workspace/branch when work begins, then the output revision and actual check evidence when delivered.

## Review
Pending. Record the reviewed output and brief revision, findings or acceptance, and any unresolved human judgment.

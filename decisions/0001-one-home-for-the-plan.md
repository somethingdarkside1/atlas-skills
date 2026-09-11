---
part: plan-skill
date: 2026-09-11
status: accepted
---

# The plan has one home per project: files or GitHub issues

Matt Pocock's set makes the tracker configurable, so every skill carries GitHub, GitLab, and local-file branches and a setup skill must run first. Atlas asks once, at scaffold time, whether the plan lives in `plan/` as files or in the repo's GitHub issues, and records the answer on one line in `plan/README.md`. The glossary, map, decisions, and notes stay in the repo either way; only work items move. A mirror was considered and rejected because two copies of a plan drift, and the drift policy it needed was a sign of the wrong design.

Considered: GitHub-only (excludes non-code projects and people without a repo); a configurable tracker abstraction (what Atlas exists to remove); files mirrored to GitHub by a publish skill (drift).
Revisit when: a second tracker (Linear, Jira) is wanted badly enough to pay for a third branch in four skills.

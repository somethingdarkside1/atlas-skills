---
part: build-skill
date: 2026-09-11
status: accepted
---

# Branches and merges exist only with a GitHub tracker

With `Tracker: files`, `build-it` works in place on whatever is checked out and commits when the folder is a git repo; there is no branch per task and the `Merge:` line is ignored. Branches, PRs, and the merge choice appear only with `Tracker: github`, where a PR gives the branch somewhere to go. The earlier design gave every git project a branch per task, which left a person without GitHub merging branches by hand and gave four skills three environments to describe instead of two.

Considered: a `Git:` line in `plan/README.md` refreshed by `/atlas` (one more line to keep true); a live git check in every skill (the same three branches in four skills).
Revisit when: a GitLab or local-only reviewer wants PR-style review without GitHub.

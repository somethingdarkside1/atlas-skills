---
part: five-things
date: 2026-09-13
status: accepted
---

# Every rule has one home, and when a skill disagrees with it the home wins

The first pass found the same rule stated in two or three places with small differences (which task is next, what a task is called, where `(you)` goes), and an agent reading both had to pick. Now formats live in the five things, the git and tracker rules live in `plan/README.md`, the shapes skills share live in `skills/README.md`, and a skill points at the home instead of quoting it. The `CLAUDE.md` block says the format wins, so an agent that finds a conflict follows the home and the skill is the thing to fix.

Considered: letting the newest text win (nobody can tell which is newest); a lint script as the arbiter (worth adding, but it cannot decide meaning).
Revisit when: a rule has no natural home and a second copy is unavoidable.

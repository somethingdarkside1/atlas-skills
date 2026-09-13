---
date: 2026-09-13
kind: handoff
part: project
---

# Handoff: review, conclude, and merge the second pass

## Summary
Branch `claude/skill-list-analysis-d40ccf` holds one commit (`34977ff`) that revises all eight skills so every shared rule has one home, waits are on disk, and git is described once. It is committed, unpushed, and unmerged. The next agent reviews it against the checklist below, settles the two open calls, and merges it into `main`.
Next: /atlas

## Detail

### What to read, in order
1. `notes/2026-09-13-review-second-pass.md`: what changed and why, in one page. `docs/second-pass.html` is the long form (also published privately for Vitali).
2. Decisions `0009` (task id), `0010` (waits on disk, the `review` status), `0011` (the home wins).
3. The homes: `plan/README.md` (Ids and statuses, Which task is next, Git), the `MAP.md` format comment, `GLOSSARY.md` Statuses, `notes/README.md`, `skills/README.md` (Shapes every skill shares).
4. `git diff 374430e..34977ff -- skills/`: the eight skills.

### Review checklist
- **One home.** Each rule in the table in `docs/second-pass.html` appears in its home and is only pointed at elsewhere. Grep a few: `grep -rn "lowest-numbered" skills plan`, `grep -rn "(you)" skills plan`.
- **Copies agree.** `plan/README.md`, `notes/README.md`, the `MAP.md` and `GLOSSARY.md` format comments, and the `CLAUDE.md` block match their copies in `skills/atlas/templates/` and `examples/brand/` byte for byte (checked at commit time with `cmp` and `diff`).
- **Shared shapes.** Every skill but `/atlas` has the identical step 1; every commit step starts `Commit as plan/README.md says`; every stop is a reason line then a `Next:` line.
- **Walk the loop on paper.** todo, doing, review, back to doing on findings, done on clean; a silent brief sends a question to the map and `Next: /interview-me`; `/atlas go` stops at non-build commands, three passes with findings, and `For you to check:`. Confirm no path loops.
- **Statuses.** The glossary's derived statuses (sketched: no brief; decided: brief, every task todo; building: a task past todo, not all done; done: all done) agree with who moves them in `skills/README.md`.
- **Prose rules.** No em dashes; no word from a glossary Avoid list in a skill (the verb "Turn" in plan-it's description is fine).

### Open calls for the reviewer
1. **A silent brief on a GitHub task branch.** `/build-it` step 4 writes the open question to `MAP.md` while the task branch is checked out, so the edit rides the PR instead of reaching the default branch. Recommended: accept it riding the PR and say so in the Git section of `plan/README.md` (and its two copies), because moving uncommitted work between branches is riskier than a late map edit.
2. **Where HTML write-ups live.** This pass added `docs/` and a Layout line in `CLAUDE.md`. Recommended: keep it; it is repo-only and never enters a project, so decision 0002 is untouched.

### How to conclude
1. Fix anything the checklist finds on this branch, as a separate commit.
2. Merge from the main checkout (`/Users/vitali/Documents/Projects/Skills Po`, on `main`), matching the earlier merge style: `git merge --no-ff claude/skill-list-analysis-d40ccf -m "Merge claude/skill-list-analysis-d40ccf: second pass, one home per rule"`. Resolve conflicts in favour of the homes.
3. The repo has no remote yet, so there is nothing to push. When one exists, push only if Vitali asks; the earlier handoff defers pushing until the end-to-end test passes.
   Another worktree, `claude/atlas-design-nuances-d452cf`, sits on the same base (`374430e`). Before merging, check it with `git -C .claude/worktrees/atlas-design-nuances-d452cf status` and `git log main..claude/atlas-design-nuances-d452cf`; if it holds work touching the skills or the homes, ask Vitali which lands first, because this pass rewrites most of those files.
4. After merging, the next real work is unchanged: the end-to-end test described in `notes/2026-09-11-handoff-skills-written.md`, now using the `review` status and the task ids from decision 0009.

### Not done in this pass
No skill has been run. `scripts/check.sh` (mechanical invariants) is proposed, not written. Whether `gh` 2.100 creates sub-issues and blocked-by dependencies from the command line is untested.

## Copied into
Nothing durable; everything this pass settled is in the commit it hands over.

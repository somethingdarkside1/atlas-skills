---
date: 2026-09-18
kind: review
part: work-skills
---

# The first agent run of the 0.2 skills

## Summary
An agent ran the six-step script from [work-skills/06](../plan/work-skills/06-patch-the-draft.md) on real scratch folders, with the 0.2 skills as they stand on PR #12, and every step reached its expected end. Nothing stopped the run, but it found one loop that happened, one that was waiting to happen, a wrong route, a fragile recovery, and one fault that could make a review reject unchanged files; all five are fixed in the skills, with a few smaller fixes. Vitali's own cold run is still the acceptance check.

## Detail

### How it was run

The skills were exported from `codex/work-skills-interview` at `62b0ff6`. A real `claude -p --plugin-dir` session could not sign in from the sandbox, so each session was a fresh Claude Opus 5 sub-agent told to read a skill's `SKILL.md` in full when a slash command arrived and follow it exactly, working only in the scratch folder. Follow-up messages played the human, answering from the brand example's own brief and decisions. Folder `a` was empty with `git init`; folder `b` was a copy of `examples/brand/` with one first commit. Two sessions died on network errors; one left a half-made edit, which became an unplanned test of recovery.

Differences from a real install: skills were read by path rather than loaded by the harness; the sub-agents could not open a browser or see an image; the first session added a co-author line to its commit until told to use the project's message only; from step 5 the session prompt asked for proportionate evidence (what was run and seen for Check by and each box) so the step 3 loop below would not repeat.

### What each step did

| Step | Commands | Result |
|---|---|---|
| 1 | `/setup-atlas`, `/atlas` in `a` | Five homes, the Atlas block and `Saving work` in `CLAUDE.md` and `AGENTS.md`, one commit. `/atlas` printed `0 sketched, 0 decided, 0 building (none), 0 done` and `Next: /interview-me`. |
| 2 | `/atlas` in `b` | `wordmark/02` reported as doing with nothing delivered; `Next: /build-it wordmark/02`. |
| 3 | `/build-it` and `/review-it wordmark/02`, as many times as needed | The first build stopped early and recorded why: task 01 names `wordmark/candidates.svg`, which the example never had. After the human said to redraw it, 5 more builds (one killed by a network error) and 5 reviews. Reviews compared the `Version:` line first, ran in a fresh sub-agent, and recorded findings with a place and a fix. The rejected `(you)` box became a finding in the human's words. Ended done. |
| 4 | `/interview-me palette`, one round, `/park-it`, then `/atlas` in a fresh session | Round 1: five questions with options, costs, and a recommendation. Round 2 answered a question asked back before asking anything new, caught "version" as an Avoid word, and listed nothing as waiting (decision 0024). The handoff held the round in flight. The fresh `/atlas` named it live and printed `Next: /interview-me palette`. |
| 5 | Finish the interview, `/plan-it palette`, `/build-it`, `/review-it`, `/atlas` | Palette decided with two decisions and a final brief; two tasks with a cross-part blocker. Bare `/build-it` took `wordmark/03`, as the shared rule says. Its review found that the brief's Outcome promises a favicon the page's minimum size rules out. `/atlas` marked the old handoff as no longer live. |
| 6 | `/plan-it wordmark "export a favicon"`, `/map-it` | Refused before drafting: the Outcome names a favicon and the Out of scope names "a symbol or icon". `Next: /interview-me wordmark`. `/map-it` rebuilt an identical diagram and reported "symbol" as a term with no entry. |

### Faults found and fixed

1. **A review could reject unchanged files.** No review in this run did, but the `Version:` recipe said "sorted order" without saying which. Checked on the run's folder, the same four files gave `9ae6cb712f54` in byte order and `26eaf0acc937` in the en_GB order a Mac terminal uses, and `./GLOSSARY.md` hashes differently from `GLOSSARY.md`, because `shasum` prints the path into what is hashed. `/review-it` sends a mismatch back to `/build-it`. The same fault turned up in the independent review of the verification method (PR #14). In this run a reviewer had to try several commands, because only `/build-it` names it. Now `/build-it` names every delivered file by its path from the project root, and both skills give the command, with paths written without `./` and in byte order (`LC_ALL=C sort`).
2. **Loop waiting to happen: an unanswered question in a task.** `/build-it` stops early with an `Open question:` line, but a later run carries on from the entry without asking it, and `/atlas` keeps routing there. Now `/build-it` asks that question first when the human has not answered it.
3. **Loop: reviews bounced a finished task for wrong prose.** Three reviews in a row sent `wordmark/02` back; twice the only finding was a wrong measurement in the builder's own notes, while the files and boxes were right. Each build added figures, and each review found a slip in them. Now a wrong statement that changes no delivered file and no box goes in the pass as a `Corrected:` line instead of a finding.
4. **Wrong route: a finding that needs the brief changed.** The `wordmark/03` finding could only be fixed by the human changing the Outcome, but `/review-it` could only route to `/build-it`, and `/atlas` then sent a build. Now `/review-it` also writes such a finding on the part's open questions and prints `Next: /interview-me <part>`, which `/atlas` already routes before a build.
5. **Recovery after a crash rested on luck.** A new session found the dead session's uncommitted edit only because it happened to look; `/build-it` never read `git status`. Now it reads it, says what it found, and checks those changes against Delivers and the findings before carrying on.

Smaller fixes: `/setup-atlas` asks `What is this, in a sentence?` together with its first question instead of after the yes, and when neither instruction file exists it writes `CLAUDE.md` and links `AGENTS.md` to it, as the brand example does, instead of two copies that can drift apart. `/build-it` has a commit message for an early stop. `/review-it` does not count code as prose when checking Avoid words (`padding` in CSS). `/interview-me` marks a question about a fact only the human knows `(your call)`, so a skip does not record a guess as fact. The brand example's `plan/README.md` matches the template again.

### Noticed and left alone

Each of these slowed a session once or made two sessions answer differently; none stopped the run. They are left for Vitali's cold run rather than fixed, because each fix adds words.

- `/atlas` fixes the shape of line one only, so lines two to four came out bare in one session and labeled in another.
- `/plan-it` ends with the ready task of the part it planned, while bare `/build-it` and `/atlas` pick by the shared rule (`palette/01` against `wordmark/03`).
- The commit pattern `<n> findings` gives "1 findings"; sessions wrote "1 finding".
- `/interview-me` writes files after every batch of answers but saves only at the end.
- "Skip for now" meets both the skip rule and the "for now" rule. Question numbers ran on across rounds without a rule saying so.
- Work one part owes another (a link on the wordmark usage page, a sentence in a done file made stale by a palette decision) has no home except an open question, which would reroute `/atlas`.
- `/map-it` cannot tell a term from an ordinary word when checking definitions.

### What this says about the open choices

- **An Outcome check on a part's last task:** the reviewer of `wordmark/03` checked the Outcome unprompted and found the favicon conflict. That is one case, not a rule.
- **Evidence weight:** the `Version:` line caught nothing false in this run, and its recipe was the one fault that could have made a review wrong. Longer Delivered entries gave the reviews more to find fault with, as the [evidence weight analysis](2026-09-17-research-evidence-weight.md) predicted.
- **Time:** step 3 took 11 commands for a script of 4, and review sessions ran 7 to 22 minutes each.

### Limits

One agent family played every role, including the human, and knew the example well. Checks that need eyes were done by measuring files, not by looking. No real harness loaded the skills, so invocation, the `disable-model-invocation` setting, and the plugin install were not tested. The fixes were checked by reading and by the project checks, not by a second run.

## Copied into
The fixes are in `skills/build-it`, `skills/review-it`, `skills/setup-atlas`, `skills/interview-me`, and `examples/brand/plan/README.md`, recorded on [work-skills/06](../plan/work-skills/06-patch-the-draft.md).

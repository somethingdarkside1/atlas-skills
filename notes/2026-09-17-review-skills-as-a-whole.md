---
date: 2026-09-17
kind: review
part: project
---

# The eight skills as a whole: what works, what stops a run, what to cut

## Summary
The design holds: five homes, a status on every part, one owner for each status move, and a `Next:` line that joins the skills. The installed skills have not changed since 2026-09-11 and have never been run end to end; seven faults stop an ordinary run, two of them new in this review and confirmed by running the skills' own commands. The revision plan answers real problems but has grown heavier than the method it serves, so this note recommends a small patch release first and a lighter path through the remaining work.

## Detail

### Scope and evidence

Read at `24b24ef`, where this branch equals `origin/main` on 2026-09-17: all eight `SKILL.md` files, the six templates, every decision, the seven briefs and 24 tasks, both 2026-09-13 reviews, the research notes, the second-pass branch at `7f1f12d`, and the brand example. `python3 scripts/check-project.py` passes with 7 parts, 24 tasks, and no errors.

The skills' own `Read first` commands were run against a scratch copy of `examples/brand/` and against a folder holding only the templates, under zsh and bash. No skill was invoked, so agent behavior is still unobserved. Finding numbers F01 to F28 point to the [initial review](2026-09-13-review-atlas-framework.md) and are not restated here. N1 to N7 are new.

### How the method works

Two ladders and two graphs carry the whole method.

| Thing | Values | Who moves it |
|---|---|---|
| Part status | sketched, decided, building, done | `/interview-me` to decided, `/build-it` to building, `/review-it` to done |
| Task status | todo, doing, done | `/plan-it` creates todo, `/build-it` to doing, `/review-it` to done |
| `Needs:` on a part | which parts must be decided first | `/interview-me` writes it |
| `blocked_by` on a task | which tasks must be done first | `/plan-it` writes it |

Every skill ends with `Next: /command <id>`. That line is the only interface between skills, and `/atlas` can rebuild it from the files at any time. This is the strongest idea in the set.

| Skill | Reads | Writes | Asks you | Ends with |
|---|---|---|---|---|
| `/atlas` | the five homes, task states, newest note, git state | the five homes on a fresh folder; status repairs later | one sentence on a fresh folder | five lines, the last is `Next:` |
| `/interview-me [part]` | map, the part's decisions, the formats | terms, decisions, open questions, new parts, then the brief | rounds of numbered questions | `/plan-it <part>` |
| `/plan-it [part]` | brief, its decisions, existing task states | task files | one sizing round | `/build-it <id>` |
| `/build-it [id]` | task, brief, decisions, neighbouring work | the thing, Delivered, ticks, part to building | nothing, or one open question | `/review-it <id>` |
| `/review-it [id]` | task, brief, decisions, glossary, the thing | a dated Review pass, task done, part done | the `(you)` checks | `/build-it <id>` or `/atlas` |
| `/prototype-it "<question>"` | the part carrying the question | `prototypes/`, a note, the answer on the map | your verdict | `/interview-me <part>` |
| `/park-it [focus]` | note format, git status | a handoff note | nothing | `/atlas` |
| `/map-it [part]` | map and glossary sections | both diagrams, a drift report, or a split file | sub-parts, when splitting | `/atlas` |

### What is strong and should survive every revision

1. Five homes with one rule: true today lives in the first four, true on a date is a note.
2. The `Next:` line as the join between skills, recomputable from disk.
3. One owner per status move, so a wrong status has one suspect.
4. The task shape (Delivers, Check by, Done when), which works for an SVG, a page of copy, and code alike.
5. The interview writes the brief while it still has the context.
6. Sections are the truth and diagrams are derived from them.
7. The voice of the draft. `Do one task, prove it, write down what you made.` is a sentence a blog post can teach.

### Seven faults that stop an ordinary run today

These are the ones a first real run will hit. Everything else in F01 to F28 bites later or only in GitHub mode.

1. **N1, observed. The first command `/atlas` runs fails in zsh.** `grep ... MAP.md map/*.md` stops with `no matches found: map/*.md` on every project without a `map/` folder, which is nearly all of them. `grep ... plan/*/*.md` fails the same way on any project with no tasks yet, and `/atlas`, `/plan-it`, and `/build-it` all use it. zsh is the macOS default. An agent will recover, but every run starts with an error. Fix: say what to read, or use a form that survives a missing folder.
2. **N2. The `(you)` marker is written in one place and looked for in another.** The plan template and `/plan-it` put `(you)` at the start of the Check by line. `/build-it` step 5 and `/review-it` steps 3 and 4 look for `(you)` on Done when boxes. Human-only checks never reach the `For you to check:` list. The second pass already moved the marker to the boxes.
3. **F03 and F04. There is no `review` status.** A delivered task stays `doing`, and `/review-it` finds it by "Delivered is newer than the last Review pass", which the file format cannot answer. In the brand example the rule selects `wordmark/02`, a task with an empty Delivered. This repository's own plan already uses `review`.
4. **F01. After a break, `/atlas` cannot see that a decided part still needs planning.** The interview sets `Plan:` when it writes the brief, and both `/atlas` and `/plan-it` test for a missing `Plan:`.
5. **F06, observed. A fresh folder is not empty.** Copying `templates/` also copies `CLAUDE-block.md` to the root, and the map keeps its `First part` placeholder, so the router never sees the empty map it has a rule for.
6. **F05. A handoff is followed forever.** Nothing marks it used or checks that its target is still open, and a newer prototype note hides it completely.
7. **F12. `/atlas go` cannot run.** All eight skills are user-invoked only, and the README and plugin text still describe the loop.

Bites later: `/park-it` commits everything under the five homes (F08); a re-plan deletes task files and frees their numbers (F11); a split resets a done part to sketched (F16); a part turns done without anyone checking its Outcome (F21); skipped interview questions take the default even when they are hard to reverse (F20); prototypes may not use tests even when the question is about behaviour (F25).

Do not fix F02, F09, F10, and F23. [Decision 0013](../decisions/0013-local-tasks-first.md) removes GitHub tracking from the first release, so that text should be deleted from the skills and templates rather than repaired.

### What the revision gets right

- [0012](../decisions/0012-atlas-owns-work-projects-own-delivery.md) and [0013](../decisions/0013-local-tasks-first.md) are removals. They take the tracker choice, branches, PRs, approvals, and merges out of four skills and delete four P1 findings outright.
- A status run that changes nothing ([0015](../decisions/0015-setup-adopts-routing-observes.md)).
- An interview that stops when the next work is safe to plan ([0020](../decisions/0020-decide-only-the-selected-scope.md)), with a short route for small work.
- A `review` and a `canceled` task status.
- Deferring `go`.

### Where the revision has grown too heavy

1. **The product is frozen while the process grows.** No `SKILL.md` has had a real edit since 2026-09-11. Since the review on 2026-09-13 the repository gained about 340 KB of plan, notes, and decisions around about 40 KB of skills. Two of 24 tasks are done and neither touched a skill. Three open tasks gate the first skill edit, 13 gate the router, 21 gate the release, and seven of those must run strictly one after another.
2. **Validation is last and should be first.** The draft has never been run. All 28 findings are source-level counterexamples, and the plan schedules the first cold run behind `work-skills/05`. One run of the 2026-09-11 test script on a scratch brand copy would sort the findings into observed and theoretical in a single session, and it gives the baseline that `validation/03` says it needs.
3. **Migration gates everything and protects nobody.** [core-model/03](../plan/core-model/03-migrate-current-projects.md) blocks all five work-skills tasks. The only legacy projects are the brand example and this repository.
4. **The voice has drifted from [0006](../decisions/0006-plain-words-over-jargon.md).** The draft says "Do one task, prove it, write down what you made." The revised glossary says a task is ready when "its required blockers are accepted and their exact needed outputs are accessible in a project-permitted workspace." The vocabulary went from about a dozen terms to about thirty. Acceptance, integration, delivery, project authorization, operation, method, context pointer, and work package are useful words for designing Atlas. They should not reach a shipped skill or template.
5. **Evidence has no light setting.** `core-model/01` needs about 550 words of Delivered and Review (547 counted), with revision hashes, to record that nine decisions were accepted. If that is the model task, a brand designer will not keep it up. [0019](../decisions/0019-acceptance-follows-output-and-scope.md) is right that a review must name what it looked at. One `Version:` line does that.
6. **A ninth command for the first minute.** `/atlas` on an empty folder is the most teachable move in the method. The same safety comes from one command with two files: `/atlas` stays read-only, and when homes are missing it lists them, asks before creating, and only then loads a `setup.md` kept beside its `SKILL.md`. Decision 0015 names this as its revisit case.
7. **A build system for four text files.** Methods as plain reference files beside the skills that use them is [0014](../decisions/0014-shared-methods-travel-with-consumers.md) in its simplest form. Source hashes, versions, and a generator can wait until a copy actually drifts. `methods/diagnosis.md` is good and is 5.7 KB, of which 1 KB is a licence; the consumer needs about ten lines at the moment a check fails.
8. **Context routing answers a cost nobody has measured.** A nine-part map is about 6 KB. The one real need is finding which file holds a split part, and that is one grep.
9. **The front page stopped teaching.** The README at `552af3a` had the loop diagram, the writes diagram, and the skills table. The current README describes the plan to revise Atlas. The brand example still says "See the Atlas README for what these lines mean", and the README no longer says.
10. **Atlas is not used to build Atlas.** This repository runs on `plan/PROMPTS.md` and a delivery policy, not on its own skills, so real use feeds nothing back.
11. **The second pass is parked though it fixes about half the P1 list.** `7f1f12d` has the `review` status, one table for ids and statuses, `(you)` on boxes, "the brief needs an answer" written to the map, a live-handoff rule, and a router that respects `Needs:`. Only its Git section conflicts with 0012.

### Recommended order

1. Run the draft once on a scratch copy of the brand example, following the 2026-09-11 test script. Record what broke as one note.
2. Ship a patch, 0.2: the seven faults above, the GitHub text deleted, the commit rule moved to one place, and the README front page restored. No new concepts. Most of it can be lifted from `7f1f12d`.
3. Use 0.2 to run the rest of this repository's work.
4. Resume the larger items with evidence from steps 1 and 3: setup as a reference file, methods as reference files, the part outcome check, re-plan with cancel, and validated handoffs.
5. Release when a cold run passes on the brand example and on one code fixture.

### Changes for every skill

1. One table for ids and statuses in `plan/README.md` (todo, doing, review, done, canceled). Skills point to it.
2. One home for the commit rule: a short paragraph in the Atlas block of `CLAUDE.md`, owned and editable by the project, with the default "commit what each command wrote, message `<command> <id>: <what>`, never push". Delete the commit step from seven skills. This is 0012 in its smallest form.
3. Delete the `Tracker:` and `Merge:` lines and every GitHub branch from skills and templates.
4. Reads that survive a missing folder (N1).
5. A missing-home message that names every missing home.
6. One `atlas: N` number covers all the formats. `/atlas` reports an older project format and changes nothing.
7. Shipped skills and templates keep the draft's voice and its dozen words.

### Changes per skill

**`/atlas`.** Keep the five lines, the fixing command beside each problem, and the single entry point.
- Fix now: shell-safe reads (N1). Copy the five homes only, and start with a truly empty map and glossary (F06). Follow the newest handoff, not the newest note, and only while its target is still open (F05). Route on "decided part with zero tasks" (F01). Add routes for a task in review and for a doing task with findings or an open question (F03). Take `go` out of the skill, the README, and the plugin text (F12, F13). Delete the tracker question, the merge guess from `git shortlog`, and `gh issue list`.
- Next: a status run changes nothing. Give the two status repairs to `/map-it`, which already owns keeping the map true. Put setup in `setup.md` beside the skill, ask before creating, list what is missing in a half-made project, and never delete `CONTEXT.md` (copy its terms and say so) (F06, F07). Write the block once when `AGENTS.md` and `CLAUDE.md` are one file (F07). Report a part that is done with open tasks, and a doing task with an empty Delivered.

**`/interview-me`.** Keep draft before asking, writing as answers land, concrete cases at boundaries, and the brief written last.
- Fix now: an argument that matches nothing asks "new part or typo?" and shows the closest ids (F20). Check `Needs:` before deciding a part (F15). Mark hard-to-reverse questions; a skipped one stays open (F20). Five questions a round, one line per option (N4). Start `brief.md` as a draft in round one so an interrupted interview loses nothing (F20). Stop when the next work is safe to plan, and leave later questions on the part with an owner (0020). Print `Next:` for the first sketched part whose `Needs:` are decided.
- Next: re-interviewing a building part lists the tasks the change touches. Propose a glossary term only when the distinction changes a decision (F19). Pick one test for what earns a decision file; the template says all three, this repository's README says any one (F17). Read `glossary/*.md` when the glossary is split.

**`/plan-it`.** Keep the three task tests, the thin first task through every layer, the single sizing round, and never reusing a number.
- Fix now: with no argument, pick the decided part with a brief and zero tasks (F01). Put `(you)` on Done when boxes (N2). Cancel a task, never delete it: `status: canceled` and one line of reason; stop when a doing or done task depends on it (F11). Read the full body of any task it edits (F11). Check the graph after writing: no cycle, no self-block, every blocker exists (F15).
- Add: the small-work route, `/plan-it <part> "<one task>"`, one task under the existing brief and no sizing round (N6, 0020).
- Remove: parent issues, sub-issues, labels, and native dependencies.

**`/build-it`.** Keep one task per run, "the way this project already makes that kind of thing", Delivered as claims a reviewer can check, and never editing the brief.
- Fix now: set `status: review` after Delivered (F03, F04). Accept a doing task: read Delivered so far, the findings, and the open question, then resume (F03). Refuse a todo task with unfinished blockers and name them (F15). When Check by fails, write the failure in Delivered, tick nothing, leave the task doing, and load the diagnosis reference only then. When the brief is wrong, write the question on the part's open questions so `/atlas` routes to the interview.
- Next: end Delivered with one `Version:` line, a commit hash in a repo or a checksum of the delivered files elsewhere (0019 at its lightest).
- Remove: step 3 and the GitHub halves of steps 2, 6, and 7.

**`/review-it`.** Keep the two checks, the fresh context, findings that cite a line, and findings going back to the builder.
- Fix now: pick by `status: review` (F04). Give the reviewer the task, the brief, the delivered files, the project instructions, and neighbouring work of the same kind, and drop "nothing else" (F22). Do not hold the session for `(you)` boxes: leave the task in review, say what to look at, print `Next: /review-it <id>`; a ticked `(you)` box counts as confirmed (N3). With findings, set the task back to doing. A finding says what is wrong, where, and what fixes it (F22). The Avoid check skips quotations and outside names (F19).
- Next: on a part's last task add check three, the brief's Outcome against everything delivered; a part with zero tasks is never done (F21). Compare the `Version:` line before reviewing and say "changed since delivery" when it differs (F04).
- Remove: approve, squash merge, branch delete, and the `Merge:` line (0012, F10).

**`/prototype-it`.** Keep one question, the smallest made thing, the verdict written back to the map, and the note.
- Fix now: take a part id, or nothing when exactly one `(prototype)` question exists; quoting the question becomes optional (N5). Allow tests, persistence, or error handling when they are what the question is about (F25). Verdicts are yes, no, or inconclusive with the next experiment (F25). State a bound before making. A same-day rerun gets a suffix (F26). Drop "Only `/atlas` reads notes" from the notes format (F26).
- Next: anything copied out of a prototype goes through a normal task and review.

**`/park-it`.** Keep "the note holds only what no home holds", the exact `Next:` shape, and the no-secrets rule.
- Fix now: commit the note and what this session's commands wrote; list other uncommitted changes in the note (F08). Record the exact target: task id, status, files in flight, folder or branch (F05). Add a time or suffix when a handoff from the same day exists (F26).
- Next: when every home is current, print `Nothing to park.` and stop.

**`/map-it`.** Keep sections as the truth, the drift report, and the nine-part ceiling.
- Fix now: check before drawing: a cycle in `Needs:`, a part that needs itself, a duplicate id, a missing part (F15). Take over the two status repairs from `/atlas`.
- Remove: the glossary diagram, or make it optional. "An edge to each term its definition names" cannot be checked for multi-word terms, this repository's own diagram already breaks the rule (F19), and it costs a redraw at the end of every interview (N7).
- Next: a split is a migration of the brief, tasks, decision `part:` lines, and incoming `Needs:` to named sub-parts, and it never resets a done part (F16). Until that exists, say "not supported yet" rather than ship a lossy split. Add rename.

### Choices for Vitali

1. **Patch the draft now, before the remaining 22 tasks?** A: yes, 0.2 with the seven faults (one or two sessions, real use starts). B: no, keep the package order (nothing usable for weeks). ➡️ A.
2. **Setup.** A: one command, two files; `/atlas` asks before creating. B: a separate `/setup-atlas` (a ninth command and a worse first minute). ➡️ A, using the revisit line in 0015.
3. **Evidence weight.** A: one `Version:` line. B: revision-bound records as in `core-model/01` (accurate, and too heavy for non-code work). ➡️ A as the default; B stays available to a project that wants it.
4. **`core-model/03` gating all skill work.** A: unblock; with no adopters, migration is a short "what changed" note. B: keep. ➡️ A.
5. **Context routing in the first release.** A: defer the package and keep the split-part lookup. B: keep both tasks. ➡️ A.
6. **The glossary diagram.** A: drop it. B: optional. C: keep. ➡️ A or B.
7. **Which voice ships.** A: the draft's voice and its dozen words, with the design vocabulary kept inside this repository. B: the revised glossary everywhere. ➡️ A, plus one release check: a non-programmer can read every template without a dictionary.

### Limits

This is a static review with a few mechanical checks. It ranks faults by how early an ordinary run would meet them, which a real run may reorder. The recommendations touch accepted decisions 0014, 0015, 0016, and 0019; nothing here changes their status.

## Copied into
Answers given the same day. Choices 1 and 4 were accepted and recorded as [decision 0021](../decisions/0021-patch-the-draft-first.md), carried out by [work-skills/06](../plan/work-skills/06-patch-the-draft.md). Choice 2 went the other way: setup stays a separate `/setup-atlas`, as [0015](../decisions/0015-setup-adopts-routing-observes.md) already says, because a user-invoked skill and a file beside it both cost nothing until used, and `/atlas` runs far more often than setup. Choice 3 was analysed in the [evidence weight note](2026-09-17-research-evidence-weight.md). Choices 5 to 7 were still open when this was written. A visual guide built from this note was published to Vitali's private Claude artifacts.

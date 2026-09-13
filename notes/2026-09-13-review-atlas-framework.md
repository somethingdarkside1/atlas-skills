---
date: 2026-09-13
kind: review
part: project
---

# Atlas framework review and proposed revision

## Summary
Atlas has a useful project model and an unusually coherent place for an agent's durable knowledge, but its written workflow cannot yet reliably distinguish delivery, review, interruption, and completion. Keep the five things and strengthen the transitions between them before adding more skills or promising unattended operation. This review explains the current design, records source-backed problems across all eight skills, compares alternative approaches, and links a prioritized local plan for a revised release.

## Detail

### Scope, evidence, and limits

Reviewed the working tree based on commit `374430e`, all eight `SKILL.md` files and their invocation metadata, all six bootstrap template files, root formats, eight decisions, three historical handoffs, the brand example, plugin manifests, and the local linking script. Four user edits were already present: `CLAUDE.md`, `GLOSSARY.md`, `plan/README.md`, and `skills/atlas/SKILL.md`. They are part of the observed design and were preserved. In particular, the glossary's broader Decision definition and the plan's impact-based selection are live edits, rather than unexplained changes introduced by this review.

This is a static design and consistency review, supplemented by local manifest validation, file checks, and dependency validation of the new plan. Scenarios below are source-level counterexamples, not claims that every agent has been observed failing. Natural-language skills leave room for an agent to repair a contradiction implicitly; that dependence on improvisation is itself the reliability problem. No production project, GitHub issue, PR, merge, or installed skill was changed to test these scenarios.

The [separate research note](2026-09-13-research-matt-pocock-comparison.md) distinguishes the available Matt Pocock reference from verified upstream sources. A locally declared version does not establish identical upstream content. Comparative judgments concern mechanisms in the inspected sources; they are not measured rankings of agent outcomes.

Finding labels below mean:

- **Confirmed:** directly inconsistent instructions, missing required evidence, or a verified platform incompatibility.
- **Gap:** a consequential case for which the written workflow has no complete rule.
- **Proposal:** a design change to evaluate and adopt deliberately.

Urgency is about release sequencing: **P1** can lose work, stall an ordinary workflow, or misreport completion; **P2** affects correctness or usability in less immediate paths; **P3** improves maintainability or teaching. This is not a security severity scale.

### How the framework works as a whole

Atlas combines a project knowledge model with an execution process. The knowledge model is the five things. The process is an interview that settles a part, a brief that captures the outcome, tasks that divide the work, a builder that produces evidence, and a reviewer that checks the result. A router chooses the next action; map maintenance, experiments, and handoffs support that loop.

That separation is its strongest idea. A handoff can disappear from attention without erasing a settled term or choice. A person can inspect the work without learning an agent's internal tools. The brief belongs to the interview, which has the context to retain small settled choices. Task checks work for SVG, copy, and software. Derived Mermaid diagrams give people a view of the same material an agent edits.

However, Atlas currently distributes its execution rules across skill bodies, root formats, templates, prose definitions, metadata, and old handoffs. The files are individually short, but a reader must reconcile all of them to answer basic questions such as: can a doing task be resumed, is a closed issue complete, and does a changed brief invalidate a review? The apparent simplicity comes partly from leaving those questions implicit.

The five homes reduce duplication of project knowledge. They do not yet provide one authority for workflow behavior. Defining that authority is the first revision, rather than expanding every skill independently.

### What to preserve

1. **Visible, portable project memory.** The five things are comprehensible without the original agent or an external service. Keep the local project model even when work is tracked remotely.
2. **A brief written where decisions happen.** [Decision 0008](../decisions/0008-the-interview-writes-the-brief.md) closes a real handoff gap. Preserve it and add intermediate capture for interviews that span sessions.
3. **One home for the work.** [Decision 0001](../decisions/0001-one-home-for-the-plan.md) correctly rejects a casual files/issues mirror. A tracker adapter can preserve this choice without duplicating every rule in every skill.
4. **Complete tasks and observable checks.** `Delivers`, `Check by`, and `Done when` are a strong medium-independent interface. Improve their evidence and revision semantics rather than replacing them with a large ticket template.
5. **A map that a person can edit.** The sections are authoritative and the diagram is derived. Preserve this direction of derivation.
6. **Short procedural skill bodies.** They should name relevant inputs, the action, and the completion condition. Move substantial conditional mechanics into reachable references; measure reliability before treating line count as success.
7. **A small public command set.** Eight commands are enough for the present experiment. Add a command only when it has a distinct user decision or a repeated routing failure.

## Workflow failures

### F01. A brief can make an unplanned part look planned

**Confirmed, P1.** Interview step 9 sets `Plan:` to the new brief's folder or parent issue. Plan step 1 chooses, without an argument, a decided part with no `Plan:` yet. Atlas step 4 routes a decided part "without a plan" to planning. The explicit interview-to-plan command can succeed, but stopping after the interview leaves a part with a brief, a Plan link, and zero tasks that does not meet the plan skill's stated automatic selection rule.

Use separate predicates: brief exists, tasks have been created, and at least one task is ready. A folder or parent issue is a location, not evidence that planning is complete. See [planning entry](archive/2026-09-13-initial-review/plan/plan-skill/01-make-planning-repeatable.md) and [routing](archive/2026-09-13-initial-review/plan/atlas-skill/02-route-from-current-state.md).

### F02. A normal GitHub start can dirty its own preflight

**Confirmed, P1.** [Build steps 2 and 3](../skills/build-it/SKILL.md) assign the issue and edit a decided part's map status before requiring a clean tree and creating the branch. On the ordinary first task of a decided part, Atlas itself makes `MAP.md` dirty before the clean-tree check. Assignment can survive a subsequent failure. Even if an agent quietly commits the map, the skill has not defined which branch contains that change.

Resolve the repository, fetch, select or resume the branch, and verify the permitted starting state before recording progress. Treat the local change and external claim as a recoverable sequence. See [GitHub start](archive/2026-09-13-initial-review/plan/build-skill/02-make-github-start-recoverable.md).

### F03. Doing covers several states the router cannot distinguish

**Confirmed contradiction plus gap, P1.** Build reads ready tasks as `todo` with completed blockers. Review step 6 leaves findings on a `doing` task and returns `Next: /build-it <id>`. Build also returns that command when waiting for an answer, leaving doing. An explicit argument might be interpreted as permission to resume, but its eligibility and branch reuse are unspecified, while its ready-only instructions point the other way. Atlas has no general route for interrupted doing work. The brand fixture already contains such a task. A failed Check by or missing verification tool also needs a recorded failure or blocked attempt and a clear retry route; treating the absence of a runnable check as successful verification would be incorrect.

Distinguish active work, waiting for an answer, ready for review, and changes requested through an explicit transition record. Define argument validation and resumption. See [build retry](archive/2026-09-13-initial-review/plan/build-skill/01-support-resume-and-fixes.md).

### F04. Review freshness is undefined for file tasks

**Confirmed, P1.** [Review's read-first section](../skills/review-it/SKILL.md) requires Delivered to be newer than the last Review pass. The file format provides neither a delivery revision nor a timestamp. A dated review cannot establish whether a subsequent artifact edit occurred. File modification time applies to the whole task and changes when the review is appended. GitHub comment timestamps give order, but do not bind the pass to the PR head or brief revision.

Bind delivery to an artifact revision, review to that delivery and the brief revision, and invalidate approval when either changes. Use file hashes or explicit revisions when Git is absent. See [review evidence](archive/2026-09-13-initial-review/plan/review-skill/01-bind-reviews-to-deliveries.md).

### F05. A stale handoff outranks current work indefinitely

**Confirmed, P1.** [Atlas step 4](../skills/atlas/SKILL.md) gives the newest note's handoff command first priority. There is no consumed marker or comparison with current state. A completed task can therefore remain the next command. A newer prototype note also hides an older handoff entirely, because only the newest note is read when it happens to be a handoff. Date-only filenames do not order multiple sessions on the same day.

Use a handoff as a candidate action, validate its target, and prefer current task evidence. Give handoffs stable identity and deterministic ordering. Keep the historical note immutable. See [handoff](archive/2026-09-13-initial-review/plan/side-skills/02-make-handoffs-resumable.md) and [routing](archive/2026-09-13-initial-review/plan/atlas-skill/02-route-from-current-state.md).

### F06. Partial initialization has no safe recovery path

**Confirmed, P1.** [Atlas step 1](../skills/atlas/SKILL.md) treats absence of `MAP.md` as a fresh folder and copies the templates, even when other homes exist. Step 2 says later runs never recreate. A project with a map but a missing plan README can therefore be sent to `/atlas` by another skill, only for `/atlas` to leave the required file absent. The existence prechecks in other skills cover only some of the files they need. Bootstrap also leaves a literal First part and glossary placeholders unless the agent infers a cleanup step, so a freshly created map is not the empty map described by the router. The template-selection rule should distinguish the five project homes from the instruction-block fragment.

Inventory every managed path before writing. Create missing files using existing context, preserve populated homes, and report incompatible existing files with a specific recovery action. This is initialization of missing state, not permission to replace project content. See [bootstrap recovery](archive/2026-09-13-initial-review/plan/atlas-skill/01-recover-partial-initialization.md).

### F07. Bootstrap migration can discard non-glossary context

**Confirmed unsafe instruction, P1.** Atlas step 1 moves `CONTEXT.md` entries into the glossary and deletes the original. That file can contain relationships, invariants, or other material excluded by Atlas's own glossary rules. The skill has no inventory, mapping, backup, or reference update. The current repo also uses `AGENTS.md -> CLAUDE.md`; a procedure that independently appends to both existing paths needs to recognize that they can name the same file.

Adopt existing context by classifying its content into the five homes, retaining provenance, verifying coverage and inbound links, and treating source removal as a separately reviewable migration step. Deduplicate instruction-block writes by resolved path. See [bootstrap recovery](archive/2026-09-13-initial-review/plan/atlas-skill/01-recover-partial-initialization.md).

### F08. File selection does not establish ownership of changes

**Confirmed, P1.** [Park step 3](../skills/park-it/SKILL.md) stages everything under the five things and prototypes, conflicting with the repo's instruction that each skill commits only what it wrote. Other skills stage "the files you wrote," which still includes unrelated edits when both a user and a skill touch the same file. Build can change the map, glossary, and decisions, but its commit step names delivered files and the task without explicitly accounting for all those mutations. A commit after a hook failure also needs a recoverable state rather than a claim of completion.

Capture a starting diff, track owned changes, and verify the exact staged diff before commit. Retain task and artifact paths in the receipt. Handoff should preserve the user's uncommitted work as information, with a concrete authorized scope for any commit. See [owned writes](archive/2026-09-13-initial-review/plan/build-skill/03-preserve-owned-changes.md) and [handoff](archive/2026-09-13-initial-review/plan/side-skills/02-make-handoffs-resumable.md).

### F09. GitHub's fields do not equal Atlas completion

**Confirmed, P1.** [The plan format](../plan/README.md) defines open/unassigned as todo, open/assigned as doing, and closed as done. It also says a task is done only once merged. A canceled or manually closed issue satisfies the first definition and fails the second. A person can assign planned work before beginning it, while the builder's account may already be assigned to many tasks. A native blocker being closed does not prove its required deliverable exists.

Define Atlas's state first, then specify the evidence the GitHub adapter reads. Ownership and lifecycle should have distinct meanings. Canceled work should have an explicit disposition rather than releasing a dependency as successful delivery. See [contract](archive/2026-09-13-initial-review/plan/five-things/01-settle-workflow-contract.md) and [GitHub completion](archive/2026-09-13-initial-review/plan/review-skill/02-verify-github-completion.md).

### F10. Automatic GitHub review assumes an impossible self-approval

**Confirmed platform mismatch plus gaps, P1.** Review step 5 approves a clean PR. GitHub prevents a PR author from approving their own PR, and build and review will often share the same authenticated account. An independent model context is not a separate GitHub reviewer identity. See [GitHub's review rules](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request).

A review report can still be useful without an approving API call. Determine account capability, respect required checks and review policy, and distinguish a clean Atlas report from approval and merge. Pin the checked head, recheck after updates, and verify merge before completion. The current step also does not establish where a local completion-map commit belongs after deleting the task branch. See [GitHub completion](archive/2026-09-13-initial-review/plan/review-skill/02-verify-github-completion.md).

### F11. Replanning can rewrite history or claim canceled work succeeded

**Confirmed, P1.** [Plan step 3](../skills/plan-it/SKILL.md) removes todo tasks and fixes every blocker naming them, but also leaves doing/done tasks untouched. A doing task that references the removed task makes those rules incompatible. Deleting the highest task number destroys the evidence needed to prevent reuse on a later run. Closing a removed GitHub task is interpreted as done under the current tracker mapping. Frontmatter-only reads are insufficient to revise a todo task's outcome or preserve human edits to its checks.

Read full bodies for tasks under revision; retain cancellation history and stable ids; inspect all incoming dependencies; report affected active work. Evaluate changed briefs against existing delivery rather than silently treating it as current. See [replanning](archive/2026-09-13-initial-review/plan/plan-skill/02-preserve-replan-history.md).

### F12. Explicit-only skills prevent the advertised automatic loop

**Confirmed platform mismatch, P1.** All eight skills set `disable-model-invocation: true`; their Codex metadata also disables implicit invocation. Atlas step 5 nevertheless tells the agent to run build and review itself. Claude's current documentation explicitly makes these skills user-invoked and bars an agent from working around that boundary by reproducing the skill. See [Claude's invocation controls](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill).

Choose one compatible design: keep the public router manual, expose selected worker skills for agent invocation, or supply a separately authorized orchestration procedure with its own supported entry point. Test the choice in each advertised harness; changing metadata alone does not establish safe transitions. See [go and invocation](archive/2026-09-13-initial-review/plan/atlas-skill/03-align-go-with-invocation.md).

### F13. The automatic loop has no general progress or waiting guard

**Gap, P1.** Three review passes with findings is a useful local bound. It does not bound repeated clean reviews waiting for a human merge, repeated routing to a consumed handoff, build failure before review, or a task waiting for an answer. Atlas's priority table does not clearly let blocking validation problems stop automatic work.

Require a changed task or delivery revision after each automatic step. Stop on a pending human action, failed prerequisite, unchanged state, or a user-specified run limit. Persist the reason and exact resumable target. See [go and invocation](archive/2026-09-13-initial-review/plan/atlas-skill/03-align-go-with-invocation.md).

## Model and consistency issues

### F14. Map shape conflates ownership and decision order

**Gap and proposal, P2.** `Needs:` means a part must be decided first. It does not model runtime connections, data ownership, interfaces, or rollout order. Labeling this one diagram as the entire shape of any system can hide essential relationships. The user's glossary edit adds a "target state" to Map, while the actual map format has no separate target-state field. A purpose sentence alone does not distinguish the current and intended design.

Keep the decision dependency map legible. Add brief-level current/target context and concrete interface or outcome boundaries where useful. Let a part link an additional diagram when relationships require it. First test whether that resolves real projects; a universal architecture schema would be premature. See [contract](archive/2026-09-13-initial-review/plan/five-things/01-settle-workflow-contract.md).

### F15. Graph constraints are incomplete

**Confirmed omissions, P2.** Atlas reports missing task blockers; map-it reports missing part ids and duplicates. Neither gives a complete rule for cycles, self-dependencies, an unplanned prerequisite, empty child sets, or duplicate task ids. Interview reads `Needs:` but does not enforce eligibility before deciding a part. Build's explicit task selection does not specify validation of blockers or part state. At the start of this review, the root map was `flowchart TB` despite its format requiring `LR`; the documentation update corrects its orientation.

Validate both dependency graphs, with actionable cycle paths and missing targets. Render from validated data. Scope the meaning of Needs to decision readiness; task dependencies remain the build order. See [map validation](archive/2026-09-13-initial-review/plan/map-skill/01-validate-graphs-and-views.md) and [planning](archive/2026-09-13-initial-review/plan/plan-skill/01-make-planning-repeatable.md).

### F16. Splitting or renaming a part lacks migration semantics

**Confirmed gap, P2.** [Map step 5](../skills/map-it/SKILL.md) creates sketched children and reduces the parent section to a status and link. It does not redistribute the parent's brief, tasks, decisions, Needs, or incoming links. A done part can become sketched after aggregate recomputation. A cross-file Needs edge can cause Mermaid to introduce a node that lacks a section in that diagram. Other skills mostly read root sections and write root `MAP.md`, so nested parts are not consistently reachable. Glossary splitting is prescribed by the format, but skill readers do not load `glossary/*.md`.

Define a shared resolver for stable part ids and their owning file. Specify parent/child ownership, summary edges, existing task retention, and rename references. Separate zooming a view from changing the decomposition of work. See [part migration](archive/2026-09-13-initial-review/plan/map-skill/02-preserve-split-part-identity.md).

### F17. Decision criteria disagree across authoritative files

**Confirmed, P2.** The working glossary uses hard-to-reverse **or** material impact **or** future surprise. The decisions README and its template require hard-to-reverse **and** surprising **and** a real trade-off. Skills defer to the latter, while the agent block asks to record hard-to-reverse choices. These rules can produce different persistence for the same answer. The map initially omitted decision 0008 from the interview part's links; the documentation update restores that link. Proposed and superseded decisions need distinct treatment by builders and reviewers.

Recommended rule to settle: record a consequential choice with rationale and reconsideration conditions; represent proposal, acceptance, and supersession explicitly. A material, surprising, or difficult-to-reverse choice can justify a decision. Keep ordinary reversible choices in the brief. Preserve the user's current wording while the contract task reconciles its consumers. See [contract](archive/2026-09-13-initial-review/plan/five-things/01-settle-workflow-contract.md).

### F18. Self-describing files need a versioned distribution policy

**Confirmed gap, P2.** Templates and adopted project formats are necessarily separate copies, but only the agent instruction block has an `atlas:` version. Updating that block does not update task schemas or map rules. The root plan has an impact-based selection option absent from its bootstrap template and builder; examples carry additional snapshots. There is no declared boundary between project customization and an obsolete format.

Version the portable format, define the owner of each invariant, and provide migrations as inspectable changes. Treat templates as distributable sources and project formats as versioned instances with documented overrides. Preserve backward reading during rollout. See [format migration](archive/2026-09-13-initial-review/plan/five-things/02-version-and-migrate-formats.md).

### F19. The glossary risks becoming a word-policing layer

**Confirmed tension and proposal, P2.** Glossary format excludes general concepts, yet interview step 5 requires every question to rest on words the glossary owns and proposes an entry for every new word appearing in a task. Review forbids every Avoid synonym without context, including quotations or the names of external APIs. The glossary's relation graph is inferred from words occurring in definitions, which requires semantic judgment and consistent handling of multiword terms; it is not a reliable regex derivation.

Use the glossary to resolve project-specific ambiguity, invariants, and confusable neighbors. Preserve names imposed by external systems. Require entries where a distinction changes a decision or behavior. Define whether semantic relationships are authored or inferred and reviewed. The root glossary already illustrates the mismatch: its diagram links Task to Ready, although the Task definition never names Ready. A relationship that is sensible to a reader can still violate the specified derivation rule. See [interview quality](archive/2026-09-13-initial-review/plan/interview-skill/01-sharpen-interview-decisions.md) and [map validation](archive/2026-09-13-initial-review/plan/map-skill/01-validate-graphs-and-views.md).

### F20. Interview settlement has no bounded uncertainty model

**Gap, P2.** "Until nothing is left to guess" and open questions `none` encourage either endless interrogation or premature certainty. Eight elaborate questions can impose substantial cognitive load. Skipped questions become recommendations by default, even when they concern consequential choices. Earlier small settled choices are only guaranteed a home when the final brief is written, so an interrupted interview can lose them. An unmatched argument silently creates a new part, including a typo. A re-interview of a building part changes its brief without classifying affected tasks; a done part's reopening behavior is undefined. GitHub parent-issue creation does not specify updating the existing parent.

Separate facts the agent can discover, delegated reversible choices, decisions requiring a person, and explicit unresolved assumptions. Ask the highest-consequence uncertainty first. Persist a draft brief or equivalent settled-choice record between rounds. Finish when the next work is safe to plan within stated assumptions. See [interview quality](archive/2026-09-13-initial-review/plan/interview-skill/01-sharpen-interview-decisions.md) and [brief revision](archive/2026-09-13-initial-review/plan/interview-skill/02-preserve-brief-revisions.md).

### F21. Completion at task level does not prove the part's outcome

**Gap, P2.** A task can pass every local box while the combined output misses the brief's Outcome. Atlas sweeps parts to done when their tasks are done. With no explicit nonempty-task condition, even a part with zero tasks can be misread as satisfying "all tasks done." Reopening work, adding a task to a done part, changing scope, and superseding a key decision lack reverse transitions.

Require an actual planned scope, current accepted evidence for its required tasks, and a proportional final check of the part's outcome. Reopen explicitly when new accepted scope invalidates completion. Distinguish delivery from release or publication when the domain needs it. See [part completion](archive/2026-09-13-initial-review/plan/review-skill/03-check-part-outcomes.md).

### F22. Review context is both under-specified and over-restricted

**Confirmed tension, P2.** Review step 2 gives a fresh reviewer only the task id and says to read the brief, decisions, glossary, Delivered, and delivered thing, "nothing else." Step 3 then expects knowledge of existing project conventions and documented standards. A task id also does not establish the change baseline, task location, actual artifact revision, or applicable project instructions. One-sentence findings citing only a brief line or glossary entry cannot always explain a code regression, design mismatch, or failed check.

Give the reviewer the review target and access to applicable project rules, neighboring implementation, and checks. Keep builder rationale optional so it does not bias the first pass. Require evidence, impact, and an actionable repair for each finding; use only as much prose as that requires. See [review evidence](archive/2026-09-13-initial-review/plan/review-skill/01-bind-reviews-to-deliveries.md).

### F23. GitHub mode needs an adapter, not repeated shorthand

**Confirmed omissions, P2.** Atlas's listed `gh issue list` command returns number, state, and assignees, but not sub-issue membership, blockers, delivery/review revisions, or merge evidence. The CLI defaults to 30 issues. A project beyond that size can disappear from status without pagination. See [the CLI manual](https://cli.github.com/manual/gh_issue_list). Issue dependency endpoints are separately paginated; see [GitHub's dependency API](https://docs.github.com/en/rest/issues/issue-dependencies).

Specify repo selection, all-page reads, labels, parent/sub-issue lookup, dependencies, permissions, and recoverable partial writes in one conditional reference. Use find-or-update semantics when rerunning after issue creation or a network failure. GitHub branches do not themselves provide exclusive task claiming or coordinate simultaneous edits to shared homes. See [GitHub start](archive/2026-09-13-initial-review/plan/build-skill/02-make-github-start-recoverable.md) and [completion](archive/2026-09-13-initial-review/plan/review-skill/02-verify-github-completion.md).

### F24. Tracker and Git workflow are coupled for convenience

**Proposal, P2.** [Decision 0007](../decisions/0007-branches-only-with-github.md) intentionally connects files with in-place commits and GitHub with branches and PRs. This saves instructions but excludes a useful case: local task files with a reviewed code branch. Conversely, a GitHub task can describe a document or service change with no natural code PR. "Nothing else changes" between trackers is therefore inaccurate.

Retain one tracker, but evaluate Git workflow as a separate project preference after the current lifecycle works. Start with two documented supported combinations rather than implementing a provider framework. Record a superseding decision only if the user adopts this trade-off. See [workflow separation](archive/2026-09-13-initial-review/plan/five-things/03-evaluate-tracker-and-git-policy.md).

### F25. Prototype rules rule out some useful evidence

**Confirmed tension and proposal, P2.** Prototype step 2 says no tests, persistence, or error handling. A prototype of a race, state model, import, or recovery path may need exactly those mechanisms to answer its question. The verdict always needs human confirmation even when the question is an objective measurement. There is no time/cost bound, falsifying observation, or inconclusive outcome. The glossary allows tasks to copy prototype code, while the skill calls it a thing nobody will keep; copied code needs normal delivery checks.

State the question, smallest discriminating experiment, time budget, observation, limits, and verdict. Match verification to the question. Let the person own preference judgments and let measured facts be recorded directly when authorized. Include an inconclusive result and a next experiment. See [prototype evidence](archive/2026-09-13-initial-review/plan/side-skills/01-make-prototypes-conclusive.md).

### F26. Note access rules contradict the evidence workflow

**Confirmed, P2.** [Notes format](../notes/README.md) says only Atlas reads notes and only the newest handoff. Prototype answers explicitly link a note for the interview to use, and the brand task's Check by points to a prototype note. Notes are also called write-once but allowed to change on their creation day. Prototype folders and note filenames can collide on repeated same-day runs.

Allow skills to read explicitly relevant evidence notes. Define completion of a note separately from its date, use a unique suffix or time for repeated runs, and record later corrections as new linked notes. Preserve artifact pointers and experiment limits. See [handoffs](archive/2026-09-13-initial-review/plan/side-skills/02-make-handoffs-resumable.md) and [format migration](archive/2026-09-13-initial-review/plan/five-things/02-version-and-migrate-formats.md).

### F27. Skill authoring rules reward formal compliance over useful behavior

**Confirmed, P3.** The repo requests a three-line `openai.yaml`, but the skeleton and all eight actual metadata files have five lines. The skills checklist requires every step's observable completion, yet several terminal print steps have no such condition. The map skill restates format details despite the rule that formats remain in their homes. All skills need a missing-file stop, but Atlas is the skill that creates those files. A universal one-line failure can hide several failed prerequisites; five lines of status conflicts with multiple problem lines. Positive-only instructions coexist with many prohibitions.

Make the checklist express behavioral obligations and justify exceptions explicitly: initialization has different prerequisites, a status report has five fields rather than five physical lines, and a failure carries the information needed to resume. Positive prose is a useful editing preference, not proof that a skill is safe or clear. See [authoring contract](archive/2026-09-13-initial-review/plan/packaging/01-align-authoring-and-installation.md).

### F28. The example and packaging overstate readiness

**Confirmed, P2.** The brand example claims delivered `wordmark/candidates.svg`; that file is absent. Its doing task lacks a delivery, and the later usage page is also absent. Its completed review is undated and does not use the two check headings. Its glossary diagram includes Palette without a definition and includes relationships inconsistent with the definition-edge rule. The repo description called it finished; the old README called one part decided while the example says building. Root skill statuses say building despite having no tracked doing tasks before this review.

The package's flat `skills/<name>/SKILL.md` layout is valid under [Claude's default skill discovery](https://code.claude.com/docs/en/plugins-reference#skills); absence of a custom `skills` field is not a defect. The old README did omit the separate plugin-install step. `scripts/link-skills.sh` replaces existing same-name symlinks and can treat an existing directory as a destination, without a collision report or uninstall plan. No release note establishes fresh-profile installation or runtime smoke-test results.

Keep the example labeled as illustrative until it contains verifiable work. Add fixture variants for each lifecycle boundary and test installation in an isolated profile. See [examples](archive/2026-09-13-initial-review/plan/packaging/02-build-realistic-fixtures.md) and [installation](archive/2026-09-13-initial-review/plan/packaging/01-align-authoring-and-installation.md).

## Skill-by-skill review

This table identifies what each skill should own after revision. Each row is a proposed contract, rather than replacement instructions already installed.

| Skill | Keep | Revise its input and action | Completion and recovery | Linked findings |
|---|---|---|---|---|
| `/atlas` | One place to discover next work | Load a normalized snapshot of relevant homes; separate inspection, initialization, and explicit repair modes; route from validated current state | Report exact blockers and candidate action; a repeated inspection preserves state; automatic steps demonstrate progress | F01, F05-F07, F12-F13, F15, F21, F23 |
| `/interview-me` | Draft before questioning; brief written by the interviewer; concrete cases | Enforce prerequisite readiness; distinguish facts, assumptions, delegated choices, and human decisions; retain settled choices between rounds; reuse an existing brief/parent | Stop when the scoped next work is clear within recorded assumptions; revision names affected tasks and decisions | F17, F19-F20 |
| `/map-it` | Sections own meaning; diagrams are views | Resolve every part and term across split files; validate graphs; separate visual redraw from a structural split or rename | Views agree with valid sections; identity and links survive structural edits; semantic ambiguity is reported for decision | F14-F16, F19 |
| `/plan-it` | Vertical delivery slices; one sizing conversation | Distinguish brief-only from planned; read tasks being revised fully; preserve ids and cancellation history; validate complete dependency graph | Every task traces to scope, has a useful check and valid blockers; reruns update existing work without duplicates | F01, F11, F15, F21, F23 |
| `/build-it` | One task, medium-appropriate work, verifiable Delivered | Validate a new task or resume an existing attempt; prepare workspace before claiming; record owned changes and a delivery revision; apply relevant specialist methods | Output and evidence exist; unresolved work is explicitly resumable; partial commits or API calls have a recovery target | F02-F04, F08-F09, F23-F24 |
| `/review-it` | Brief and conventions as distinct checks; fresh context when supported | Receive a fixed review target plus project rules; assess current evidence and regressions; separate report, approval, merge, and part acceptance | Findings are actionable; a clean pass identifies exact delivery and brief; human wait is durable; completion is verified | F04, F09-F10, F21-F22 |
| `/prototype-it` | One empirical question; small artifact; verdict feeds interview | Declare the experiment and limit; use a suitable method; distinguish observed facts from preference and inconclusive evidence | Artifact, observations, limits, and verdict are linked; next action follows the result; repeated runs preserve earlier evidence | F25-F26 |
| `/park-it` | A handoff contains session context missing from homes | Record exact task/branch/artifact pointers and unresolved interaction; commit only the agreed owned changes; use unique note identity | A fresh reader can validate and resume the target; current state outranks a stale instruction | F05, F08, F26 |

### Read dependencies and useful disclosure

The universal requirement to read the entire glossary and map on every turn will become expensive as a project grows. Keep an always-visible pointer to the project model, then load the relevant part, terms, accepted decisions, and task. A compact index can identify which split file owns an id. Specialized tracker instructions belong in a reference reached only for that tracker. Shared rules should be reachable by file path even when a public skill is explicit-only.

The proposed execution sequence for any mutating skill is: resolve its target and context, validate prerequisites, perform the owned transition, record evidence, verify resulting state, and return a resumable next action. This is a common interface, not a demand to repeat six paragraphs in every skill. The project formats own the fields; the shared contract owns the invariant; a skill owns the action that changes it.

## What Matt Pocock does better, and what to borrow

Read the [comparison and source inventory](2026-09-13-research-matt-pocock-comparison.md) for detailed evidence. The useful contrast is between mechanisms, not a claim that one collection is uniformly better.

| Mechanism in the inspected reference | Why it can improve Atlas | What to adopt | Cost or limit |
|---|---|---|---|
| Grilling and documentation-aware interviewing | Explicit closure criteria and context discipline help resist rushing through open questions | Ask concrete high-value questions; retain the settled result before handing off | Relentless questioning still needs a proportionate stopping rule |
| Shared domain and codebase-design references | Terms describe boundaries, responsibility, and invariants, beyond avoiding synonyms | Use domain modeling to test the meaning of parts and interfaces | Engineering detail belongs in relevant branches, not every brand task |
| Prototype branches for UI and logic | An experiment method can fit the uncertainty being tested | Distinguish visual preference tests from behavioral/state experiments | More references are useful only if the entry point reliably selects them |
| Diagnostic and TDD methods | Reproduction and falsifiable checks supply more evidence than "run existing checks" | Offer a diagnosis route for broken behavior and use a failing test where it demonstrates a real defect | Mandatory TDD for every task would harm non-code and low-impact work |
| Independent review axes | Different questions can expose different failures and reduce builder anchoring | Give reviewers a fixed change and enough project context; retain brief and conventions checks | A fresh agent has context and cost requirements; it is not GitHub approval |
| Scoped reference files and documentation | Conditional mechanics can be taught once and loaded when needed | Move tracker-specific procedures and format migrations behind strong pointers | A reader must be able to discover every hard dependency |

Atlas does better at a visible project-level map, a single local vocabulary, an explicit home for each knowledge type, a brief written at interview completion, and one coherent route across media. Those are worth preserving. Matt's tracker variants and engineering-specific methods offer useful detail, but wholesale copying would expand Atlas's configuration surface and weaken its cross-domain promise.

The comparison also finds incomplete paths in Matt's set, including implementation/review sequencing and tracker completion issues. Treat those as counterexamples to copying by reputation. Neither terse prose nor a larger skill library substitutes for behavioral evidence.

### Other influences to consider

These are design analogies and proposed evaluation criteria, rather than claims of adopting a particular external framework:

- **State machines:** define legal transitions and guards; distinguish a stored status from derived readiness. Apply this to handoff, retries, human waiting, cancellation, and stale review before adding status names.
- **Recoverable operations:** after a partial local/GitHub update, repeated execution should find the existing issue, branch, or delivery and continue safely. A database or event platform is unnecessary; a small durable receipt may suffice.
- **Information architecture:** each home answers a different question. Current truth and dated evidence need links in both directions when they matter, with a clear precedence rule.
- **Empirical evaluation:** compare old and revised skills on the same realistic task, including a failed check and an interruption. Measure correct next action and preserved work rather than exact generated wording.
- **Domain-specific craft:** software diagnosis, visual inspection, content editing, and data verification provide different evidence. Atlas should route to the right method while keeping its task interface small.

## Proposed transition model

This is a design candidate for the [first task](archive/2026-09-13-initial-review/plan/five-things/01-settle-workflow-contract.md), not a schema migration applied by this review. Prefer retaining `todo`, `doing`, and `done` if a small structured attempt record makes the distinctions below unambiguous. Evaluate an explicit `canceled` state because treating cancellation as success loses information. Avoid adding every transient condition as a top-level status.

| Situation | Required evidence | Action and owner | Result |
|---|---|---|---|
| Brief exists, tasks absent | Current brief and satisfied decision prerequisites | Plan creates accepted tasks | Planned work with stable ids |
| Task ready | Required blockers completed; task and brief current; workspace usable | Build claims and starts an attempt | Doing, with attempt identity |
| Attempt interrupted | Existing branch/artifact and last completed action | Build resumes the same attempt | Doing, with preserved prior work |
| Answer needed | Named question and the decision it blocks | Person answers, then build resumes | Waiting is resolved explicitly |
| Delivery ready | Artifact revision, checks and results, outstanding human checks | Review reads this delivery | One review target |
| Findings | Review tied to the delivery, with actionable findings | Build creates a revised delivery | Old review retained; new target awaits review |
| Clean, local work | Current clean review and completed required human checks | Review records completion | Done |
| Clean, PR workflow | Current clean review; required checks and policy satisfied | Authorized merge actor integrates | Done only after merge is verified |
| Brief or artifact changes | New revision and affected work identified | Interview/plan/build reopen relevant work | Earlier evidence remains historical |
| Work removed | Reason and incoming dependency assessment | Plan records cancellation and repairs scope | Removed work is distinguishable from delivery |
| All required tasks complete | Nonempty accepted scope and part outcome check | Review accepts the part | Part done at the accepted scope revision |

A review should identify what it examined, what it checked, what it could not check, and its disposition. A delivery should identify what changed, where it exists, and which checks actually ran. Those fields are more useful than adding universal paragraphs to every task. Keep existing documented formats authoritative during the transition: candidate field names belong in the contract task, and adopting them includes updating the templates and every reader that consumes them.

### Router precedence to test

1. Report invalid or inaccessible required state and its recovery action.
2. Surface an unresolved human action or failed operation relevant to current work.
3. Resume an explicit active task, or fix its current review findings.
4. Review a new valid delivery.
5. Build a ready task using one documented selection policy.
6. Plan a part with a current brief and no accepted task set.
7. Continue a relevant answered prototype or run the needed experiment.
8. Interview an eligible sketched or reopened part.
9. Report completed scope or a genuine dependency deadlock.

A handoff supplies context and a preferred target within this order. It does not supersede a completed task, a failed prerequisite, or a newer user direction. Exact scheduling remains a choice: the working plan mentions impact, while the builder uses map order then number. If impact is adopted, record the priority basis so two runs can explain their choices.

### Suggested command shape

Keep the eight public skill names during the first revision. Evaluate `/atlas` as inspection, `/atlas init` as adoption, `/atlas repair` as a visible repair operation, and `/atlas go` as a bounded supported mode only after invocation and progress checks pass. These are proposals, not currently supported command syntax.

A separate research skill, bug-diagnosis skill, or release skill is optional. First demonstrate that existing skills cannot reliably route to a relevant installed capability or write the appropriate evidence note. A retrospective should use observed failure patterns to simplify the framework, rather than create a ninth home for state.

### How much machinery is justified?

| Candidate | Benefit | Cost | Recommendation |
|---|---|---|---|
| Keep all behavior in prose and improve wording | Minimal installation and broad portability | Graph checks, state normalization, and retries are reimplemented by the model on every run | Keep prose for judgment and human interaction; use it alone only while scenarios remain simple and demonstrably reliable |
| Add small deterministic helpers for ids, graphs, views, and evidence checks | Repeated operations become inspectable and can reject invalid state consistently | A runtime, version policy, and compatibility tests become part of installation | Preferred next experiment for operations that already have a precise invariant; keep manual Markdown editing possible |
| Introduce a full workflow engine or service | Central locking, persistence, and scheduling can support large concurrent work | A sixth state store, deployment, and recovery burden threaten Atlas's purpose | Defer until concurrent real use demonstrates a need the file model cannot meet |

A helper should produce a proposed diff or a normalized read result that a person can inspect. It should earn its place by catching a real failure in the scenario suite. A parser that merely asserts heading spelling would add little confidence. A checker that prevents a canceled dependency from unlocking delivery, or rejects a stale review, protects a meaningful contract.

### Match the entry point to the uncertainty

For a small correction within an existing brief, create or select one task with a specific output and check, then build and review it. A new feature with unresolved scope needs the interview. A failing import needs diagnosis and a reproduced symptom before task acceptance is finalized. A visual preference needs contrasting artifacts and the person's judgment. A broad refactor may need compatible intermediate stages rather than artificial independent slices.

These routes should all return evidence to the same five homes. Atlas gains breadth by choosing the right work method, not by requiring the same depth of interview for each case. The [interview task](archive/2026-09-13-initial-review/plan/interview-skill/01-sharpen-interview-decisions.md) tests that lighter entry. The [reference comparison](2026-09-13-research-matt-pocock-comparison.md) explains the small-work and staged-migration mechanisms worth borrowing.

Before making these defaults, compare current and revised routes on the same bounded cases. Record time to useful output, avoidable user questions, state inconsistencies, lost or duplicated work, quality of the checks, and ability to resume from a fresh context. Record the model and harness because prose behavior can vary. A few runs expose obvious failures; they do not establish a universal success rate.

## Issue index

The linked task files are the actionable issue tracker for this review because this project uses `Tracker: files`. Each follows the existing task format, includes acceptance checks, and names real blockers. The briefs scope the review follow-up; they are planning drafts created by this audit, not evidence that new design choices were accepted in an interview. Task 01 under Five things is the decision gate for dependent changes.

| Urgency | Task | Findings or purpose |
|---|---|---|
| P1 | [five-things/01: settle the workflow contract](archive/2026-09-13-initial-review/plan/five-things/01-settle-workflow-contract.md) | F03-F04, F09, F14, F17, F21 |
| P1 | [atlas-skill/01: recover partial initialization](archive/2026-09-13-initial-review/plan/atlas-skill/01-recover-partial-initialization.md) | F06-F07 |
| P1 | [atlas-skill/02: route from current state](archive/2026-09-13-initial-review/plan/atlas-skill/02-route-from-current-state.md) | F01, F03, F05, F13 |
| P1 | [atlas-skill/03: align go with invocation](archive/2026-09-13-initial-review/plan/atlas-skill/03-align-go-with-invocation.md) | F12-F13 |
| P1 | [plan-skill/01: make planning repeatable](archive/2026-09-13-initial-review/plan/plan-skill/01-make-planning-repeatable.md) | F01, F15, F23 |
| P1 | [plan-skill/02: preserve replan history](archive/2026-09-13-initial-review/plan/plan-skill/02-preserve-replan-history.md) | F11, F20 |
| P1 | [build-skill/01: support resume and fixes](archive/2026-09-13-initial-review/plan/build-skill/01-support-resume-and-fixes.md) | F03-F04 |
| P1 | [build-skill/02: make GitHub start recoverable](archive/2026-09-13-initial-review/plan/build-skill/02-make-github-start-recoverable.md) | F02, F09, F23 |
| P1 | [build-skill/03: preserve owned changes](archive/2026-09-13-initial-review/plan/build-skill/03-preserve-owned-changes.md) | F08 |
| P1 | [review-skill/01: bind reviews to deliveries](archive/2026-09-13-initial-review/plan/review-skill/01-bind-reviews-to-deliveries.md) | F04, F22 |
| P1 | [review-skill/02: verify GitHub completion](archive/2026-09-13-initial-review/plan/review-skill/02-verify-github-completion.md) | F09-F10, F23 |
| P1 | [side-skills/02: make handoffs resumable](archive/2026-09-13-initial-review/plan/side-skills/02-make-handoffs-resumable.md) | F05, F08, F26 |
| P2 | [five-things/02: version and migrate formats](archive/2026-09-13-initial-review/plan/five-things/02-version-and-migrate-formats.md) | F18, F26 |
| P2 | [five-things/03: evaluate tracker and Git policy](archive/2026-09-13-initial-review/plan/five-things/03-evaluate-tracker-and-git-policy.md) | F24 |
| P2 | [interview-skill/01: sharpen interview decisions](archive/2026-09-13-initial-review/plan/interview-skill/01-sharpen-interview-decisions.md) | F17, F19-F20 |
| P2 | [interview-skill/02: preserve brief revisions](archive/2026-09-13-initial-review/plan/interview-skill/02-preserve-brief-revisions.md) | F20-F21 |
| P2 | [map-skill/01: validate graphs and views](archive/2026-09-13-initial-review/plan/map-skill/01-validate-graphs-and-views.md) | F15, F19 |
| P2 | [map-skill/02: preserve split part identity](archive/2026-09-13-initial-review/plan/map-skill/02-preserve-split-part-identity.md) | F16 |
| P2 | [review-skill/03: check part outcomes](archive/2026-09-13-initial-review/plan/review-skill/03-check-part-outcomes.md) | F21 |
| P2 | [side-skills/01: make prototypes conclusive](archive/2026-09-13-initial-review/plan/side-skills/01-make-prototypes-conclusive.md) | F25-F26 |
| P2 | [packaging/02: build realistic fixtures](archive/2026-09-13-initial-review/plan/packaging/02-build-realistic-fixtures.md) | F28 and behavioral evidence |
| P2 | [packaging/03: run release acceptance](archive/2026-09-13-initial-review/plan/packaging/03-run-release-acceptance.md) | Both trackers, advertised harnesses, real project |
| P3 | [packaging/01: align authoring and installation](archive/2026-09-13-initial-review/plan/packaging/01-align-authoring-and-installation.md) | F27-F28 |

### Adoption order and scope

First settle the contract and create realistic fixtures. Address initialization, ownership of changes, planning entry, build resumption, review identity, and router precedence as small complete repairs. Then test the GitHub start/review/merge sequence with partial failures. Enable automatic continuation only after those transitions work in a supported harness. Follow with split-map migration and more ambitious tracker/Git separation.

Each repair should update its authoritative rule, consuming skill, portable template when relevant, and one meaningful scenario. This avoids a single wholesale rewrite whose improvements cannot be attributed or rolled back. Existing accepted decisions remain accepted until a chosen revision explicitly supersedes them. In particular, the five root homes, one tracker, and current Git policy are not silently replaced by this document.

### Behavioral evaluation plan

| Scenario | Observable result that matters |
|---|---|
| Fresh non-Git folder | Homes created once; useful next action; a second invocation preserves content |
| Partially adopted project | Missing files recovered, existing material retained, instruction symlinks handled once |
| `CONTEXT.md` with terms and invariants | Each item retains a documented destination and inbound references remain usable |
| Brief but zero tasks | Router selects planning rather than treating the part as complete |
| Cycle and cross-part blockers | Exact invalid path reported; blocked work stays unselected |
| Task interrupted after one file | Same task/attempt resumes with that file preserved |
| Review finds a real defect | Builder fixes it, reviewer checks the new delivery, earlier evidence stays historical |
| Two deliveries on one day | Review target is unambiguous and stale approval is detected |
| Human-only acceptance | Wait is recorded; automatic continuation pauses once and resumes after the answer |
| Handoff followed by later work | Completed target is skipped and current state governs routing |
| Unrelated edits in a touched file | Only owned changes enter the skill's commit |
| GitHub creation fails after parent issue | Rerun reuses the parent and completes missing relationships |
| More than 30 GitHub tasks | Full state is visible; dependencies and parent completion remain correct |
| PR author equals reviewer account | Useful report succeeds without an impossible self-approval |
| Clean PR waiting for a human | Task stays incomplete; loop pauses; later merge is verified |
| Canceled task or manually closed issue | Completion and dependent readiness reflect the disposition accurately |
| Split building part with cross-links | Ids, task ownership, decision links, and incoming dependencies remain resolvable |
| Added work after part completion | Part is explicitly reopened at the revised scope |
| Prototype gives no clear answer | Inconclusive evidence is retained and a next experiment is proposed |
| Brand and software projects | Checks match the medium; combined outcome is verified |

Keep structural checks small: required format fields, stable ids, resolvable references, graph integrity, template version handling, and valid plugin metadata. Use behavioral runs to evaluate interviewing, useful task sizing, review quality, and recovery. Exact wording tests would mostly measure conformance to prose, not whether Atlas helps finish work.

### Validation performed for this review

Both `claude plugin validate .` (marketplace) and `claude plugin validate .claude-plugin/plugin.json` passed locally. `bash -n scripts/link-skills.sh` passed. Read-only file checks confirmed the missing brand outputs and the root map orientation discrepancy. The added task graph, Markdown file links, required brief/task fields, and preservation of the four pre-existing edits were checked before delivery; results are summarized in the final task response.

Those checks establish document and package consistency at the inspected level. They do not establish installed skill discovery, successful GitHub writes, good interviews, or a completed end-to-end workflow. The release acceptance task explicitly retains that work.

## Copied into

[README.md](../README.md) explains current operation and limitations. [MAP.md](../MAP.md) links the review follow-up and records its open questions. The nine part folders under [plan/](../plan/) hold scoped briefs and 23 tasks with acceptance checks. The existing skills, templates, and accepted decisions retain their current behavior pending that work.

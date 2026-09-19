---
date: 2026-09-19
kind: research
part: project
---

# Atlas and Matt Pocock: a segmented comparison framework

## Summary

Atlas has the stronger design for keeping a project's work understandable across sessions and media; Matt's collection has the more explicit engineering techniques and a clearer short route for small work. Atlas should retain its shared work record, complete the already adopted method separation, and borrow specific techniques where they improve an observable outcome. These are source-based design judgments, qualified by the limited Atlas run evidence, rather than a measured ranking of the two systems.

## Detail

### Scope and how to read the comparison

This answers the request to compare both systems at high and low levels, judge their decisions, and identify what Atlas should do about each. It is a research deliverable supporting the existing work packages, especially [work-skills/02](../plan/work-skills/02-build-and-review.md), rather than an implementation of that task or a new release plan.

Atlas baseline: `3f6aa5b3b7c1af38ac8393058273d826af7c6fce`, incorporating the planning update that arrived during this comparison. The executable operation files are unchanged from the initially inspected `472ca9508bdf896dbe000c0f66d81157a4d10afc`. There are **nine executable operations**, including `setup-atlas`, in draft 0.2. Some older package descriptions still count eight. Keep three evidence levels separate:

- **Executable draft:** what the files under `skills/` currently instruct.
- **Implemented method source:** diagnosis, verification, and prototype guidance under `methods/`; consumer wiring and generated installation bundles are pending.
- **Accepted direction:** the decisions and task contracts in the active plan. Acceptance of a design does not establish successful operation.

Matt baseline: [`c55ee46073ed923f86ce59a5eb3b6d895095d1b7`](https://github.com/mattpocock/skills/commit/c55ee46073ed923f86ce59a5eb3b6d895095d1b7), returned as upstream main by GitHub on September 19, with commit date September 18. All thirteen cited Matt skill files were read from the ignored local reference, and their Git blob hashes were compared with the complete upstream tree at that revision: **all thirteen matched**. Public citations below therefore identify the inspected source without requiring the ignored directory. This establishes those files' identity, not identity of the entire local reference or a tested installation. Git commands inside that reference resolve to Atlas's enclosing repository and must not be used as Matt provenance.

The [first Atlas scratch run](2026-09-18-review-first-agent-run-of-0-2.md) exercised an earlier revision, `62b0ff6`, through fresh agents reading skills by path. It found defects that were patched, including recovery and checksum problems. It did not test actual installed invocation, used an agent to answer for the human, and was not repeated end to end after the fixes. There is no equivalent controlled Matt run in this comparison. Earlier notes dated [September 13](2026-09-13-research-matt-pocock-comparison.md) and [September 15](2026-09-15-research-matt-boundaries-efficiency.md) are historical inputs; the distinctions above update their account without rewriting them. The contemporaneous [simplicity assessment](2026-09-19-research-matt-simplicity.md) and accepted [0025](../decisions/0025-finish-simple-skills-before-the-human-run.md) establish the current order: refine simple skills first, then perform Vitali's human acceptance run on the prepared candidate.

Judge each decision by five questions: does it help produce the right outcome, preserve enough information to resume, use the person's attention well, fit the supported project and medium, and earn its maintenance cost? A mechanism can win for a large project and lose for a small correction. “Keep” below supports an existing choice; “finish” identifies accepted but incomplete work; “test” identifies a candidate for the owning task, not an adopted new rule.

### 1. Product architecture: what the system is responsible for

Atlas is an integrated project method. Its operations share a glossary, map, plan, decisions, and dated notes. Matt's collection combines a recommended workflow with independently useful techniques, shared domain records, and configurable tracking. Matt also retains state; the difference is the breadth and uniformity of the shared contract.

| Decision | Atlas | Matt | Which is better, why, and what to do |
|---|---|---|---|
| Product integration | Common homes, task states, and next-operation rules. | Composable methods connected by a router and recommendations. | **Atlas for continuity; Matt for selective use.** Keep Atlas as one method with modular internals, as decision 0018 already says. Make each operation useful without requiring every preceding operation on every run. |
| Durable work record | Local briefs and tasks with stable ids, blockers, deliveries, and review history. | Local or hosted issues, specs, domain terms, decisions, and portable handoffs. | **Atlas for a uniform lifecycle; Matt for fitting an established team tracker.** Keep one local canonical plan for this release. Finish that contract before adding hosted adapters; do not create a second editable copy of task state. |
| Domain and medium | The same task structure can deliver code, a document, a design, or a process. | Core implementation guidance is strongly oriented toward software, although interviewing, research, and wayfinding are broader. | **Atlas for mixed work; Matt for engineering depth.** Keep general outcome and acceptance concepts, then select concrete verification by medium. A universal “run checks” instruction is too weak by itself. |
| Responsibility for delivery | Operations defer saving and integration to project instructions. | Some operations specify actions directly, such as committing on the current branch or retaining a prototype on a separate branch. | **Atlas's separation is better for reuse.** Finish decision 0012, with exact pending actions when project delivery fails. Review acceptance and successful merge remain distinct facts. |

Sources: Atlas [skill architecture](../skills/README.md), [local work](../decisions/0013-local-tasks-first.md), [product boundary](../decisions/0018-one-method-modular-skills.md), [delivery boundary](../decisions/0012-atlas-owns-work-projects-own-delivery.md); Matt [routing][m-route], [setup][m-setup], [implementation][m-implement], [prototype][m-prototype].

### 2. Thinking and decisions: how uncertainty becomes usable scope

Both systems use successive question rounds, shared vocabulary, concrete scenarios, and recorded decisions. The important differences are when to stop, what to ask, and who maintains the result.

| Decision | Atlas | Matt | Which is better, why, and what to do |
|---|---|---|---|
| Interview mechanics | Up to five questions whose prerequisites are settled; answers are written into homes during the interview. | A shared grilling method recomputes the available questions after every round, with fact gathering delegated separately. | **Combine them.** Matt's single reusable method is easier to keep consistent; Atlas's incremental persistence protects interrupted sessions. Finish the shared interview source and let operations own its writes. |
| Stopping rule | Accepted direction stops at the material choices needed for the selected outcome; later questions get an explicit place. | Grilling asks for every decision branch to be visited and confirmation of shared understanding. | **Atlas's scoped stopping rule is better for delivery.** Complete decision 0020 in all consumers. Exhaustive questioning is useful only when the person actually requests exhaustive exploration. |
| Defaults and permission | The draft treats skipped ordinary options as recommended defaults, with `(your call)` exceptions. | Grilling puts decisions to the person and waits. | **Matt is clearer about unanswered decisions; Atlas tries to reduce routine effort.** Classify an accessible fact, a delegated reversible choice, and a consequential human decision separately. Reuse existing authorization. Test skipped answers and “for now”; the scratch run already found ambiguity here. |
| Vocabulary | Five-home glossary discipline, including strong wording checks in the draft. | An active domain-modeling method challenges overloaded terms and checks descriptions against code. | **Matt more clearly separates active modeling from ordinary vocabulary reads; both have a canonical glossary.** Use real counterexamples when two meanings change behavior. Apply Atlas's current glossary rule that a distinction must change a decision or behavior; ordinary words should not require entries. |
| Recording decisions | Short decisions with adoption status; small settled choices live in the brief. | Deliberately sparse ADR creation with hard-to-reverse, surprising, and real-tradeoff tests. | **Keep the shared restraint.** Record enough rationale to explain a consequential choice, and preserve its actual status. Do not force every interview answer into a separate file. |

Sources: Atlas [interview operation](../skills/interview-me/SKILL.md), [bounded scope](../decisions/0020-decide-only-the-selected-scope.md), [glossary entry rules](../glossary/homes.md), [decision format](../decisions/README.md); Matt [grilling][m-grill], [domain modeling][m-domain]. Owner: [shared-methods/01](../plan/shared-methods/01-interview-and-model.md) and [work-skills/01](../plan/work-skills/01-interview-and-plan.md).

### 3. Planning and context: how work becomes manageable

Atlas's map describes project responsibilities and progress. Matt's wayfinding map describes an effort's unresolved decisions and the order in which they become answerable. Those views serve different purposes, so replacing one with the other would discard information.

| Decision | Atlas | Matt | Which is better, why, and what to do |
|---|---|---|---|
| Project shape and unresolved questions | Stable parts, decision prerequisites, task blockers, and open questions. | A destination, precise decision questions, unresolved areas that cannot yet be phrased precisely, and explicit exclusions. | **Use Atlas's shape with Matt's treatment of uncertainty.** Do not invent precise tasks for questions that cannot yet be stated. Keep exclusions separate from unresolved in-scope work, using the existing map and brief rather than adding another authoritative map. |
| Small work | One task can be added under an existing brief, but the draft still has a confirmation step; building and review are separate invocations. | After its interview, the router sends work that fits one session to implementation without a separate spec and decomposition; implementation is also directly invocable. | **Matt's route is simpler.** Finish Atlas's accepted direct route: settled brief, one task, necessary work and checks. The benefit of an extra interview or planning round must be a remaining decision. |
| Decomposition | Independently checkable outputs, stable task numbers, explicit blockers, and a first slice through the layers. | Complete vertical slices, plus explicit expand-and-contract guidance for wide mechanical refactors. | **Atlas has better identity rules; Matt has better refactor guidance.** Retain stable ids and cancellation records. Test Matt's wide-refactor exception in planning: add a compatible form, migrate callers in verifiable batches, then remove the old form. |
| Changed scope | The interview names affected tasks, but draft planning leaves review and done tasks untouched. | Specs and issues provide requirements, but the inspected composition does not establish Atlas's uniform revision-aware acceptance contract. | **Atlas's accepted direction is better than either incomplete implementation.** Finish impact assessment when a brief changes, including previously accepted work and canceled dependencies. Do not reset everything or assume all old acceptance survives. |
| Reading scope | The repository has INDEX.md and scoped reads; the installed template still asks for the glossary and map before working. | Task and phase routes, small references, and instructions to retrieve linked detail when needed. | **Matt often has the more economical entry point; Atlas has explicit ownership.** Finish conditional reads with expansion triggers. Measure cold-start and resumption cost, including missed context and unnecessary questions. Shorter instructions alone do not prove lower total cost. |

Sources: Atlas [plan operation](../skills/plan-it/SKILL.md), [template instructions](../skills/setup-atlas/templates/CLAUDE-block.md), [context direction](../decisions/0016-pointers-before-label-taxonomy.md), [acceptance direction](../decisions/0019-acceptance-follows-output-and-scope.md); Matt [wayfinding][m-wayfinder], [routing][m-route], [specification][m-spec], [task slicing][m-tickets]. Owners: [work-skills/01](../plan/work-skills/01-interview-and-plan.md), [work-skills/03](../plan/work-skills/03-map-and-identity.md), [core-model/02](../plan/core-model/02-define-task-evidence.md), and [context routing](../plan/context-routing/brief.md).

### 4. Execution and acceptance: how the result earns trust

This is the most consequential layer. Strong planning cannot compensate for weak feedback during implementation, and a recorded review cannot compensate for examining the wrong result.

| Decision | Atlas | Matt | Which is better, why, and what to do |
|---|---|---|---|
| Code feedback loop | Draft build runs project checks and the task's Check by. General verification guidance exists as an unwired method source. | Explicit TDD, tests through public interfaces, independent expected values, and one behavior slice at a time. | **Matt is stronger in the executable instruction.** Keep or invoke this discipline for code that benefits from tests, while respecting established project test conventions. Finish wiring Atlas's verification source so unsupported non-code claims also receive meaningful checks. |
| Test design choices | Project conventions and outcome criteria determine checks. | Local TDD requires confirmed test seams and places refactoring in review rather than the implementation loop. | **Keep Matt's observable-behavior focus, but evaluate its ceremony separately.** Existing accepted interfaces should settle routine test placement. Test whether postponing all refactoring causes avoidable duplication; small behavior-preserving improvements under passing tests and broader redesign have different costs. |
| Diagnosis | A source method distinguishes observations, competing hypotheses, bounded probes, and inconclusive results across media. | Detailed software reproduction and falsifiable debugging discipline. | **Matt supplies a strong software technique; Atlas's source provides a broader reusable contract.** Finish conditional loading when a failure needs explanation. Preserve the original failing signal and rerun it after a correction. Do not force an elaborate investigation when the evidence already establishes a narrow fix. |
| Review dimensions | Brief and conventions, preferably in a fresh context, with findings written back to the task. | Standards and specification reviewed separately, with distinct agent contexts and explicit missing-spec reporting. | **Combine them.** Retain both independent questions and a clear correction route. Use additional reviewers when their independence earns its cost; separate headings alone do not establish independent review. |
| Review target | Files plus checksum are compared before review. | Code review specifies a comparison ending at committed HEAD, while implementation calls review before committing. | **Atlas's explicit candidate identity is better.** In Matt's inspected composition, uncommitted implementation changes can fall outside the requested diff. Fix candidate selection before borrowing the workflow: baseline, actual candidate including working changes, and applicable criteria must be unambiguous. This is a static contract gap, not an observed failed Matt run. |
| Evidence weight | A short version line helps detect changed files; full output-and-scope identity is an accepted but unfinished contract. | Much less uniform delivery and review bookkeeping across operations. | **A compact Atlas record is the better middle ground.** A checksum detects change; it does not preserve an earlier file, identify an omitted file, or bind changing requirements. Resolve decisions 0019 and 0022 explicitly in core-model/02 before promising full retrievability. Keep evidence the next step actually uses. |
| What “done” means | Task done follows review; draft part completion is derived from task states. | Completion rules vary between the implementation, review, and tracking flows. | **Atlas has the stronger intended semantics.** Test a part whose tasks are all accepted but whose overall Outcome is unmet. Also test a done blocker whose output is absent in the current workspace. State alone must not stand in for the required result. |

Sources: Atlas [build](../skills/build-it/SKILL.md), [review](../skills/review-it/SKILL.md), [task template](../skills/setup-atlas/templates/plan/README.md), [diagnosis source](../methods/diagnosis.md), [verification source](../methods/verification.md), [0019](../decisions/0019-acceptance-follows-output-and-scope.md), [0022](../decisions/0022-one-version-line-per-delivery.md); Matt [TDD][m-tdd], [diagnosis][m-diagnosis], [implementation][m-implement], [review][m-review]. Owners: [core-model/02](../plan/core-model/02-define-task-evidence.md), [work-skills/02](../plan/work-skills/02-build-and-review.md), [shared-methods/05](../plan/shared-methods/05-bundle-method-references.md).

### 5. Learning and continuity: how experiments and interrupted work remain useful

| Decision | Atlas | Matt | Which is better, why, and what to do |
|---|---|---|---|
| Prototype construction | Draft supports different media and records a verdict. Source method adds measurable observations, preference, and inconclusive results. | Detailed logic and UI routes, visible state, contrasting alternatives, and a simple launch path. | **Matt is more operationally specific; Atlas's source is more general.** Finish the existing adaptation. Frame the deciding observation first, then build only what can expose it. An experiment that cannot reach its deciding evidence should return an explicit next experiment. |
| Prototype retention | Dedicated prototype folder, dated evidence, and a return to the part's open question; draft prohibits task links to the prototype. | Retains prototype source on a separate branch with an issue pointer. | **Matt is stronger on traceable source; Atlas is better at avoiding a universal Git policy.** Distinguish a reference to experimental evidence from a production dependency on the prototype. Let the project choose storage, and reverify anything promoted into actual work. |
| Ordinary resumption | A dated in-project handoff points to a task or part and carries only missing session context. | A temporary portable handoff references existing artifacts and suggests skills for the next session. | **Atlas for continuity in one project; Matt for a move between people, directories, or tools.** Keep Atlas's durable task as the primary resumption record. Treat a portable handoff as an export with resolvable pointers. |
| Handoff freshness | Draft checks the newest handoff and whether target status still matches. | The handoff source does not define a common freshness guard. | **Atlas has a guard, but it is too weak for its intended contract.** A task can remain doing while its output changes, or return to doing after review. Test these cases and search by relevant target, rather than letting a newer unrelated note hide the needed handoff. |

Sources: Atlas [prototype operation](../skills/prototype-it/SKILL.md), [prototype method](../methods/prototype.md), [park operation](../skills/park-it/SKILL.md), [handoff template](../skills/setup-atlas/templates/notes/README.md); Matt [prototype][m-prototype], [handoff][m-handoff]. Owner: [work-skills/04](../plan/work-skills/04-prototype-and-handoff.md), with the task identity contract in core-model/02.

### 6. Adoption and maintenance: what makes the design supportable

| Decision | Atlas | Matt | Which is better, why, and what to do |
|---|---|---|---|
| Setup and inspection | Setup is separate; the router reads and recommends without changing files. | Separate setup discovers tracking and domain-document conventions. | **Both make the useful separation.** Atlas should keep it and finish adoption tests for pre-existing homes, conflicting content, interrupted setup, custom instruction blocks, and repeated runs. Creating missing files is easier than safely adopting an existing project. |
| Shared-method distribution | Accepted design authors once and generates references beside each consumer; not yet implemented. | Several workflows invoke other named skills and depend on project configuration. | **Matt is simple in a complete installation; Atlas's design addresses selective installation explicitly.** Complete consumer mappings and deterministic bundles, then test them. Do not advertise dependency independence merely because folders can be copied separately. |
| Invocation and autonomy | Public state-changing operations require explicit invocation; automatic continuation is deferred. | Mixes directly invoked flows with reusable methods, and implementation calls review internally. | **Matt reduces command handoffs; Atlas makes the current control boundary clearer.** Preserve Atlas's supported explicit flow for release. Treat an optional automatic build-review cycle as the existing unresolved design question, requiring termination and authorization tests rather than an incidental change to the router. |
| Documentation and extension | Small consistent operation set and an explicit unfinished-release plan; some count and run descriptions lag the patch. | More user-facing entry points and specialist capabilities such as triage, architecture exploration, research, and human questionnaires. | **Matt offers broader discovery; Atlas offers a smaller product to learn.** Link compatible specialist techniques instead of cloning the catalogue. Describe observed run evidence precisely and keep current docs aligned with nine operations. |
| Validation | Structural checks exist; scratch run evidence is limited; installation and cold acceptance remain release work. | Source inspection establishes mechanisms, not comparative success rates or installation reliability. | **No empirical winner is established.** Keep Atlas's evidence-before-release gate and run a fair comparison. A collection's popularity, prompt length, or release label cannot answer which method completes equivalent tasks more reliably. |

Sources: Atlas [setup](../skills/setup-atlas/SKILL.md), [router](../skills/atlas/SKILL.md), [authoring and distribution](../skills/README.md), [release gate](../decisions/0017-evidence-before-release.md); Matt [setup][m-setup], [routing][m-route], [implementation][m-implement]. Owners: [project setup](../plan/project-setup/brief.md), [shared-methods/05](../plan/shared-methods/05-bundle-method-references.md), [work-skills/05](../plan/work-skills/05-cut-over-router-and-contracts.md), [public release](../plan/public-release/brief.md).

### Operation-by-operation application

| Atlas operation | Closest Matt counterpart | What Atlas should retain | What to improve or finish |
|---|---|---|---|
| `setup-atlas` | `setup-matt-pocock-skills` | Separate, repeatable adoption and project policy. | Preserve existing conventions and prove recovery from partial setup. |
| `atlas` | `ask-matt` | Reconstruct current state and recommend the next actual operation. | Combine state with the user's selected target; narrow reads and avoid stale handoffs. |
| `interview-me` | `grilling`, `grill-with-docs`, `domain-modeling` | Incremental writes and one interview at project or part scope. | One shared method, material-choice stopping, concrete examples, and clear unanswered decisions. |
| `map-it` | `wayfinder`, domain modeling | Stable project responsibilities and diagrams derived from text. | Keep decision uncertainty distinct from structure, preserve identity during splits, and justify completion from outcomes. |
| `plan-it` | `to-spec`, `to-tickets` | A brief plus durable tasks and explicit dependency checks. | A short route for settled work, wide-refactor guidance, and impact assessment for old acceptance. |
| `build-it` | `implement`, `tdd`, `diagnosing-bugs` | One resumable task, project-owned saving, observed verification. | Wire concrete methods and check access to accepted blocker outputs. |
| `review-it` | `code-review` | Task-bound acceptance and a runnable findings loop. | Correct candidate and scope identity, proportionate independent review, and concise evidence. |
| `prototype-it` | `prototype` and its logic/UI references | One bounded question and evidence returned to the project. | Detailed experiments, accessible source evidence, and precise inconclusive outcomes. |
| `park-it` | `handoff` | Durable in-project context with references instead of duplication. | Target-aware freshness and portable export when moving to another workspace or person. |

### Advice for each system

For **Atlas**, preserve the shared lifecycle while making its normal path easier to enter and its engineering methods concrete. Its main risk is a gap between thoughtful contracts and what the installed operations actually do, compounded by record keeping or questions that do not improve the result. The next useful work is integration, simplification, and observed validation.

For **Matt's collection**, preserve independent methods and the light small-work route. Strengthen the joins with a few explicit facts: what candidate review examines, which requirements it answers to, what remains after a failed attempt, and which required skills are available. Put environment-specific delivery rules in project configuration. That would address the most important continuity gaps without requiring every adopter to install Atlas's five-home structure.

### What to do first

This is a priority lens over the existing plan, not permission to skip its blockers or a replacement execution order.

1. **Refine the candidate before the human run.** Follow [0025](../decisions/0025-finish-simple-skills-before-the-human-run.md): complete the remaining scope, credit work already demonstrated by the patch, and simplify instructions that do not change behavior. Use focused scratch checks during refinement; the outstanding human check in [work-skills/06](../plan/work-skills/06-patch-the-draft.md) remains release evidence, not a prerequisite for starting refinement.
2. **Settle evidence and resumption once.** In [core-model/02](../plan/core-model/02-define-task-evidence.md), reconcile 0019 with 0022, changed scope, accessible blockers, human judgments, and multiple attempts. Subsequent operations should consume the same answer.
3. **Connect the good methods already written.** Complete the interview source and [method bundles](../plan/shared-methods/05-bundle-method-references.md), then the eligible work-skill tasks. More method prose has little benefit while operations do not load it.
4. **Remove unnecessary interaction and reads.** Exercise a one-task correction, an already settled test interface, and a previously answered question. Use [context-cost measurement](../plan/context-routing/02-measure-context-cost.md) to count the complete run, including questions and recovery.
5. **Prove adoption and installation.** Finish project-setup recovery and the [clean-profile matrix](../plan/public-release/02-verify-installation-matrix.md). Full-package success does not prove single-skill success.
6. **Run acceptance on the prepared candidate and publish demonstrated claims.** Complete the independent runs and Vitali's deferred human check in [cold-context acceptance](../plan/validation/03-run-cold-context-acceptance.md), align user documentation, and only then assess a tagged release. Additional commands and automatic orchestration can wait for an observed need.

### A fair comparison to run

Use the same model, harness, starting files, user answers, project permissions, and independently specified acceptance criteria. Pin both skill revisions. Test the executable releases separately from experimental adaptations. Repeat runs when resources permit, keeping failures and variation visible.

| Case | What would distinguish the designs |
|---|---|
| A clear one-session bug fix | Correct fix and meaningful regression check, with few unnecessary questions or planning artifacts. |
| A feature spanning sessions | A fresh agent finds the right task, consumes the right blocker output, and completes the requested behavior. |
| A wide refactor | Intermediate states remain valid where promised, dependencies are accurate, and the final transition has actual verification. |
| Review before commit | Review examines the modified candidate rather than only committed HEAD. |
| Changed artifact or changed brief | Earlier acceptance is retained as history and affected checks or judgments are renewed. |
| Crash and later resumption | Existing work is preserved, unanswered choices remain pending, and unrelated newer handoffs do not hide the target. |
| A non-Git document or visual deliverable | Content and visual claims receive the appropriate checks; the reviewed version and human judgments are identifiable. |
| An inconclusive prototype | The method records what the experiment established, what it did not, and the next useful observation. |
| Partial setup and selective installation | Existing project content survives; the selected operation can find all required resources. |

Record acceptance success, unsupported completion claims, missed changes, lost work, questions needing human decisions, total context read, tool calls, elapsed time, and recovery effort. Treat correctness and required human judgment as constraints; optimize attention and cost among runs that satisfy them. This report establishes no numerical speed, cost, or reliability advantage.

### Verification of this report

Source inspection covered all nine Atlas operations, their relevant project formats, the implemented method sources, linked accepted decisions, and the existing run evidence. All thirteen cited Matt skill files matched the pinned upstream tree by Git blob hash. The project structural check passed with no errors; this checks local document links, planning structure, and metadata, not remote service behavior or comparative agent performance. No skills were executed as part of this analysis.

## Copied into

Nothing durable. This dated comparison evaluates existing decisions and supplies candidates to the linked task owners. It adopts no new decision, changes no task acceptance, and implements no skill behavior.

[m-route]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/ask-matt/SKILL.md
[m-setup]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/setup-matt-pocock-skills/SKILL.md
[m-implement]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/implement/SKILL.md
[m-prototype]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/SKILL.md
[m-grill]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling/SKILL.md
[m-domain]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/SKILL.md
[m-wayfinder]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/wayfinder/SKILL.md
[m-spec]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-spec/SKILL.md
[m-tickets]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-tickets/SKILL.md
[m-tdd]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/SKILL.md
[m-diagnosis]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/diagnosing-bugs/SKILL.md
[m-review]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/code-review/SKILL.md
[m-handoff]: https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/handoff/SKILL.md

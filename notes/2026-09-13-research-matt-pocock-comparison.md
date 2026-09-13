---
date: 2026-09-13
kind: research
part: project
---

# Atlas and Matt Pocock's skills: what to borrow, adapt, and test

## Summary

Atlas has a stronger shared record and a more explicit delivery lifecycle; the Matt Pocock reference has stronger reusable engineering disciplines, clearer entry points, more candid user documentation, and better handling of work that does not fit the main flow. The useful influence is its separation of routing, reusable methods, and human documentation, with concrete feedback loops and examples behind each method. Keep the five things, repair Atlas's lifecycle and platform contracts, then add selective capabilities rather than copying the reference's whole catalogue.

## Detail

### Scope, provenance, and confidence

This is a static comparison of all eight Atlas skills and relevant material under `reference/mattpocock-skills/`, with selected first-party web verification on 2026-09-13. Atlas's terms and current structure come from [GLOSSARY.md](../GLOSSARY.md) and [MAP.md](../MAP.md). This note compares mechanisms and likely failure modes; it does not claim benchmark results or successful end-to-end execution of either framework.

The local reference is an untracked reference copy, not a separately identifiable checkout. Running `git -C reference/mattpocock-skills rev-parse --show-toplevel HEAD` resolves to the Atlas repository and its commit. That commit is not provenance for the Matt Pocock copy. The local [package.json](../reference/mattpocock-skills/package.json), [plugin manifest](../reference/mattpocock-skills/.claude-plugin/plugin.json), and [changelog](../reference/mattpocock-skills/CHANGELOG.md) identify version 1.2.3. The [upstream package.json](https://raw.githubusercontent.com/mattpocock/skills/main/package.json) also reported 1.2.3 when checked. Matching versions establish agreement on a version label, not byte identity, acquisition date, or a pinned upstream commit.

The [upstream README](https://github.com/mattpocock/skills) independently confirms the broad approach: small composable skills, a router, a main interview-to-implementation flow, separate reusable methods, and distinct user-invoked and model-invoked skills. Detailed comparisons below cite the local files actually read. Those links require the gitignored local reference copy and will not resolve in a clean public checkout. The [upstream source tree](https://github.com/mattpocock/skills/tree/main) is a public discovery path, but its current files may differ; a future reproducible comparison should pin the upstream revision or retain permitted source excerpts with hashes. Claims reported by local human documentation are distinguished from behavior established by the skill text. The reference's usage anecdotes and token estimates are not independently reproduced here.

Confidence labels mean:

- **High:** the instruction or omission is directly visible, or the platform behavior is stated in current official documentation.
- **Medium:** the design implication is reasoned from those instructions and needs a scenario test.
- **Exploratory:** the change may help, but its value depends on user behavior and measured outcomes.

### The architectural difference

Atlas asks each skill to participate in one shared method. The five things answer where current terms, shape, work, choices, and dated observations live. The eight skills move a project through that shared record, and `/atlas` attempts to derive the next action from it. This gives a fresh session an explicit place to orient and gives completion a home. The cost is stronger coupling: every skill depends on the consistency of shared formats, task transitions, part transitions, and tracker behavior. Sources: [Atlas skill](../skills/atlas/SKILL.md), [build](../skills/build-it/SKILL.md), [review](../skills/review-it/SKILL.md).

The reference is closer to a collection of methods joined by recommendations. [ask-matt](../reference/mattpocock-skills/skills/engineering/ask-matt/SKILL.md) explains routes; [grilling](../reference/mattpocock-skills/skills/productivity/grilling/SKILL.md), [domain-modeling](../reference/mattpocock-skills/skills/engineering/domain-modeling/SKILL.md), [tdd](../reference/mattpocock-skills/skills/engineering/tdd/SKILL.md), and [code-review](../reference/mattpocock-skills/skills/engineering/code-review/SKILL.md) supply reusable disciplines. Its small-build route skips a spec and ticket breakdown. Its large-effort route uses [wayfinder](../reference/mattpocock-skills/skills/engineering/wayfinder/SKILL.md), which produces decisions before implementation work is planned. The cost is that the joins can remain manual or incomplete.

**Recommendation, high confidence:** keep Atlas's canonical record and completion accounting, and borrow the reference's ability to enter at the right depth. A well-scoped correction should be able to become one task from an existing brief; a new product deserves an interview; a hard unknown deserves research or a prototype. Treat the route as a consequence of the uncertainty and scope, with recorded preconditions, rather than requiring the same conversation for every change.

### Skill-by-skill comparison

| Atlas skill | Reference counterpart | What the reference adds | What Atlas should retain or improve |
| --- | --- | --- | --- |
| [`atlas`](../skills/atlas/SKILL.md) | [`ask-matt`](../reference/mattpocock-skills/skills/engineering/ask-matt/SKILL.md), [`setup-matt-pocock-skills`](../reference/mattpocock-skills/skills/engineering/setup-matt-pocock-skills/SKILL.md) | A route chosen by situation, distinct setup, explicit context-boundary guidance, and configuration adapted to existing repositories. | Keep state-derived orientation. Separate observation, repair, and execution; give setup a migration path. Make orchestration compatible with invocation restrictions. |
| [`interview-me`](../skills/interview-me/SKILL.md) | [`grilling`](../reference/mattpocock-skills/skills/productivity/grilling/SKILL.md), [`grill-with-docs`](../reference/mattpocock-skills/skills/engineering/grill-with-docs/SKILL.md), [`domain-modeling`](../reference/mattpocock-skills/skills/engineering/domain-modeling/SKILL.md), [`wayfinder`](../reference/mattpocock-skills/skills/engineering/wayfinder/SKILL.md) | One reusable interview method; explicit fact gathering; checking user descriptions against existing code; room for uncertainty that is not yet precise enough to become a question. | Keep incremental writing and one interview at project and part scope. Separate unknown facts, user choices, and unresolved assumptions. A skipped answer needs an explicit default policy, especially for material decisions. |
| [`map-it`](../skills/map-it/SKILL.md) | [`wayfinder`](../reference/mattpocock-skills/skills/engineering/wayfinder/SKILL.md), [`domain-modeling`](../reference/mattpocock-skills/skills/engineering/domain-modeling/SKILL.md) | A low-resolution index with links to detailed decisions; named destinations; a distinction between unresolved scope and excluded scope. | Keep diagrams derived from sections. Treat splitting as a migration of identities, dependencies, briefs, and tasks. Keep project structure separate from an effort's decision order. |
| [`plan-it`](../skills/plan-it/SKILL.md) | [`to-spec`](../reference/mattpocock-skills/skills/engineering/to-spec/SKILL.md), [`to-tickets`](../reference/mattpocock-skills/skills/engineering/to-tickets/SKILL.md) | Test boundaries before build; complete vertical slices; explicit expand-and-contract handling for wide refactors; a small-work route that skips decomposition. | Keep Delivers, Check by, Done when, durable task IDs, and blockers. Add a falsifiable acceptance check and a change-impact pass when a brief changes. Give cancellation a meaning distinct from successful completion. |
| [`build-it`](../skills/build-it/SKILL.md) | [`implement`](../reference/mattpocock-skills/skills/engineering/implement/SKILL.md), [`tdd`](../reference/mattpocock-skills/skills/engineering/tdd/SKILL.md), [`diagnosing-bugs`](../reference/mattpocock-skills/skills/engineering/diagnosing-bugs/SKILL.md) | Behavioral tests through public interfaces, one failing case at a time, a diagnosis loop that reproduces a symptom before choosing a fix. | Keep delivery evidence, task ownership, and explicit state updates. Add optional methods by medium; code should have a verification discipline as concrete as the delivery record. Make interrupted work and findings runnable again. |
| [`review-it`](../skills/review-it/SKILL.md) | [`code-review`](../reference/mattpocock-skills/skills/engineering/code-review/SKILL.md) | A fixed comparison boundary, separate review contexts per axis, explicit missing-spec handling, and labeled heuristics beneath documented standards. | Keep acceptance checks and the feedback-to-build loop. Bind a review to an exact delivery revision and give reviewers enough surrounding context. Keep quality judgment separate from platform approval and merge. |
| [`prototype-it`](../skills/prototype-it/SKILL.md) | [`prototype`](../reference/mattpocock-skills/skills/engineering/prototype/SKILL.md), its [`LOGIC.md`](../reference/mattpocock-skills/skills/engineering/prototype/LOGIC.md) and [`UI.md`](../reference/mattpocock-skills/skills/engineering/prototype/UI.md) | Different artifacts for logic and appearance; an easy launch path; visible internal state; explicit handling when persistence is the thing being tested; retained primary-source material. | Keep broad media support, a question, a verdict, and the return to the interview. Permit source links for evidence while keeping production dependencies separate. Make empirical answers agent-verifiable when possible. |
| [`park-it`](../skills/park-it/SKILL.md) | [`handoff`](../reference/mattpocock-skills/skills/productivity/handoff/SKILL.md), [`ask-matt` phase boundaries](../reference/mattpocock-skills/skills/engineering/ask-matt/PHASE-BOUNDARIES.md) | A portable handoff outside the workspace, skill recommendations for the next session, and a clear distinction between continuing, clearing, compacting, delegating, and handing off. | Keep a dated project history. Record a resumable target and its revision, define when a handoff is consumed or stale, and make commit scope explicit. A project checkpoint and an export for another person are different uses. |

### What the reference does better, and why

#### 1. It reuses a discipline instead of retyping a style

The reference's interview wrappers reach the same [grilling primitive](../reference/mattpocock-skills/skills/productivity/grilling/SKILL.md). Domain work has its own active [method](../reference/mattpocock-skills/skills/engineering/domain-modeling/SKILL.md), while simple vocabulary consumption remains a file read. Its [invocation guidance](../reference/mattpocock-skills/.agents/invocation.md) distinguishes invoking a method from mentioning a command to a person.

Atlas repeats parts of the interview format in [interview](../skills/interview-me/SKILL.md), [planning](../skills/plan-it/SKILL.md), and [map splitting](../skills/map-it/SKILL.md). Those copies are shorter, but diverge and leave some consumers relying on a format that is not fully defined where they read it.

**Adopt first, high confidence:** give shared interview rules one reachable home. A plain reference file is sufficient if it needs no independent invocation. A new skill earns its existence only if it is useful independently or must be invoked as a method. Eight coherent commands are better than a large catalogue of wrappers.

#### 2. It identifies hard prerequisites separately from helpful context

The reference [setup decision](../reference/mattpocock-skills/.agents/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md) distinguishes skills that need a configured tracker to publish correctly from skills that merely benefit from a glossary. The [setup skill](../reference/mattpocock-skills/skills/engineering/setup-matt-pocock-skills/SKILL.md) inspects existing tracker and document arrangements before choosing defaults.

Atlas's fixed layout is easier to explain, but [initialization](../skills/atlas/SKILL.md) treats an absent map as a fresh project and moves `CONTEXT.md` entries into a glossary before deleting that file. In an established repository, absence of Atlas's map does not mean absence of useful project structure.

**Adapt, high confidence:** keep the default layout, add an import preview and resumable initialization, and require only the homes each operation actually needs. Preserve source material until the migration accounts for its contents and references.

#### 3. It gives uncertainty a place before it becomes a task

[Wayfinder](../reference/mattpocock-skills/skills/engineering/wayfinder/SKILL.md) distinguishes a precise unanswered question from an area that cannot yet be phrased precisely. It also separates both from work excluded by the destination. Its decision work can be research, a prototype, an interview, or a prerequisite action.

Atlas already distinguishes prototype questions and has a `research` note kind, but the [interview](../skills/interview-me/SKILL.md) principally advances by questions and answers. A research finding can therefore have a storage format without a defined path back into a decision or brief.

**Adapt, medium confidence:** add question type, resolution evidence, and a reopening rule within existing part sections before adding more top-level structures. A research method should return facts with sources and uncertainty, then link the result to the question it resolves. Test whether this can remain a reference branch of interviewing before adding `/research-it`.

#### 4. It plans for feedback, not only output

[To-spec](../reference/mattpocock-skills/skills/engineering/to-spec/SKILL.md) asks where behavior will be tested, [TDD](../reference/mattpocock-skills/skills/engineering/tdd/SKILL.md) explains public-interface tests, and [diagnosing-bugs](../reference/mattpocock-skills/skills/engineering/diagnosing-bugs/SKILL.md) requires an observed failing signal for the reported symptom. These are mechanisms for discovering that an implementation is wrong while it is still cheap to change.

Atlas's [Check by and Delivered](../skills/build-it/SKILL.md) make verification reportable across media. The missing layer is how a builder chooses a meaningful check when the project has weak existing practices.

**Adapt, high confidence:** keep universal delivery fields and add optional verification guides. Code needs public behavior, failure cases, and an appropriate test boundary. A document may need factual and visual review. A design may need contrasting examples and accessibility checks. Require evidence proportional to the risk and medium; importing mandatory TDD into every Atlas task would shrink Atlas's usefulness.

#### 5. It handles decomposition exceptions explicitly

[To-tickets](../reference/mattpocock-skills/skills/engineering/to-tickets/SKILL.md) describes expand, migrate, and contract for a broad mechanical change that cannot be delivered as an independent vertical slice. It also allows an integration branch when intermediate batches cannot be green. That is substantially more precise than telling an agent to split until tasks are small.

Atlas's [planning rule](../skills/plan-it/SKILL.md) has a good first thin slice, but its default to splitting can create work that is small on paper and unverifiable alone.

**Adopt, high confidence:** add a task-shape check and explicit migration handling. Each task should name the observation it changes and what would falsify success. Size tasks by independently verifiable progress, including evidence-only progress where appropriate, instead of an abstract session duration alone.

#### 6. It documents how a human can tell that a skill worked

The reference's [writing-docs guidance](../reference/mattpocock-skills/.agents/writing-docs.md) separates the human explanation from the agent recipe. Its pages describe when to reach for a skill, neighboring routes, prerequisites, common questions, and visible success signals. [Implement's page](../reference/mattpocock-skills/docs/engineering/implement.md) is unusually candid about lifecycle gaps. [To-tickets' page](../reference/mattpocock-skills/docs/engineering/to-tickets.md) explains over-decomposition and acceptance criteria that are true before work begins.

**Adopt now, high confidence:** Atlas's README should explain the whole method and routes, then describe each command's input, output, next action, and failure recovery. A reader should understand the system without reading eight instruction files. Keep factual behavior aligned with the skills, and label proposed behavior as proposed. Examples and observable success signals matter more than adding prose volume.

#### 7. It treats packaging and release records as part of the product

The reference carries an explicit [promoted-skill manifest](../reference/mattpocock-skills/.claude-plugin/plugin.json), [release history](../reference/mattpocock-skills/CHANGELOG.md), and a [version synchronization check](../reference/mattpocock-skills/scripts/sync-plugin-version.mjs). Its [repository instructions](../reference/mattpocock-skills/CLAUDE.md) require docs and router updates when a skill changes.

**Adapt, high confidence:** Atlas does not need the reference's buckets or release tooling to gain the benefit. It needs a tested install path, an explicit support matrix, a release checklist, template-version compatibility, and a discoverable changelog. Static validation and scenario tests should gate claims of readiness.

### What the reference does not solve better

1. **Implementation closure is weaker.** [Implement](../reference/mattpocock-skills/skills/engineering/implement/SKILL.md) runs review and commits, but does not define a response to findings, tick task criteria, or close work items. The [human documentation](../reference/mattpocock-skills/docs/engineering/implement.md) explicitly acknowledges these gaps. Atlas's [review lifecycle](../skills/review-it/SKILL.md) has the stronger intention: findings return to build and clean results advance the task. Repair that lifecycle rather than replacing it with the shorter reference recipe. **High confidence.**

2. **Its review boundary is good but its composition is broken.** [Code-review](../reference/mattpocock-skills/skills/engineering/code-review/SKILL.md) compares a fixed point with `HEAD`; [implement](../reference/mattpocock-skills/skills/engineering/implement/SKILL.md) invokes it before committing. Current uncommitted work can therefore be absent from the review. The docs acknowledge this exact issue. Atlas should adopt an explicit reviewed revision and baseline, including an explicit strategy for working-tree changes. **High confidence.**

3. **Some human checkpoints are broader than the job needs.** The reference's [TDD](../reference/mattpocock-skills/skills/engineering/tdd/SKILL.md) requires user agreement before any test seam; [grilling](../reference/mattpocock-skills/skills/productivity/grilling/SKILL.md) asks for exhaustive shared understanding. These constraints can help a difficult design and burden a routine fix. Existing agreement should count, and reversible implementation choices should be delegated where the user has authorized them. This is a design recommendation, not a demonstrated performance result. **Medium confidence.**

4. **The catalogue creates a navigation and maintenance bill.** A dedicated [router](../reference/mattpocock-skills/skills/engineering/ask-matt/SKILL.md) and mirrored [documentation tree](../reference/mattpocock-skills/.agents/writing-docs.md) help, but also require synchronized updates. Atlas's small vocabulary and eight commands are a real advantage if they cover the routes users need. Copy mechanisms before adding names. **Medium confidence.**

5. **Code-specific defaults narrow applicability.** [Prototype](../reference/mattpocock-skills/skills/engineering/prototype/SKILL.md) branches between logic HTML and UI variants, and [to-spec](../reference/mattpocock-skills/skills/engineering/to-spec/SKILL.md) calls for extensive user stories and testing decisions. Atlas can handle a brand, writing, research, or operations without treating everything as an application. Preserve that breadth with examples and medium-specific evidence. **High confidence about the textual difference; medium about product advantage.**

6. **Its portability prose still assumes capabilities.** The local [invocation guide](../reference/mattpocock-skills/.agents/invocation.md) names a Skill tool as the way to compose methods. Some hosts expose different tools or file-based loading. [Ask-matt](../reference/mattpocock-skills/skills/engineering/ask-matt/SKILL.md) also gives context-window estimates and harness commands that should be treated as host-specific advice. Atlas needs capability checks and fallback behavior, not a claim that one prose convention behaves identically everywhere. **Medium confidence.**

7. **Source-code observations are stronger evidence than popularity or anecdotes.** The reference's docs contain reports of expensive tickets, parallel-checkout accidents, and unreliable dependency wiring. Those reports are useful hypotheses for Atlas's test cases, but this review did not reproduce their frequencies. Treat them as prompts for evaluation, not measurements of Atlas or universal model behavior. Sources: [implement docs](../reference/mattpocock-skills/docs/engineering/implement.md), [planning docs](../reference/mattpocock-skills/docs/engineering/to-tickets.md). **High confidence about the provenance limit.**

### Platform facts that change the design

**Invocation is a real boundary.** Current Claude Code documentation states that `disable-model-invocation: true` makes a skill user-only, blocks model invocation, and instructs the model not to reproduce the steps through another route. All eight Atlas skills set it. Therefore `/atlas go` calling build and review as separate skills conflicts with Claude's documented behavior. A workable design can keep a user-invoked orchestrator and give it a deliberately callable implementation method, or keep routing manual. This needs an explicit design decision and host testing. Source: [Claude skill invocation](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill). The generic [Agent Skills specification](https://agentskills.io/specification) describes the portable file format; it does not establish identical host orchestration semantics.

**Atlas's flat plugin layout is valid.** Claude discovers `skills/<name>/SKILL.md` under the plugin root. The absence of a `skills` array in Atlas's manifest is not, by itself, a packaging defect. The reference needs explicit paths for its selected nested catalogue; Atlas's flat layout can use the default. Plugin commands are namespaced, which should be reflected in install examples. Source: [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference#skills).

**Adding a marketplace and installing a plugin are separate actions.** Documentation for a self-hosted catalogue should show the actual repository as the source of `/plugin marketplace add`, then the declared plugin and marketplace names in `/plugin install plugin-name@marketplace-name`. A placeholder or bare repository install line is not proof that installation works. Source: [Claude plugin installation](https://code.claude.com/docs/en/discover-plugins#install-plugins).

**An agent review is not automatically an eligible GitHub approval.** GitHub does not allow a pull request author to approve their own pull request. If build and review use the same authenticated identity, a fresh review context does not change that identity. Atlas can record its review as a comment and report which approval or merge requirements remain. Source: [GitHub pull request review rules](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request).

**Complete tracker reads require deliberate pagination and dependency reads.** `gh issue list` defaults to 30 results. REST dependency lists also paginate, with a default page size of 30 and maximum 100. Atlas's status query of issue number, state, and assignees cannot establish all blockers, delivery events, review events, or merge status by itself. The tracker implementation needs complete reads, native relation queries, and explicit mappings between external state and Atlas state. Sources: [GitHub CLI issue list](https://cli.github.com/manual/gh_issue_list), [GitHub issue dependency API](https://docs.github.com/en/rest/issues/issue-dependencies).

These are verified platform constraints, not evidence that the installed local harness or CLI was tested. Record supported versions and run installation, invocation, and GitHub lifecycle scenarios before claiming compatibility.

### Proposed adoption order

| Order | Proposed revision | Why this comes first | Confidence and proof |
| --- | --- | --- | --- |
| 1 | Define the task lifecycle, reviewed revision, blocking meaning, and resumable failure states. | Atlas's main advantage depends on completion accounting being correct. | High. Walk success, findings, interruption, cancellation, and human merge scenarios without chat history. |
| 2 | Make status read-only by default; define repair separately; settle how explicit invocation and automated execution coexist. | A router must recommend a possible action from trustworthy state. | High. Test each advertised host's invocation behavior and unchanged status reads. |
| 3 | Publish the human explanation, eight command reference entries, limitations, and evidence-based issue list. | Users need to understand the current method and the proposed changes independently. | High. Give an unfamiliar reader a small example and ask them to find the next command and reason. |
| 4 | Consolidate shared interview and context-reading rules, and add revision-aware replanning. | Shared rules and re-entry determine whether the method survives learning and change. | High to medium. Change a brief after one task is done and another is doing; account for every affected task. |
| 5 | Add a verified GitHub adapter and an installation compatibility suite. | Hosted behavior has more failure modes than local files. | High. Exercise more than 30 tasks, native blockers, same-account review, rejected writes, and pending merge. |
| 6 | Add small-work entry, research resolution, and optional verification guides by medium. | Borrow composability and stronger feedback without growing the mandatory process. | Medium. Compare a correction, a feature, a hard bug, and a non-code deliverable. |
| 7 | Add richer context handoff, prototype variations, and alternative-design exploration where measurements justify them. | These can improve judgment but should follow a reliable core. | Exploratory. Measure answer quality, restarts, time to a useful artifact, and user interruptions. |

### Influences worth carrying forward

The strongest reusable ideas are the public-interface test boundary from [TDD and codebase-design](../reference/mattpocock-skills/skills/engineering/codebase-design/SKILL.md), falsifiable feedback from [diagnosing-bugs](../reference/mattpocock-skills/skills/engineering/diagnosing-bugs/SKILL.md), complete slices and staged migration from [to-tickets](../reference/mattpocock-skills/skills/engineering/to-tickets/SKILL.md), and progressive disclosure from [writing-for-agents](../reference/mattpocock-skills/skills/productivity/writing-for-agents/SKILL.md). Atlas can apply those principles to its own framework: a small command interface, explicit inputs and outputs, a clear source for each fact, and independent tests of transitions.

Treat writing advice as a hypothesis about agent behavior. Claims such as negative phrasing causing worse outcomes or a particular token count marking a reasoning boundary are not established by the files themselves. Test shortened and expanded instructions on the same scenario set. Prefer instructions that yield correct state, useful evidence, and fewer avoidable human interruptions over instructions that merely look minimal.

Any future copied implementation text should keep provenance with the adaptation. The local [MIT license](../reference/mattpocock-skills/LICENSE) contains the copyright and permission notice for the reference. Conceptual influence, adapted prose, and copied source deserve distinguishable records; this note supplies an evidence trail but is not a license audit.

The proposed result is Atlas as a small, reliable project method with optional specialist methods. Its five things should make sessions resumable and decisions traceable, while the skills remain interchangeable ways of producing and checking that record. The standard for an addition is an observable improvement in a real route through the method, not the presence of a similarly named skill in another catalogue.

## Copied into

The [framework review](2026-09-13-review-atlas-framework.md) and its [local plan](../plan/) incorporate the comparison and adoption order. The [README](../README.md) explains the resulting direction and known platform limits. Proposed design changes remain candidates until the relevant work records their adoption.

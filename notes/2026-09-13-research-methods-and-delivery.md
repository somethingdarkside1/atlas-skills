---
date: 2026-09-13
kind: research
part: project
---

# Reusable methods, project delivery rules, and focused context

## Summary

Atlas should separate its project record, reusable methods, and project delivery instructions. Keep GitHub delivery compatible with Atlas while making local plan files the first public release's supported task home, then require demonstrated demand and contract tests before adding a hosted tracker. Reuse interviewing, diagnosis, verification, and prototyping through small, explicitly reached references, and earn claims of lower context cost through measured discovery tests.

## Detail

### Evidence and limits

This is a design recommendation grounded in the current Atlas files, Matt Pocock's local reference, and official documentation fetched on 2026-09-13. It supplements the [earlier comparison](2026-09-13-research-matt-pocock-comparison.md), which records the local reference's provenance limits. No comparative model evaluation, isolated installer run, or live tracker migration was performed for this note.

The public [grilling](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md) and [diagnosis](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/diagnosing-bugs/SKILL.md) sources were also read. Upstream links are moving references. The comparison package should pin a revision and record local source hashes before a reproducible public benchmark. Recommendations below are architectural judgments, not measured superiority claims.

### Separate three responsibilities

Atlas's current [build](../skills/build-it/SKILL.md), [review](../skills/review-it/SKILL.md), and [plan format at the start of this analysis](archive/2026-09-13-initial-review/plan/README.md) couple tracker choice to branch creation, commit timing, PR creation, approval, and merge. Consequently, changing where a task lives also changes how the project ships. The two reasons for change are independent.

Adopt three responsibilities:

| Responsibility | Owns | Completion |
| --- | --- | --- |
| Atlas operation | Select a target, read its current contract, perform the bounded work, update the five things | Its recorded postconditions hold, or a precise interruption is recorded |
| Reusable method | A disciplined way to answer a question, investigate a failure, establish evidence, or compare alternatives | Its result meets explicit evidence criteria and returns to the operation |
| Project delivery instructions | Commit timing, branches, worktrees, pushes, PRs, merge, release | The project's declared delivery requirement has observable confirmation |

A review can be clean while a PR awaits a required approval. A merged PR can contain a change that invalidates an earlier review. Represent both facts explicitly. The task's accepted result and delivery state need separate meanings, with prerequisite readiness defined against the evidence actually required by the dependent task. That definition belongs in the task format, not in a GitHub branch inside a skill.

`/review-it` should judge a specified result revision against a specified brief revision, record findings and limits, and update the task's review state. If project instructions authorize the same session to merge after checks, the agent can then perform that delivery work under those instructions. This preserves automation while removing merge ownership from the review method. A merge conflict that changes the result requires renewed checks against the changed revision.

### Make the shared rule small and enforceable

A proposed shared rule is: “Follow the active project instructions for delivery. Preserve unrelated work. Record the target, the changes owned by this operation, and the evidence for its result.” Each operation should identify the active instructions during preflight and report any unresolved conflict that affects the next action.

Keep the rule reachable from every installed operation. The project instruction file holds the project's actual choices. Generalize the questions a delivery policy answers, rather than shipping universal answers:

- What change boundary deserves a commit, and which checks precede it?
- Does work start in the current checkout, a branch, or a worktree? From which baseline?
- When are pushes and PR creation authorized, and which remote and base branch apply?
- Which evidence and approvals allow merge, who performs it, and which merge strategy applies?
- What happens to temporary branches and worktrees after confirmed integration?

Absence of a policy leaves these choices to the user's current authorization and the host's normal rules. It should not make every Atlas operation invent a branch, auto-commit, or stop for a fresh permission ritual. A non-Git folder remains a supported project.

Preserving unrelated work needs a concrete boundary. Record the initial status and relevant diff before mutation. A path list alone is insufficient when a user already edited the same file: commit ownership may need hunk-level selection or a separate checkout. The rule should state the intended preserved result; project tooling determines how to achieve it.

OpenAI documents that Codex loads project instructions along the path to its working directory and that nearer instructions can override earlier guidance. It also documents a size limit. Setup therefore needs to inspect applicable instructions, including overrides, and verify what the target host actually loads. A root `AGENTS.md` is not proof that every session sees the same policy. [Official OpenAI documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

### Add setup, retain a read-only entry point

Add `/setup-atlas` for installation into a project, repair, and migration. Keep `/atlas` as orientation and routing. Setup should inspect existing homes, project instructions, applicable nested rules, and any existing workflow before proposing changes. Re-running it should preserve user text and either make a precise migration or report that nothing needs changing.

Matt's [setup skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md) is a useful influence: it discovers current tracker and domain arrangements, writes focused project references, and updates an identified instruction block. Atlas should improve on its fixed preference for `CLAUDE.md` whenever present. Select or adapt the entry point the user's host loads, while keeping one authoritative policy body when several host files point to it.

Separate a versioned Atlas-owned block from a project-owned delivery section. An Atlas upgrade can change its own routing pointer and format version. Editing delivery policy is a separate, reviewable configuration change. Use existing user authorization for routine setup; ask only for genuinely unresolved consequential choices. An interrupted run needs a detectable partial state and an idempotent continuation.

Success includes content preservation, valid links, a second run with no unintended diff, and a fresh-session check that finds the intended instructions. Setup should not infer merge permission from contributor counts or treat a GitHub remote as a request to move the plan into GitHub.

### GitHub: remove coupling before deciding the adapter

For the first public release, recommend local plan files as the supported canonical task record and support normal GitHub delivery through project instructions. This immediately supports local tasks plus branches and PRs, local tasks with direct commits, and projects without Git.

Keep future hosted tracking as a distinct adapter decision. A hosted adapter must map stable Atlas identities, readiness, delivery evidence, review history, cancellation, and reopening onto the provider without treating issue assignment or closure as complete lifecycle evidence. It also needs complete pagination, readback after writes, interrupted-write recovery, and one declared home for current task truth. A casual mirror creates two editable authorities and a synchronization product.

This recommendation limits release scope; it does not prove that GitHub tracking is undesirable. Before removing existing configuration, inventory active users and provide an export or migration path. A representative hosted-workflow scenario can later justify an adapter. The public release should advertise only supported behavior actually tested.

### Four reusable methods

**Interview.** Borrow dependency-ordered questions, recommended answers, and the separation of facts from choices from Matt's [grilling](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md). Improve completion: “every imaginable branch visited” has no practical finite bound. Define the decision needed, evidence already available, open prerequisites, decision owner, and the uncertainty that can remain. A round is complete when its independent material questions have answers or explicit deferrals. The interview is complete when the brief is actionable within scope, with remaining assumptions recorded and reopening triggers stated. Honor decisions already delegated to the agent. Research resolvable facts directly. Use concrete counterexamples to sharpen terms instead of interviewing the user about facts in the repository.

**Diagnosis.** Borrow the reproducible symptom, discriminating feedback loop, ranked hypotheses, focused probes, and original-scenario rerun from Matt's [diagnosis](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/diagnosing-bugs/SKILL.md). Improve the boundary: diagnosis can end with a demonstrated cause, an evidence-backed narrowing, or a precise access limitation. Static investigation remains useful when a production symptom cannot be replayed; distinguish suspicion from confirmation. Fixing is a subsequent authorized build action. Choose a time budget for minimization and a statistically appropriate treatment of intermittent failures rather than demanding a universal fast, deterministic reproduction.

**Verification.** Borrow meaningful public behavior checks and independently derived expectations from Matt's [TDD](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md), and separate specification and convention checks from his [review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md). Generalize across media: execute code behavior, inspect document facts and rendered pages, compare design variants at intended sizes. Each claim needs an artifact revision, procedure, expected result, observed result, and limitation. Pass, fail, and unable-to-check are distinct. Verification supplies evidence; review judges its adequacy. Test-first development is an optional code method, not a universal Atlas requirement.

**Prototype.** Borrow question-dependent artifacts, easy launch, and visible relevant state from Matt's [prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md). Improve it with a hypothesis, distinguishing observation, effort bound, and explicit inconclusive result. A prototype can be code, a document, a service experiment, or a visual comparison. Retain the evidence needed to understand the verdict. Production use goes through a task and normal verification. Prototype storage and branch policy remain project choices; the Atlas requirement is a resolvable artifact and a note connecting evidence to the open question.

A fifth shared domain method may emerge naturally from interviewing: distinguish overloaded terms, challenge relationships using scenarios, check existing behavior, then update the glossary and decisions. Matt's [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) demonstrates the difference between reading vocabulary and actively changing it. Start with that discipline inside the interview reference. Promote it separately only when independently useful routes need it.

### References first, additional skills when justified

Author these methods once as focused reference files. Each operation names the branch that requires the relevant method and consumes a defined result. For example, build loads diagnosis when the task concerns an unexplained failure; review loads verification for acceptance evidence; planning loads interview only for unresolved consequential sizing or scope choices.

A plain reference has no independent invocation policy and adds no extra skill to the host's discovery catalogue. A model-invoked method earns a separate skill when users need it outside Atlas operations, its trigger is specific, and its output contract is meaningful independently. Avoid creating empty wrappers solely to imitate another catalogue.

Distribution needs a deliberate solution. The [skills installer](https://github.com/vercel-labs/skills) supports selecting individual skills. A reference outside an installed skill's directory may therefore be absent. Prefer one canonical authoring source plus generated, checked-in copies inside each skill that needs it, with a sync check and provenance marker. Generated duplication in the distribution is compatible with one editable source. This has maintenance cost, but permits selective installs without hidden runtime dependencies. Whole-bundle installation is a simpler alternative if explicitly required and verified. Test the chosen policy rather than assuming a cross-skill dependency manager exists.

The [Agent Skills specification](https://agentskills.io/specification) supports references loaded on demand and recommends shallow relative links. Host invocation semantics are additional constraints: [Claude documents](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill) that a user-only skill cannot be invoked automatically or reproduced through another route after a blocked invocation. [OpenAI documents](https://learn.chatgpt.com/docs/build-skills) its own implicit-invocation control. Shared reference reuse is appropriate; using references as a disguised bypass for an explicitly restricted operation is not. Keep automated multi-operation execution out of the first release until its callable surface is intentional and host-tested.

### Labels should route, not replace reading

Use the map's stable part identifiers and concrete task links first. Add a small context index only when the project needs it: part, purpose, paths, relevant decisions, methods, and conditions for expanding scope. Optional labels such as `format`, `lifecycle`, or `distribution` can help retrieve candidate work, but a label is not an ownership boundary or evidence that other files are irrelevant.

A build's minimum context is its whole task, applicable brief, linked decisions, relevant glossary entries, active project instructions, and actual touched files. Inspect callers, consumers, shared contracts, and tests when a change crosses those boundaries. A review needs the same relevant surroundings plus its baseline and result identity. A narrow initial index must not turn into a prohibition on looking further.

Move detail behind conditional pointers, not behind chains of label dictionaries. Avoid maintaining another copy of task state in the index. Derive mechanical indexes where useful, validate targets and identifiers, and retain repository search as a fallback when labels are missing or stale.

The official [Agent Skills specification](https://agentskills.io/specification) and [OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills) support progressive loading; they do not establish that adding a directory or labels reduces total task tokens. The relevant comparison includes index tokens, fetched files, repeated reads, irrelevant output, missed context, retries, and user interruptions. An extra index that agents always read can increase cost.

### Proof before public claims

Run the same scenarios against the current framework, revised framework, and reference methods with recorded versions, equivalent tools, and comparable task inputs. Use multiple runs for judgments sensitive to model variation. Evaluate outcomes before interpreting token counts.

Required scenarios include:

1. Setup with existing instructions, a partial Atlas installation, both host files, nested overrides, and a repeated invocation.
2. Selective installation of each skill into an isolated directory, with every required reference resolvable.
3. A delegated small choice, a consequential unanswered choice, and a fact obtainable from the repository.
4. A deterministic bug, an intermittent symptom, and an unavailable reproduction environment.
5. Review findings followed by repair, review of changed evidence, and clean review pending external integration.
6. Unrelated edits in another file and in the same file, under commit, branch, and worktree policies.
7. An inconclusive prototype and a non-code deliverable with appropriate evidence.
8. Missing or stale labels and a change whose effects cross the initially selected part.

Score correct state transitions, preserved work, usable evidence, unnecessary blocking, context retrieval failures, total tokens, and time to an accepted result. The proposed differentiation is a coherent, resumable project record with bounded methods and delivery independence. It becomes a credible advantage when these scenarios demonstrate it.

## Copied into

The [architecture review](2026-09-13-review-methods-and-project-policy.md), proposed decisions 0012 through 0017, and the [active work packages](../plan/README.md) incorporate these recommendations. This note remains the dated evidence and proposal record.

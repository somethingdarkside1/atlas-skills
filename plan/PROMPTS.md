# Prompts for the Atlas work packages

Copy one entire prompt into a new agent session opened in this repository. The agent then reads current files, so these prompts remain usable as task states change. They are launch instructions; the brief and task files own scope, dependencies, and acceptance. [COORDINATION.md](COORDINATION.md) links the seven GitHub package issues.

## Which prompt to use

Start with **Core model** while `core-model/01` is unresolved. It is a decision task and may need your answers. Use the other package prompts only as their task blockers become satisfied. A package can have eligible early tasks and blocked later tasks; issue-level closure is not its execution dependency graph.

Each package prompt starts or resumes one task and prepares a PR. It does not launch seven agents, execute the entire release, or grant blanket permission to merge or publish. The separate review/integration and release prompts state those scopes explicitly. Existing session authorization still applies. Use a separate worktree for simultaneous work and coordinate shared contract changes through the task owner.

| Package | Current brief | Prompt |
|---|---|---|
| core-model | [Brief](core-model/brief.md) | [Start](#core-model) |
| shared-methods | [Brief](shared-methods/brief.md) | [Start](#shared-methods) |
| project-setup | [Brief](project-setup/brief.md) | [Start](#project-setup) |
| work-skills | [Brief](work-skills/brief.md) | [Start](#work-skills) |
| context-routing | [Brief](context-routing/brief.md) | [Start](#context-routing) |
| validation | [Brief](validation/brief.md) | [Start](#validation) |
| public-release | [Brief](public-release/brief.md) | [Start](#public-release) |

## core-model

Settle Atlas work, evidence, and project-workflow boundaries.

```text
Work in the Atlas repository, somethingdarkside1/atlas-skills. Read the applicable AGENTS.md, INDEX.md, plan/README.md, and the package brief below. Read relevant glossary entries, linked decisions, and the full selected task, including blockers and evidence. Inspect branch, worktree, merge state, and existing edits before changing files; preserve unrelated work and its staging state.

Package: plan/core-model/brief.md. The package issue is linked from plan/COORDINATION.md.

Start with core-model/01 if it is still open. Read decisions 0012 through 0017 and the relevant glossary clusters. Stress-test a code PR, a document delivery, and a non-Git prototype. Distinguish operation completion, acceptance, integration, readiness, and project authorization. Ask a small round of concrete questions only for material choices that remain unresolved. A proposal is not an accepted answer.

After my answers, record the actual decisions, rationale, and scope, then complete the selected decision task. Continue to task 02 or 03 only if I selected that task or ask you to continue. Later tasks define revision-bound evidence and a repeatable legacy migration; preserve old ids, history, and project customizations.

Select one eligible task in this package using the current local task states and access to blocker outputs. Prefer its existing resumable attempt when relevant. If none is eligible, report the exact blockers and the next action; keep their acceptance states truthful. Keep remaining material questions pending and continue only independent work until answered.

Make the declared output, verify its Done when criteria, and record Delivered and Review against the actual output and scope. Run python3 scripts/check-project.py and the task-specific checks. A passing structural check does not establish agent behavior. Update only the current homes affected by the work.

Follow AGENTS.md for delivery. Commit the coherent owned changes, push the task branch, and open or update a focused PR. Reference the package issue using Refs rather than a closing keyword for partial package work. Leave the PR ready for review; perform merge or release only when the current session separately authorizes it. End with the task id, what changed, evidence and limits, branch/commit/PR, unresolved action, and next eligible task.
```

## shared-methods

Build reusable interview, diagnosis, verification, and prototype methods.

```text
Work in the Atlas repository, somethingdarkside1/atlas-skills. Read the applicable AGENTS.md, INDEX.md, plan/README.md, and the package brief below. Read relevant glossary entries, linked decisions, and the full selected task, including blockers and evidence. Inspect branch, worktree, merge state, and existing edits before changing files; preserve unrelated work and its staging state.

Package: plan/shared-methods/brief.md. The package issue is linked from plan/COORDINATION.md.

Select one eligible method task, 01 through 04, or task 05 when all its blockers are accepted. Use the adopted core boundary rather than reopening it. Read only the relevant method sources and consumer operations, preserving attribution where material is adapted.

For interviewing, resolve consequential uncertainty and domain distinctions while retaining settled choices. For diagnosis, separate observations from hypotheses and use a discriminating check. For verification, bind actual check results and limitations to the examined output and scope. For prototypes, name the bounded question, observation, limits, and verdict, including inconclusive results. The caller owns persistence and state transitions.

Demonstrate the selected method in its required contexts. For task 05, author once, generate checked references for consumers, and prove selective installation has all required resources. Finish the selected task rather than rewriting the entire method set.

Select one eligible task in this package using the current local task states and access to blocker outputs. Prefer its existing resumable attempt when relevant. If none is eligible, report the exact blockers and the next action; keep their acceptance states truthful. Keep remaining material questions pending and continue only independent work until answered.

Make the declared output, verify its Done when criteria, and record Delivered and Review against the actual output and scope. Run python3 scripts/check-project.py and the task-specific checks. A passing structural check does not establish agent behavior. Update only the current homes affected by the work.

Follow AGENTS.md for delivery. Commit the coherent owned changes, push the task branch, and open or update a focused PR. Reference the package issue using Refs rather than a closing keyword for partial package work. Leave the PR ready for review; perform merge or release only when the current session separately authorizes it. End with the task id, what changed, evidence and limits, branch/commit/PR, unresolved action, and next eligible task.
```

## project-setup

Adopt projects with a separate setup-atlas operation.

```text
Work in the Atlas repository, somethingdarkside1/atlas-skills. Read the applicable AGENTS.md, INDEX.md, plan/README.md, and the package brief below. Read relevant glossary entries, linked decisions, and the full selected task, including blockers and evidence. Inspect branch, worktree, merge state, and existing edits before changing files; preserve unrelated work and its staging state.

Package: plan/project-setup/brief.md. The package issue is linked from plan/COORDINATION.md.

For task 01, discover existing project instructions and conventions, then settle only the missing adoption choices using non-Git, local Git, and PR-based examples. Preserve the user's existing delivery policy and authorization.

For task 02, implement the separate setup operation against empty, populated, partial, legacy-context, and linked-instruction fixtures. Account for every preserved item, make the adoption diff reviewable, and show that a repeated run is stable. Setup adopts policy; it does not infer push or merge permission from a remote or contributor count.

For task 03, exercise the same Atlas acceptance under different project delivery policies. Preserve unrelated edits and distinguish an accepted result from a failed or pending integration. Use authorized scratch resources. Complete only the selected eligible task.

Select one eligible task in this package using the current local task states and access to blocker outputs. Prefer its existing resumable attempt when relevant. If none is eligible, report the exact blockers and the next action; keep their acceptance states truthful. Keep remaining material questions pending and continue only independent work until answered.

Make the declared output, verify its Done when criteria, and record Delivered and Review against the actual output and scope. Run python3 scripts/check-project.py and the task-specific checks. A passing structural check does not establish agent behavior. Update only the current homes affected by the work.

Follow AGENTS.md for delivery. Commit the coherent owned changes, push the task branch, and open or update a focused PR. Reference the package issue using Refs rather than a closing keyword for partial package work. Leave the PR ready for review; perform merge or release only when the current session separately authorizes it. End with the task id, what changed, evidence and limits, branch/commit/PR, unresolved action, and next eligible task.
```

## work-skills

Refine the eight Atlas operation contracts.

```text
Work in the Atlas repository, somethingdarkside1/atlas-skills. Read the applicable AGENTS.md, INDEX.md, plan/README.md, and the package brief below. Read relevant glossary entries, linked decisions, and the full selected task, including blockers and evidence. Inspect branch, worktree, merge state, and existing edits before changing files; preserve unrelated work and its staging state.

Package: plan/work-skills/brief.md. The package issue is linked from plan/COORDINATION.md.

Choose one eligible task from this package. Read its operation sources, adopted formats, applicable shared methods, and relevant evidence from codex/second-pass-reference. Adopt useful prior work selectively and validate it against the newer contracts.

For each operation in the selected task, specify required and conditional reads, owned writes, observable finish, and durable recovery. Cover the task's normal and failure paths with actual artifacts. Keep work acceptance and project delivery separate. Project instructions own commits, branches, worktrees, pushes, PRs, and merges.

Exercise draft operations in scratch projects. Task 05 performs the consistent cutover only after its blockers pass: atlas becomes read-only orientation, setup handles adoption, local files own task state, and unsupported hosted tracking or automatic go is explicitly deferred. Avoid a partial format migration that breaks untouched consumers; surface a cross-task contract dependency when necessary.

Select one eligible task in this package using the current local task states and access to blocker outputs. Prefer its existing resumable attempt when relevant. If none is eligible, report the exact blockers and the next action; keep their acceptance states truthful. Keep remaining material questions pending and continue only independent work until answered.

Make the declared output, verify its Done when criteria, and record Delivered and Review against the actual output and scope. Run python3 scripts/check-project.py and the task-specific checks. A passing structural check does not establish agent behavior. Update only the current homes affected by the work.

Follow AGENTS.md for delivery. Commit the coherent owned changes, push the task branch, and open or update a focused PR. Reference the package issue using Refs rather than a closing keyword for partial package work. Leave the PR ready for review; perform merge or release only when the current session separately authorizes it. End with the task id, what changed, evidence and limits, branch/commit/PR, unresolved action, and next eligible task.
```

## context-routing

Implement and measure focused context routing.

```text
Work in the Atlas repository, somethingdarkside1/atlas-skills. Read the applicable AGENTS.md, INDEX.md, plan/README.md, and the package brief below. Read relevant glossary entries, linked decisions, and the full selected task, including blockers and evidence. Inspect branch, worktree, merge state, and existing edits before changing files; preserve unrelated work and its staging state.

Package: plan/context-routing/brief.md. The package issue is linked from plan/COORDINATION.md.

For task 01, build on existing part ids and the trigger-to-source directory. Each pointer must resolve to an authoritative source. The selected task should load its brief, relevant formats and decisions, needed method, and affected dependencies. Expand to both sides of a changed boundary. Keep status and task truth in their existing homes.

For task 02, compare focused and broad reads on the same tasks after the revised operations are available. Include a missing pointer, renamed part, shared dependency, and stale index. Measure reads and loaded bytes; give tokenizer counts only when actually measured. Report missed evidence, quality, retries, and human interruptions alongside cost. Retain a simpler directory unless another label layer demonstrably helps.

Select one eligible task in this package using the current local task states and access to blocker outputs. Prefer its existing resumable attempt when relevant. If none is eligible, report the exact blockers and the next action; keep their acceptance states truthful. Keep remaining material questions pending and continue only independent work until answered.

Make the declared output, verify its Done when criteria, and record Delivered and Review against the actual output and scope. Run python3 scripts/check-project.py and the task-specific checks. A passing structural check does not establish agent behavior. Update only the current homes affected by the work.

Follow AGENTS.md for delivery. Commit the coherent owned changes, push the task branch, and open or update a focused PR. Reference the package issue using Refs rather than a closing keyword for partial package work. Leave the PR ready for review; perform merge or release only when the current session separately authorizes it. End with the task id, what changed, evidence and limits, branch/commit/PR, unresolved action, and next eligible task.
```

## validation

Prove the revised Atlas workflow with independent evidence.

```text
Work in the Atlas repository, somethingdarkside1/atlas-skills. Read the applicable AGENTS.md, INDEX.md, plan/README.md, and the package brief below. Read relevant glossary entries, linked decisions, and the full selected task, including blockers and evidence. Inspect branch, worktree, merge state, and existing edits before changing files; preserve unrelated work and its staging state.

Package: plan/validation/brief.md. The package issue is linked from plan/COORDINATION.md.

Choose one eligible validation task and treat checks as evidence, not a claim that the release is ready. For task 01, extend meaningful structural invariants and include deliberately invalid fixtures. For task 02, create real software and non-code artifacts covering normal work, interruption, findings, waiting, cancellation, stale review, and changed scope.

For task 03, use an independent agent or fresh session with a realistic request, raw fixture, and minimum required inputs. Keep expected results and suspected bugs out of the evaluator prompt. Compare actual outcomes afterward. Record revision, model/harness, checks, observations, limitations, and unresolved failures. Use authorized disposable resources for external effects. Distinguish static checking, behavioral evidence, installation evidence, and comparative claims.

Select one eligible task in this package using the current local task states and access to blocker outputs. Prefer its existing resumable attempt when relevant. If none is eligible, report the exact blockers and the next action; keep their acceptance states truthful. Keep remaining material questions pending and continue only independent work until answered.

Make the declared output, verify its Done when criteria, and record Delivered and Review against the actual output and scope. Run python3 scripts/check-project.py and the task-specific checks. A passing structural check does not establish agent behavior. Update only the current homes affected by the work.

Follow AGENTS.md for delivery. Commit the coherent owned changes, push the task branch, and open or update a focused PR. Reference the package issue using Refs rather than a closing keyword for partial package work. Leave the PR ready for review; perform merge or release only when the current session separately authorizes it. End with the task id, what changed, evidence and limits, branch/commit/PR, unresolved action, and next eligible task.
```

## public-release

Document, install, and publish the verified Atlas release.

```text
Work in the Atlas repository, somethingdarkside1/atlas-skills. Read the applicable AGENTS.md, INDEX.md, plan/README.md, and the package brief below. Read relevant glossary entries, linked decisions, and the full selected task, including blockers and evidence. Inspect branch, worktree, merge state, and existing edits before changing files; preserve unrelated work and its staging state.

Package: plan/public-release/brief.md. The package issue is linked from plan/COORDINATION.md.

Select task 01 or 02 when eligible. Write accurate public documentation and provenance for Atlas by Vitali Liouti, retaining required credit for adapted material. For installation, test a clean profile at a fixed candidate revision with every required method and template, the supported namespaces, collision handling, and uninstall behavior.

Make support claims only from recorded evidence. Prepare a reviewable PR with the exact candidate, public copy, checks, and remaining limits. This package-start prompt prepares the release; use the separate release prompt for task 03 once its prerequisites and release version are settled. An available source repository is not a validated tagged release.

Select one eligible task in this package using the current local task states and access to blocker outputs. Prefer its existing resumable attempt when relevant. If none is eligible, report the exact blockers and the next action; keep their acceptance states truthful. Keep remaining material questions pending and continue only independent work until answered.

Make the declared output, verify its Done when criteria, and record Delivered and Review against the actual output and scope. Run python3 scripts/check-project.py and the task-specific checks. A passing structural check does not establish agent behavior. Update only the current homes affected by the work.

Follow AGENTS.md for delivery. Commit the coherent owned changes, push the task branch, and open or update a focused PR. Reference the package issue using Refs rather than a closing keyword for partial package work. Leave the PR ready for review; perform merge or release only when the current session separately authorizes it. End with the task id, what changed, evidence and limits, branch/commit/PR, unresolved action, and next eligible task.
```

## Pick one specific task

Replace `<part/NN>` with a real active task id. Use this when you already know the exact slice you want handled.

```text
Complete Atlas task <part/NN> in this repository. Read applicable AGENTS.md, INDEX.md, plan/README.md, the owning brief, and the full task plus its blockers and relevant decisions. Follow the corresponding package guidance in plan/PROMPTS.md. Verify that blocker outputs are accepted and accessible before starting; resume the existing attempt if one exists. Settle only the remaining material choices with me, using concrete scenarios and facts you can obtain yourself.

Implement and verify this task's declared output. Preserve unrelated work, keep current homes and evidence accurate, run the project checker and task-specific checks, then commit, push, and open or update its focused PR under project policy. Reference the package issue without closing it for a partial task. Leave the PR ready for review. Report the result, evidence, revision, PR, limits, and next action.
```

## Resume interrupted work

Replace `<part/NN>` with the task to resume. The task record should supply the branch and PR; discover and verify them before changing anything.

```text
Resume Atlas task <part/NN>. Read applicable AGENTS.md, INDEX.md, its brief and task, the relevant handoff, and current Git/PR state. Compare the saved pointers with actual files and current scope. Locate the existing attempt and preserve its partial work and unrelated edits. Report any mismatch that changes what should happen next.

Continue from the first incomplete valid step rather than recreating tasks, artifacts, or PRs. Ask only for a still-required answer that is not already recorded. Verify the resulting output, update its evidence and pending action, run required checks, and commit/push the owned continuation to the existing PR. Leave integration for its current authorization. End with exact resumable pointers if anything remains blocked.
```

## Review and integrate one PR

Replace `<PR URL>` and `<part/NN>`. Pasting this prompt authorizes integration of that named PR when its current revision satisfies the checks. It does not authorize an unrelated tag or release.

```text
Review and, if acceptable, merge <PR URL> for Atlas task <part/NN>. Read applicable AGENTS.md, the current brief and task, required decisions, actual PR base/head, changed artifacts, and relevant project standards. Verify the result against the task criteria and scope using current evidence; keep review findings separate from GitHub approval and merge eligibility.

Fix actionable in-scope findings and repeat the affected checks. Record the reviewed revision, actual results, limitations, and any required human judgment. If acceptance, required checks, or required approval is missing, leave a precise pending action and keep the PR unmerged.

Once the current revision satisfies acceptance and platform requirements, merge using the project policy and authorization in this prompt. If integration changes the content, rerun affected checks before claiming acceptance of the integrated result. Fetch and verify the merged revision. Synchronize the appropriate local main checkout while preserving other sessions' work. Close the package issue only if all its required tasks and overall outcome have verified completion; otherwise report remaining work. Finish with PR, merge revision, checks, and next task.
```

## Publish the verified release

Replace `<version>` with the agreed release version. Use only after the local blockers of `public-release/03` have accepted evidence. This prompt explicitly authorizes the scoped public release; a missing required judgment remains a blocker.

```text
Complete Atlas public-release/03 for the agreed version <version>. Read applicable AGENTS.md, INDEX.md, the public-release brief and task, the accepted installation and behavioral evidence, current package metadata, license/provenance, and the exact candidate revision. Verify every prerequisite and support claim, and reconcile the candidate with any changes since those checks ran.

Prepare the exact release diff and notes, resolve in-scope defects, and complete the project's authorized PR/merge workflow with required checks and approvals. Then tag and publish <version> in somethingdarkside1/atlas-skills under Vitali Liouti's attribution. Preserve required notices. Verify the public installation route at the published revision and record its observed result.

Use existing remote state to recover from a partial attempt without duplicating or overwriting a published tag. If a prerequisite, access, judgment, or check prevents publication, record the exact blocker and usable recovery state. Report the release URL, tag, revision, supported installation, validation evidence, and any remaining limits. Close the release package issue only when its full outcome is demonstrated.
```

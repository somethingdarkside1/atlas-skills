<!--
FORMAT. One project term per entry. Define what it is in one or two sentences; use _Avoid_ for genuinely confusing synonyms and _Not_ only for a useful neighboring distinction. External names remain accurate in quotations and integrations. These entries are authoritative; GLOSSARY.md is their index. Add a term when its distinction changes a decision or behavior. Update the index relationship view when an entry changes a represented relation.
-->

# Work

**Work package**:
The bounded work for one part of this release plan, described by a brief, tasks, read scope, ownership, and a completion condition.
_Avoid_: workstream

**Brief**:
The account of what a part must achieve and why, with its scope and settled choices.
_Avoid_: spec, PRD

**Task**:
One independently verifiable piece of work in the plan, with stable identity, explicit blockers, and acceptance checks.
_Avoid_: ticket, story

**Ready**:
A task that can start because its required blockers are accepted and their exact needed outputs are accessible in a project-permitted workspace. Integration is required only when the dependency's outcome or project policy requires it.
_Avoid_: unblocked

**Delivery**:
The retrievable, revision-identified output of a task together with the verification that was actually performed. The identity accounts for the actual examined content with or without Git.
_Avoid_: build result
_Not_: Integration, where that output enters the project workflow.

**Acceptance**:
A recorded judgment that a specific delivery satisfies the identified applicable brief and task criteria. Changes to content or scope require an impact assessment and renewal of affected acceptance while preserving prior evidence.
_Avoid_: approval
_Not_: Integration, moving the output through the project workflow.

**Integration**:
The project action that places an identified output into its required shared destination.
_Avoid_: merge as a synonym for done
_Not_: Acceptance, whether the output meets its criteria.

**Project authorization**:
Permission under applicable instructions and user direction to perform a project action. Acceptance or a navigation pointer cannot grant it; existing authorization continues to apply within its scope.

**Cancellation**:
Removal of planned work with its identity and reason retained. Incoming dependencies require explicit replacement or removal with a scope rationale, since canceled work supplies no accepted output.

**Finding**:
An evidenced mismatch between a delivery and an applicable requirement, with its impact and a usable correction target.
_Avoid_: observation as a synonym for defect

**Handoff**:
A note carrying the unresolved session context and exact pointers needed to resume current work.
_Avoid_: checkpoint as a synonym for commit

**Sketched**:
A part whose scoped direction remains to be adopted.
_Avoid_: todo part

**Decided**:
A part whose scoped direction and brief are adopted sufficiently for its next work.
_Avoid_: fully known

**Building**:
A part with active work toward its adopted scope.
_Avoid_: doing part

**Done**:
A task or part whose required outcome has current acceptance evidence.
_Avoid_: closed issue
_Not_: Integration, a separate project step unless it is the named task outcome.

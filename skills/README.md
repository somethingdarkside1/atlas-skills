# Skill authoring

The nine operations implement the integrated process candidate under [work-skills/07](../plan/work-skills/07-integrated-process-candidate.md) and proposed [0028](../decisions/0028-evaluate-a-small-integrated-process.md). [GUIDE.md](../GUIDE.md) explains the human workflow. Format-3 templates and generated consumer methods are included; candidate checks do not substitute for clean-profile host installation, the deferred human run, or a tagged release. The prior 0.2 behavior remains retrievable in project history.

## Contract before prose

The candidate contracts below define each operation. The skill body implements its contract; project formats own shared state and evidence rules. Evaluate these fields when changing an operation:

| Contract field | Meaning |
|---|---|
| Reads | Required inputs, conditional inputs, and where to expand scope |
| Changes | Owned artifacts and allowed state transitions |
| Finished | Observable evidence that this operation has completed its job |
| Recovery | A durable waiting/failure record and the exact resumable target |

The operation follows applicable project instructions and preserves unrelated work. Project instructions own commits, branches, worktrees, pushes, PRs, and merges. A successful review is an acceptance result; integration follows the project's separately authorized workflow.

## Source layout

Keep one flat `skills/<name>/` folder per installable skill. Its `SKILL.md` holds the operation; `agents/openai.yaml` holds supported invocation metadata; its conditional references and templates live beside it. The project templates live in `skills/setup-atlas/templates/`, and every other skill reads formats from the project's own homes, never from another skill's folder. Author shared methods once in `methods/`, with the consumer map in `methods/consumers.json`. Generate copies with `python3 scripts/bundle-methods.py`; check source identities with `--check`. Consumer copies retain attribution and contain no sibling-skill dependencies. The shared evidence helper is authored in `scripts/evidence.py` and generated the same way.

An index or label is a pointer, not a method body. Load a method only for the branch that requires it. An independently invocable method earns a public skill only when a real use case and invocation test justify that interface.

## Procedure shape

Keep the skills simple under [0025](../decisions/0025-finish-simple-skills-before-the-human-run.md). The [Matt comparison](../notes/2026-09-19-research-matt-simplicity.md) supplies the rationale and examples for this standard:

- Write the operation's essential sequence in plain steps. Keep a rule when it defines an Atlas boundary or prevents a concrete failure; remove repeated instructions and prose that adds nothing to the agent's normal work.
- State the required information or result. Prescribe a tool, shell command, exact phrase, or count only when correctness depends on it. Formats still own the fields other operations consume.
- Keep each rule in one home. A skill points to the project's format instead of retelling it, and to project instructions for saving work.
- Keep guidance needed on every path visible. Move a substantial conditional branch behind a clear pointer only when other paths can skip it. Count the references read during a run when assessing complexity.
- Use examples to explain a difficult choice. Keep regression cases in validation fixtures rather than turning every observed incident into another universal instruction.
- Verify simplifications against the affected success and recovery cases. Word counts can reveal growth, but a shorter file alone does not demonstrate better behavior.

1. Resolve the target and read the relevant current formats and project instructions. Done when the target and prerequisites are known.
2. Perform the operation using the selected shared method where needed. Done when its declared output and evidence exist.
3. Record the resulting state or the unresolved action and return a usable next step. Done when a fresh session can verify completion or resume.

Adapt the number of steps to the operation. Each step has an observable completion condition. A read command must return cleanly under zsh when a folder or file kind is absent (no bare `folder/*.md` globs) and must not match an example block inside a README or a format comment; check it against a templates-only folder and a copy of `examples/brand/`. A save step identifies the owned changes and follows the applicable project policy; message wording and commit timing belong to that policy. Setup resolves adoption conflicts and restores missing required homes; another operation points to setup when its required state is absent. Report enough detail to recover from a failure. Use positive instructions with explicit ownership and prerequisites.

## Invocation and packaging

Public state-changing operations remain explicitly invoked for the first revision. The router recommends their actual installed names. Automatic continuation is deferred until the harness policy and bounded progress tests support it; a pointer to a disabled skill does not bypass that restriction. Shared plain references can be read as method guidance by their owning operation.

Keep metadata consistent with supported hosts and validate the file contents rather than their line count. The current five-line `openai.yaml` shape is valid:

```yaml
interface:
  display_name: "Operation name"
  short_description: "One concrete job"
policy:
  allow_implicit_invocation: false
```

## Completion checklist

- The operation and each shared method have one source for their rules.
- Reads, owned writes, completion, and failure handling match the adopted format and decisions.
- Project delivery policy stays in project instructions and is honored by the run.
- Selective installation contains every required reference with a valid source version.
- Applicable structural checks pass, and the package's behavioral cases have recorded results.
- Human documentation describes demonstrated behavior and links remaining work.

## Candidate operation contracts

| Operation | Required reads and expansion | Owned changes | Finished or recovery |
|---|---|---|---|
| setup-atlas | Existing homes, project purpose, instructions and authority; migration guidance for old formats | Missing homes, scoped format upgrades and instruction pointers | Consistent adopted homes, or a precise conflict with old authority preserved; rerun continues adoption |
| atlas | Map directory and task state, then selected brief/evidence and relevant handoff | None | An actionable next step, acceptance, or a named wait; unrelated questions do not steal focus |
| interview-me | Selected scope, decisions and affected tasks; interview method, diagnosis only for unexplained failure | Brief, adopted/proposed choices, relevant terms and map questions; impacted acceptance records | Scope sufficient for next work, or one recorded unresolved input/experiment |
| plan-it | Brief, task format, existing and incoming dependencies; interview method for material decomposition choices | Tasks and affected dependency/map pointers | Verifiable work with valid ids and blockers, or a specific missing decision/input |
| build-it | Task/attempt, brief, requirements, actual blocker outputs and project conventions; diagnosis/verification as needed | Task output, its delivery and affected part progress | Verified delivery awaiting separate review, or partial work and exact pending action |
| review-it | Actual output and scope, criteria, standards and dependencies; verification/diagnosis as needed | Review, affected task acceptance and combined part acceptance | Supported acceptance, material correction, or version-bound human wait |
| map-it | Map format, affected part records and inbound links; interview method for responsibility changes | Map views and owned links | Consistent structure or a named fault; never invented Outcome acceptance |
| prototype-it | Question, deciding evidence, prior experiments and prototype method | Experiment, dated evidence and answer/pending pointer | Supported answer, required preference, or next observation for an inconclusive result |
| park-it | Current target/attempt, workspace and relevant existing handoff | Missing durable facts and a useful handoff/export | Exact resumption pointers or reuse of an unchanged adequate handoff |

# Skill authoring

The nine skill folders are the draft at 0.2: the earlier draft patched under [decision 0021](../decisions/0021-patch-the-draft-first.md) so an ordinary run works, with `setup-atlas` split out of `atlas`. It has not been run end to end. The [work skills package](../plan/work-skills/brief.md) defines the rest of the migration; the [shared methods package](../plan/shared-methods/brief.md) defines reusable reasoning. Shared method bundles are planned, not yet installed here.

## Contract before prose

Every operation declares these in its brief before implementation:

| Contract field | Meaning |
|---|---|
| Reads | Required inputs, conditional inputs, and where to expand scope |
| Changes | Owned artifacts and allowed state transitions |
| Finished | Observable evidence that this operation has completed its job |
| Recovery | A durable waiting/failure record and the exact resumable target |

The operation follows applicable project instructions and preserves unrelated work. Project instructions own commits, branches, worktrees, pushes, PRs, and merges. A successful review is an acceptance result; integration follows the project's separately authorized workflow.

## Source layout

Keep one flat `skills/<name>/` folder per installable skill. Its `SKILL.md` holds the operation; `agents/openai.yaml` holds supported invocation metadata; its conditional references and templates live beside it. The project templates live in `skills/setup-atlas/templates/`, and every other skill reads formats from the project's own homes, never from another skill's folder. Author shared methods once when the shared-methods package creates their canonical source. Package generated copies inside the skills that need them and validate their source hashes so selective installation has every required reference.

An index or label is a pointer, not a method body. Load a method only for the branch that requires it. An independently invocable method earns a public skill only when a real use case and invocation test justify that interface.

## Procedure shape

1. Resolve the target and read the relevant current formats and project instructions. Done when the target and prerequisites are known.
2. Perform the operation using the selected shared method where needed. Done when its declared output and evidence exist.
3. Record the resulting state or the unresolved action and return a usable next step. Done when a fresh session can verify completion or resume.

Adapt the number of steps to the operation. Each step has an observable completion condition. A read command must return cleanly under zsh when a folder or file kind is absent (no bare `folder/*.md` globs) and must not match an example block inside a README or a format comment; check it against a templates-only folder and a copy of `examples/brand/`. A save step names the skill's files and its message, and points to the project's `Saving work` section for everything else. Initialization identifies missing homes and restores them; another operation points to setup when its required state is absent. Report enough detail to recover from a failure. Use positive instructions with explicit ownership and prerequisites.

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

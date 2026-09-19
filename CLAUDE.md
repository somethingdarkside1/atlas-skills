# Atlas project instructions

## Read by scope

Read [INDEX.md](INDEX.md) to select a part, then its brief, the chosen task, and relevant terms in [GLOSSARY.md](GLOSSARY.md). [MAP.md](MAP.md) owns the shape; [plan/README.md](plan/README.md) owns the current work format. Read the format of each home you change and the decisions it cites. Expand through affected dependencies and applicable nested instructions.

## This repository

Atlas is by Vitali Liouti. The active plan prepares the next public release. `skills/` contains the integrated process candidate under work-skills/07, built on the 0.2 patch; the work packages retain its adoption and release checks. Execute draft skills against scratch fixtures during validation. Use the package start prompts for work on this repository.

- `INDEX.md` routes reads; the five things own project state.
- `skills/<name>/` remains flat. Follow [skills/README.md](skills/README.md) when editing skills.
- `examples/` holds teaching fixtures; copy them before a run.
- `notes/archive/` preserves superseded planning evidence. [plan/MIGRATION.md](plan/MIGRATION.md) maps it to current work.
- `reference/` is an ignored comparison copy. Retain source attribution for any adapted material.
- Keep `AGENTS.md` and `CLAUDE.md` resolving to these same instructions.

## Delivery policy for this repository

This section is project policy, separate from Atlas's method. Applicable user instructions and existing authorization determine the permitted actions.

1. Inspect the branch, worktree, merge state, staged diff, and existing changes before editing. Preserve unrelated work and its staging state.
2. Use a `codex/<work-name>` branch from current `main` for a coherent work package. Resume its existing branch when appropriate. Use a separate worktree when another session owns the checkout or an isolated run needs it.
3. Validate the chosen work with the checks named by its task. Review the actual staged diff. Commit the coherent owned changes with a message describing the result; retain incomplete work with an accurate handoff when a check fails.
4. Push and open a PR when the user's request or an explicit project delegation covers those actions. A PR names the work, evidence, and remaining limits. Reuse its existing PR when continuing the same work.
5. Merge when authorized and the current PR revision satisfies its acceptance and applicable required checks. Use a merge commit for this repository's architecture and work-package changes so source history remains traceable. Fetch the result and confirm local `main` matches it. Record a blocker if account permissions or remote policy prevent completion.
6. A review report records acceptance and findings. Run delivery actions as a separate project step. Preserve the reviewed revision if integration changes it, and rerun affected checks before claiming the integrated result is accepted.

For this planning task, the user's instruction explicitly authorizes the push and merge. Public source publication is separate from tagging a validated skill release; the latter has its own task in the public-release package.

## Writing and verification

Use plain words and sentences with commas, colons, periods, or parentheses. Each rule has one authoritative home. Read [skills/README.md](skills/README.md) for procedure shape and method packaging. Put consequential proposed choices in `decisions/` with their actual status. Preserve historical notes; write a new dated note for later conclusions.

Run `python3 scripts/check-project.py` for project links, active task dependencies, package coverage, and metadata. Run any additional checks required by the selected task. A structural pass is evidence about documents and packaging; behavior is established by the validation work package.

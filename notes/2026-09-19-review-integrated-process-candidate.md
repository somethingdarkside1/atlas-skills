---
date: 2026-09-19
kind: review
part: work-skills
---

# Integrated process candidate: implementation and observed runs

## Summary

The candidate implements the requested guide and all nine operations with shared formats, stable identities, focused routing, and explicit progress or waiting. Isolated agent runs exercised software, an event plan, and exhibition adoption without the tested repetition and completion failures. This accepts the candidate work in work-skills/07, with the release, installation, and human checks below still outstanding.

## Detail

### Examined output and scope

Work was isolated on `codex/atlas-process-revision`, based on `72e890a`, under the user's 2026-09-19 request. The scope is [work-skills/07](../plan/work-skills/07-integrated-process-candidate.md), its [brief](../plan/work-skills/brief.md), and proposed [0028](../decisions/0028-evaluate-a-small-integrated-process.md). Separate review and combined Outcome acceptance remain settled requirements; the glossary and receipt refinements are implemented proposals for evaluation, not invented answers to prior questions.

The [source manifest](evidence/2026-09-19-process/candidate-source.json) identifies 53 candidate source files by SHA-256, including the guide, nine skills, templates, methods, generated consumers, helper, packaging, and checks. Its own SHA-256 is `290418bf55a2c63e18414dffd899c8a2a65a18b38b474396603b95e20df68b62`. The [observed fixture archive](evidence/2026-09-19-process/observed-fixtures.json) preserves 55 resulting files and symlink targets. Absolute paths inside archived text identify historical scratch locations; the JSON preserves the contents without requiring those locations to remain available.

### Segmented assessment

| Layer | Implemented choice | Reason and evidence |
|---|---|---|
| Human process | Set up, clarify where needed, plan, build, separately review | Removes unnecessary interviews for settled work; software build stopped at review, which was invoked separately |
| Organisation | Responsibilities/outcomes with stable ids; one owner and linked views | Software display rename preserved `totals`, task paths, acceptance, and navigation |
| Meaning and decisions | Useful distinctions, small choices in briefs, consequential choices with actual status | Exhibition setup reused CONTEXT rather than duplicating its glossary; interview reused settled scope |
| Planning | Small verifiable slices, real accepted-output blockers, preserved existing work | Accepted function stayed done while the missing usage guide became task 02 |
| Evidence | Output and scope identities; meaningful checks; retain otherwise unrecoverable prior results | Changed seating source renewed the count check; helper tests distinguish output, requirements, and bookkeeping |
| Progress and recovery | Target first, current records before handoffs, unchanged wait reused | Event repeated review and router changed no files; missing blocker produced a recovery action |
| Methods and packaging | Matt-derived reasoning adapted once, copies generated inside consumers | Every skill's relative resources resolve when copied alone; missing/stale bundles are detected |
| Delivery | Follow the project's authority and permissions | Scratch policies prohibited commits and external actions; runs saved local artifacts only |

### Observed operation runs

Three agents began in fresh contexts, each with one isolated fixture and the named skill source. Subsequent operations in a fixture were separately requested, but reused that agent's conversation. This is forward execution of instructions, not installed slash-command dispatch or independent review by a different model. The parent examined the resulting records; same-context builder/reviewer limits are explicit in them.

| Scenario and sequence | Observed result |
|---|---|
| Software: build `totals/01` | Corrected invoice arithmetic, preserved interface and unrelated personal file. Four initial tests exposed the bug; expanded six-method suite passed after correction. Delivery was `review`, part `building`, with a separate review recommendation. |
| Software: separately review `totals/01` | Reran six tests and checked 3,232 cases against exact rational arithmetic. Accepted task 01 but kept the part building: its brief also promised an absent usage guide. Routed known missing work to plan, without another scope interview. |
| Software: plan, then map rename, then park, then atlas | Added guide task 02 with blocker 01; renamed display to Invoice calculations while preserving id and paths. Handoff named target/workspace/evidence. Read-only router selected the ready guide task. |
| Event: review, repeated review, then target router | Reconciled 32 + 60 = 92 and kept organiser sightline judgment unticked. Old same-target and newer unrelated handoffs did not override current delivery. Repeat and router left all 12 then-existing file identities unchanged and reported the same human wait. |
| Event: source change, review, build, separate review | Changed front seats per row from 8 to 9. Review found 32 should be 36 and 92 should be 96, returned the task to doing, and preserved unaffected evidence. Build corrected the counts and recorded delivery 2; separate review verified it and returned to the organiser wait, with no fabricated approval. |
| Existing exhibition: setup, repeated setup, router | Preserved catalogue, British house style, CONTEXT meanings, and shared instruction symlink. Created missing homes and linked the existing language owner. Repeat setup and router left all 10 path identities unchanged. No parts or tasks were invented. |
| Exhibition: interview with supplied settled direction | Recorded one decided exhibition part and brief from the given outcome. No redundant confirmation or invented user decision. Actual missing object-source information remained visible. |
| Exhibition: prototype an explicit label question | Made three comparable A1 label alternatives before a question marker existed, preserved “date unknown”, inspected SVG structure, and recorded an inconclusive preference. No production label or task was manufactured. Rendering, printing, and visitor readability were explicitly untested. |
| Software copy: remove accepted blocker output, then build guide | Moved totals.py to retained/totals.py while task 01 still said done. Identity check failed and checks could not import the module. Task 02 recorded doing with a recovery/verification action; no guide, restored output, or new acceptance was invented. |

The event retention snapshot correctly names its limit: it contains the old room plan and the changed source used by review 2, not the original delivery-1 source. The evaluator deliberately changed that source outside the workflow. A receipt cannot recover bytes that were never retained; the candidate's preservation rule addresses edits made through its workflow.

### Repeating the scenarios

Run `python3 scripts/create-process-fixtures.py /absolute/new/scratch-directory`. The destination must not exist. This recreates the three starting fixtures with deliberate defects and pending judgments. Invoke each skill separately against the selected fixture, using its local instruction policy, and inspect actual file/state changes after each step rather than supplying the expected answer as user direction.

For exhibition interviewing, the supplied direction was: a one-day free event for local residents in an already booked hall; all 30 selected objects need labels and a printed catalogue; include a 20-minute introduction; reuse existing content; no website, fundraising, or acquisitions; ordinary reversible choices are delegated. For the prototype, compare A1 labels so the accession and date can be found easily; the date is unknown and the organiser has not chosen a layout. For the event change, set front `seats_per_row` to 9. For the missing-output case, copy the completed software fixture and move totals.py into a retained folder before invoking task 02.

This is a reproducible fixture and scenario recipe, not a deterministic assertion that another model will make the same choices. The archived artifacts show the actual observed outcome of this run.

### Structural and helper checks

- `python3 scripts/test-evidence.py`: nine passing tests, covering content/scope changes, bookkeeping stability, missing files and removals, safe path boundaries, retained output survival, and task headings inside fenced examples.
- `python3 scripts/test-packaging.py`: three passing tests, covering exact bundles, individual-skill relative resources, and deliberately missing/stale consumer copies.
- `python3 scripts/bundle-methods.py --check`: current generated copies, including retained source and license notices.
- `python3 scripts/check-project.py`: no errors across active project links, metadata, tasks, dependencies, and package coverage. Remote links and behavior are outside this check.
- Ruby's YAML parser: all nine frontmatters and invocation metadata validated, including explicit invocation flags and short-description limits. The skill-creator quick validator could not run because PyYAML was absent in both available Python environments; its source also omits the existing disable-model-invocation field from its allowlist. That validator is not reported as passed.
- `claude plugin validate .` and `claude plugin validate .claude-plugin/plugin.json`: both passed. These validate manifests, not clean-profile installation or invocation.
- `bash -n scripts/link-skills.sh` and `git diff --check`: passed.
- Fixture generator: created all three starting projects in a new destination. Its initial indentation defect was corrected before retaining the final source; the successful regeneration is the checked result.

The primary reviewer read the guide, all nine operation instructions, common formats, helper and bundle code, and the actual fixture task records. Changes to helper heading handling, scope-file display, metadata, and documentation during evaluation did not alter the tested state transitions; final helper and packaging tests cover those changes. No unresolved material finding was identified within the candidate task's scope.

### Remaining limits

These cases support the specific demonstrated behavior, not a guarantee against every loop or suitability for every domain. A real domain supplies its own authoritative sources, tools, checks, and human judgments. Hosted authority migration conflicts, concurrent writers, cancellation with complex incoming dependencies, large split maps, external-service evidence, and installed-host dispatch still require their package cases.

Clean-profile installation, the agreed human cold run, original package acceptance, and release tagging remain with their existing tasks. The integrated candidate supplies reusable output and evidence to those tasks; it does not mark them done, close package issues, or change proposed decisions to accepted.

## Copied into

- [Candidate task and acceptance](../plan/work-skills/07-integrated-process-candidate.md).
- [Human guide](../GUIDE.md) and [operation contracts](../skills/README.md).
- [Candidate decision](../decisions/0028-evaluate-a-small-integrated-process.md).

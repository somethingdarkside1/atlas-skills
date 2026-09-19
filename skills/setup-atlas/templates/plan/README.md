# Plan

Atlas format: 3
Tracker: files

One folder per part contains its brief and numbered tasks. The plan owns work, waiting, delivery, and acceptance. The map links here; it does not copy task state.

## Working rules

Start with the user's target, its brief, applicable project instructions, and the relevant records. Follow links to decisions, required outputs, and affected parts when their facts matter. Read a glossary entry to resolve meaning, rather than loading every term. Missing optional context is a discovery problem; missing required scope or an unavailable accepted output needs an explicit next action.

Use the smallest useful route. A clear request within a settled brief can be one task without another interview. A new or materially changed outcome needs clarification first. Update only homes whose facts changed. Skill invocations do their named operation; build ends with a separate review recommendation.

Before changing files, inspect existing work and preserve unrelated edits and staging. Save owned changes under project instructions. Commits, branches, pushes, merges, publishing, and external actions follow the project's existing authorization. When no delivery policy exists, leave the files saved in the workspace and report that state.

A return names what changed, what is verified or unresolved, and the next useful action. Use `Next: /command <target>` for an available operation, or `Next: waiting for <input or event>, then /command <target>`. Use the actual installed command name. A recommendation never invokes another operation or supplies permission.

**Progress and waiting.** A repeated operation first checks its existing output and latest pending action. Continue when new input, changed evidence, or an untried relevant action makes progress possible. Otherwise report the existing wait without duplicating records or sending the same unchanged work between skills. Investigate a repeated failure before another attempt; record the missing input or next discriminating check when no justified action remains. Waiting on one target does not block unrelated eligible work.

## Brief

`plan/<part>/brief.md` has `part: <stable-id>` frontmatter and these sections:

- `Problem`: who needs what to change and why.
- `Outcome`: the observable result, including how its combined usefulness can be assessed.
- `Decisions`: linked consequential choices and short settled choices that need no separate file.
- `Out of scope`: explicit exclusions.

A draft can exist before adoption. Mark unresolved scope as `Draft:` below the title and keep only material open questions on the map. Record agreed answers as they arrive. When changing adopted scope, retain its prior version through project history or a dated note before overwriting it. Name affected tasks and assess their acceptance, rather than restarting the whole project.

## Tasks and dependencies

A task is `plan/<part>/NN-<slug>.md`; its id is `<part>/<NN>`. Numbers are never reused. Inside a part, blockers may use the short number. Quote blocker ids in frontmatter. A changed display name does not change the part id or its task paths.

```md
---
status: todo
blocked_by: []
---

# 01: Deliver the agreed result

## Delivers
One independently checkable output, in the medium the task needs.

## Check by
A check that could fail if the result is wrong, with its expected answer from the brief, a source of record, or a person.

## Done when
- [ ] The required result exists and passes its check
- [ ] (you) A stated judgment only the person can make

## Delivered

## Review
```

An optional `kind: decision | build | check | release` describes the output; it adds no new lifecycle. Tasks may deliver decisions, experiments, documents, data, code, or external work. Use complete useful slices. For a wide change that cannot be sliced independently, plan compatible expansion, migration, and removal, or an explicit integration task with its verification boundary.

| State | Meaning and owner |
|---|---|
| todo | Planned by plan-it; ready only when blockers are accepted and their needed outputs are accessible. |
| doing | Started or resumed by build-it, or returned for changes by review-it; may have a pending question or failed check. |
| review | Delivered by build-it; awaiting review or a required human judgment. |
| done | Accepted by review-it against the identified output and scope. |
| canceled | Removed by plan-it with its reason and incoming dependencies repaired. |

Read blocker outputs as well as their states. Part `Needs` edges concern prior decisions; task `blocked_by` edges concern accepted outputs. Neither an issue label nor a merge substitutes for acceptance. Integration is part of acceptance only when this task explicitly delivers it or project policy requires it.

Plan-it preserves historical deliveries and reviews. It can revise active scope under the user's instruction, recording affected work and renewing affected acceptance. A canceled task supplies no output: repair every incoming dependency with an explicit replacement or scope reason. Check missing ids, self-dependencies, and cycles before calling the plan ready. Existing work is resumed or revised, not recreated because another command was run.

## Delivery and review evidence

Append a compact entry when a delivery, finding, decision, or pending action changes. Give entries distinct headings (date and a local suffix suffice for repeats). A stopped attempt records its workspace, usable partial output, check or question, and exact next action; it remains doing.

A delivery records the output location, what was checked and observed, and any unchecked criterion. Identify both the output (`Version:`) and applicable brief and task criteria (`Scope:`). For files, name the examined paths (`Files:`), including explicit removals when relevant, and use a repeatable content identity. Record additional scope sources or the identity command when needed to reproduce the scope check. Exclude bookkeeping files from the output set unless they are themselves the deliverable. The build and review skills include an optional evidence helper when the project has no equivalent.

Git history or the project's artifact versioning can retain the accepted result. Outside such storage, retain a copy before replacing an accepted output or its scope. The short identity stays in the task; copies are needed only where the earlier result would otherwise become unrecoverable. For an external result, use its stable record/version and inspection time, or state the limit if it cannot be retrieved. An unverifiable required result stays unresolved.

A review names `Reviewed:` and `Scope:`, records criteria and conventions separately, and states findings with a location, consequence, and useful correction. Record only checks actually performed. Human-only criteria stay unticked until the person confirms them for this output; a later change renews affected judgments. A platform approval records platform state, not a substitute for examining the work.

Changed content or scope triggers impact assessment: reuse unaffected evidence, renew affected checks, and preserve the earlier review. Review-it may complete the new checks within the requested review when evidence suffices; otherwise it records exactly what build-it or the person must supply. Correct a harmless reporting mistake in the review instead of forcing an unchanged artifact through another build.

## Completing a part

Task acceptance and part acceptance are different. Once the current tasks are accepted or deliberately canceled, review-it checks the combined result against the brief's Outcome and exclusions. Record that assessment in the final task's Review and link it from the map's `Acceptance:` field. Keep the part building if work is missing, retaining valid task acceptance and recording `Remaining work:` with a pointer for plan-it. A map redraw cannot infer this assessment from task counts. Later scope or result changes invalidate only the affected acceptance and reopen the part when needed.

## Earlier projects

This format replaces the draft's state-only handoff freshness and output-only checksum. Setup adopts it explicitly, preserving ids, custom content, prior evidence, and project policy. Old accepted tasks keep their historical state, but missing outputs or missing identity are not invented: verify what a new dependent or changed scope actually requires. Hosted-task projects keep their old authority until an explicit migration accounts for every task and dependency.

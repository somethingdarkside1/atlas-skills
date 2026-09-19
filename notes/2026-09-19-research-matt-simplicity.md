---
date: 2026-09-19
kind: research
part: project
---

# Matt's simplicity and Atlas finalisation

## Summary

Matt's useful example is a small operation with a clear purpose, a few consequential constraints, and references reached only when needed. His collection also contains long procedures, rigid defaults, and a composition gap, so matching its shortest files would not establish reliability. Atlas should remove duplicated rules and unnecessary prescriptions while retaining its shared work record, honest acceptance, and recoverable progress.

## Detail

### Scope and provenance

The user accepted completing the remaining release plan, asked to keep the skills simple like Matt's, and deferred their fresh-session run until the candidate is in good shape. This note supplies research and recommendations, not acceptance of new contracts or evidence that the release passes.

Inspected Matt Pocock's public repository on 2026-09-19 at [commit c55ee46073ed923f86ce59a5eb3b6d895095d1b7](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7), committed 2026-09-18. A shallow clone is at `/private/tmp/atlas-matt-simplicity-20260919`; the ignored Atlas reference copy was not changed. Its [package metadata](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/package.json) reports 1.2.3. All upstream links below are pinned and usable without that local clone.

This supplements the [September 13 comparison](2026-09-13-research-matt-pocock-comparison.md) and [September 15 boundary research](2026-09-15-research-matt-boundaries-efficiency.md), which could not identify exact upstream commits. It does not retroactively establish their snapshots. Atlas examples below were inspected at `472ca95`, before this finalisation pass.

### What actually makes Matt's skills simple

**The operation has one recognizable job.** [Implement](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/implement/SKILL.md) is a small sequence: implement the given work, use TDD where possible, check it, review, commit. [Grilling](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling/SKILL.md) organizes questions by settled prerequisites, lets each answer change the next round, and assigns fact discovery to the agent. These central ideas are easier to follow than a catalogue of every possible situation. The concrete constraints matter more than terse wording.

**Small entry points compose substantive methods.** [Grill-with-docs](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/grill-with-docs/SKILL.md) invokes grilling and domain modeling instead of restating either. [Domain modeling](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/SKILL.md) creates documents only when there is material to record and limits ADRs to consequential, surprising tradeoffs. A short wrapper is not evidence of a short execution path: its dependencies count too.

**Rules earn their place, and location follows use.** [Writing for agents](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/writing-for-agents/SKILL.md) recommends deleting whole instructions that do not change behavior, leaving cheap environmental lookups to the environment, keeping a meaning in one place, and grouping a concept with its rules. It keeps common steps visible and discloses references by branch. It says a split must earn its added load. My inference for Atlas is that moving all the same rules into extra files does not by itself simplify the operation. Its claims about model attention are author guidance, not measurements established by this inspection.

**The route scales to the work.** [Ask Matt](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/ask-matt/SKILL.md) skips spec and ticket decomposition for work that fits one session, while retaining its preceding interview; multi-session work gets a spec and tickets. It reserves the denser wayfinder route for a large uncertain effort. [The setup decision](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/.agents/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md) distinguishes required configuration from helpful context. Missing vocabulary should not automatically block an otherwise usable skill.

**References teach judgment with examples.** [TDD](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/SKILL.md) emphasizes tests through public behavior and independently derived expectations. Its [test examples](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/tests.md) show the difference between observing checkout behavior and asserting internal calls. [Prototype](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/SKILL.md) first chooses the question, then loads either logic or appearance guidance. These are useful distinctions that change the artifact, rather than arbitrary extra steps.

**Human explanation stays separate from the recipe.** [The documentation guidance](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/.agents/writing-docs.md) asks human pages to explain the defining constraint, when to use the skill, common questions, and observable signs that it is working. It discourages duplicating the agent procedure. Atlas can explain its lifecycle in human documentation without teaching the whole product again inside every skill.

### Brevity has limits

Whitespace-separated word counts of complete files, including frontmatter, provide scale only:

| Source | Words |
|---|---:|
| grill-with-docs | 35 |
| implement | 70 |
| grilling | 319 |
| prototype | 487 |
| TDD | 559 |
| setup-matt-pocock-skills | 1,008 |
| code-review | 1,064 |
| diagnosing-bugs | 1,402 |
| ask-matt | 1,769 |
| writing-for-agents | 1,777 |

These counts were computed with `len(Path(file).read_text().split())` against the pinned clone. Prototype's conditional LOGIC and UI files add 1,025 and 1,118 words respectively. This is a varied collection, not a universal short-file standard; counts omit the further context a run may load.

Several specifics should not be copied into Atlas:

- [Diagnosis](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/diagnosing-bugs/SKILL.md) usefully demands a symptom-specific feedback signal, but also prescribes seconds rather than minutes, complete minimization, and three to five hypotheses. Those are strong defaults for its intended hard-bug workflow, not universal requirements for document work, costly environments, or an already-demonstrated cause.
- [Prototype's UI guidance](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/UI.md) chooses a URL parameter, a floating switcher, and specific keyboard behavior. These make a particular UI experiment repeatable. Atlas's general prototype operation should let the question determine the medium and interaction.
- [Setup](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/setup-matt-pocock-skills/SKILL.md) chooses CLAUDE.md whenever present. Atlas should follow the actual host and existing project ownership instead of treating that preference as a portable rule.
- [Invocation guidance](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/.agents/invocation.md) tells skills to call a named Skill tool. That instruction alone cannot establish compatibility with a host exposing no such tool, or a selective installation missing the dependency. Keep Atlas's consumer packaging checks.
- Implement invokes review before committing, while [code-review](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/code-review/SKILL.md) constructs `git diff <fixed-point>...HEAD`. The command excludes uncommitted implementation changes. This is a static composition gap, not an observed failed execution. Atlas should explicitly cover the delivered candidate and relevant working changes.

### Assessment for Atlas

Atlas already has the right broad distinctions in its [authoring rules](../skills/README.md): operations own writes, methods supply reasoning, project policy owns delivery. Its current prose often repeats the distinction's implementation details rather than relying on the authoritative home. These are concrete simplification candidates, not a proposal to remove the shared state model:

The nine Atlas skill bodies contain 5,999 whitespace-separated words after excluding YAML frontmatter, with 61 explicit `Done when` phrases. The interview body has 1,231 words and review has 780, despite occupying only 36 and 30 lines including metadata. These counts use a different boundary from the full-file Matt table and are not a ratio comparison. They show why line count is a poor proxy: several numbered steps contain many separate conditions on one long line. Keep a completion test where it resolves uncertainty, rather than requiring the same phrase after every obvious action.

| Current example | Recommended treatment |
|---|---|
| [map-it](../skills/map-it/SKILL.md) repeats diagram construction already owned by the map format | Read the current map format and regenerate accordingly; keep the rule there once. |
| [atlas](../skills/atlas/SKILL.md) specifies five lines while its problems line allows multiple lines | Require a concise status and useful next action; let problems take the space they need. |
| Router and map reads contain literal grep pipelines tied to paths and presentation | Describe the records and fields needed. Keep a command only when its exact behavior is part of the contract and validated. |
| [setup-atlas](../skills/setup-atlas/SKILL.md) promises existing homes stay unchanged, then copies CONTEXT terms into the glossary | Preserve existing content and resolve conflicts under one clear adoption rule. Avoid overlapping promises that disagree. |
| Setup replaces an older Atlas block while preserving the separate delivery section | Make upgrades preserve project additions as well as unrelated sections; test rerunning setup on customized instructions. |

### Recommended direction, not new acceptance

1. Write each operation around its target, action, and observable result. Keep only the boundaries that change behavior: owned writes, real prerequisites, consequential choices, honest acceptance, and resumption.
2. Remove repeated format rules and incidental presentation constraints before adding references. A reference earns its existence because a real branch needs it, not because the top-level word count looks better afterward.
3. Keep fixed identifiers, dependencies, human checks, the examined output, and the findings loop. These make Atlas's persistent project record useful; deleting them would trade clarity for hidden ambiguity.
4. Use examples to exercise the rules rather than adding a new prohibition for every failure. Put shell commands, host behavior, release steps, and branch policy in their actual owner when the operation does not require them.
5. Validate the reduced path against the same meaningful cases: a small clear task, changed scope, interruption, review findings, a human-only judgment, selective installation, customized setup, and non-code work. Record regressions before deciding a removed instruction was unnecessary.

For example, a revised build procedure can have four visible stages: select a ready task or resume its recorded attempt, make the declared output, verify it against the task, then record delivery or the reason it is waiting. The project's task format supplies states and version fields, a diagnosis reference is reached for an unexplained failure, and project instructions supply saving policy. The stage count is an illustration, not a new mandatory format. Its value must be tested against the same interruption and review cases as the longer text.

No comparative run, token-saving measurement, speedup, or reliability ranking was established here. The remaining release plan and the user's deferred fresh-session run still own that evidence. Matt's [MIT license](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/LICENSE) must accompany copied or substantially adapted material; this note does not replace existing source attribution.

## Copied into

[Skill authoring](../skills/README.md) now states the simplification standard. [Decision 0025](../decisions/0025-finish-simple-skills-before-the-human-run.md) records the user's full-scope, simplicity, and cold-run timing instructions; the [work-skills brief](../plan/work-skills/brief.md) and [map](../MAP.md#work-skills) point here for the assessment. The specific procedure changes above remain recommendations for the owning tasks, not accepted or validated executable changes.

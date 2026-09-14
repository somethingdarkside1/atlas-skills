---
date: 2026-09-15
kind: review
part: shared-methods
---

# Diagnosis method demonstrations

## Summary

The primary agent followed the candidate diagnosis method on a software failure and a data-quality failure, then returned an inconclusive process result when evidence was unavailable. Executed software checks failed before a scratch correction and passed afterward; direct inspection reconciled the data discrepancy. These are synthetic, author-run demonstrations, not independent or cold-context validation of installed Atlas operations.

## Detail

### Examined output and scope

Task: [shared-methods/02](../plan/shared-methods/02-diagnose-with-evidence.md), with its original four Done when criteria unchanged. Base: `6737912`, containing accepted blocker output `208b197`. Workspace: `/Users/vitali/Documents/Projects/Skills Po`; branch: `codex/shared-methods-02-diagnosis`. The brief's only scope clarification in this task selects diagnosis's minimum return and points to its source; other methods and bundling remain pending.

The examined method and fixtures have the SHA-256 identities below. Paths are repository relative. This identifies the uncommitted candidate bytes used during the demonstrations, rather than treating the base commit as their identity.

| File | SHA-256 |
|---|---|
| methods/diagnosis.md | `488cd29a9f43b6f48eabdcad2888142b26cb516320617b3e1ba79bab49ba2fb3` |
| methods/README.md | `58f4f959b29ffde03575cb74095c6f6420b0dab8233a1b42d404eb5b442a716a` |
| tests/fixtures/diagnosis/README.md | `e373009b495488e4a3c9a5acb9d66624c0bc3775b137e44866472cfb19c9948e` |
| tests/fixtures/diagnosis/page.py | `00c3324386dbee875737f725585531b0df4e48cc9e3a278c5959f7b5de1f1083` |
| tests/fixtures/diagnosis/check_page.py | `fac4f98202f8e67dd626c8085bd446c76a7710e6d3a7897fa525c02d3087af34` |
| tests/fixtures/diagnosis/ledger.csv | `e2bd1a980c45b7c4f7896b65ed318b846d8133f7475d12521698fd30c09f5317` |
| tests/fixtures/diagnosis/export.csv | `b5ee996fea6484014079a3f1b30a36d4eeed5c794018a2eee99e72b2dc413285` |
| tests/fixtures/diagnosis/report.md | `e946d9a12d83cea6482e03e2fc7ae7af0e6cc9fab0e936af32b67603abd9f02c` |

Provenance: inspected local Matt Pocock `skills/engineering/diagnosing-bugs/SKILL.md`, SHA-256 `77f3cf31bc99b2f49af943222526531fcc9fc41d047626d3640e875e85af3e84`, from the reference labeled 1.2.3. No upstream commit identity is claimed. [The method](../methods/diagnosis.md) retains the upstream locator, attribution, and MIT notice. [Earlier comparison research](2026-09-13-research-matt-pocock-comparison.md) documents the reference-copy provenance limitation.

### Execution setup

Created `/tmp/atlas-diagnosis-r5o17S` with `mktemp -d /tmp/atlas-diagnosis-XXXXXX`, then copied `tests/fixtures/diagnosis/.` there with `cp -R`. Runtime: local macOS, Python 3.9.6. Repository fixtures remained unchanged. Reproduction starts with `python3 check_page.py` inside any fresh scratch copy; the faulty fixture intentionally exits 1.

The primary agent used the candidate's procedure directly under the package prompt. Consumer contexts below are simulated responsibilities, not invocations of the unmigrated draft skills. The inspected draft build, review, and interview operations establish relevant consumers; their persistence, tracker, and Git behavior were not executed or changed.

### Software failure, builder context

Question: why does a first page of size two omit B? Bound: two discriminating checks after initial reproduction. The initial `python3 /tmp/atlas-diagnosis-r5o17S/check_page.py` exited 1 with these actual results:

| Input, offset, size | Expected | Before | After scratch correction |
|---|---|---|---|
| A B C, 0, 2 | A B | A, fail | A B, pass |
| A B C, 2, 2 | C | C, pass | C, pass |
| empty, 0, 2 | empty | empty, pass | empty, pass |
| A B, 0, 1 | A | empty, fail | A, pass |

Before the next probe, the agent stated competing predictions in the session: pagination loss predicts a short direct function result; presentation loss predicts a complete direct result. The cheapest probe was a direct `page(['A', 'B', 'C'], 0, 2)` call, which printed `['A']`. Reducing input to A, B retained `['A']`. Inspection of the scratch source showed `items[offset:offset + size - 1]`. These observations support an endpoint error and weaken presentation loss within this fixture.

The second check changed only the scratch slice endpoint from `offset + size - 1` to `offset + size`, predicting that the original missing-item signal would pass. Rerunning the unchanged `check_page.py` exited 0 with all four results in the table. This is a discriminating intervention, not merely a prose account of intended behavior.

Returned result: endpoint error supported for these inputs; the caller can apply and verify the bounded correction. Limits: synthetic function only, no application rendering path, concurrency, negative arguments, or performance claim. The original failing source is retained in the repository; corrected material is only in scratch. No instrumentation was added; the scratch directory retains the experiment and can be discarded after review. No production task was accepted by the method.

### Data-quality failure, reviewer context

Question: why does the export exceed the ledger by USD 60? Bound: one row reconciliation after reading the failing totals. The report and both CSVs were read with `cat`; the report's same-day, same-currency, one-row-per-invoice contract fixes the expected basis. The agent then stated predictions before the probe: duplication predicts a repeated key with a matching ledger amount; an amount error predicts unique keys with mismatched values.

The executed probe was `nl -ba` on each scratch CSV, followed by direct row comparison and arithmetic. Ledger lines 2 and 3 are A,40,USD and B,60,USD. Export lines 2 through 4 are A,40,USD, B,60,USD, B,60,USD. Ledger count is two, export count three; B appears twice with the same USD 60 amount. The sums are 40 + 60 = 100 and 40 + 60 + 60 = 160. The extra B row accounts exactly for the excess, supporting duplication and weakening the unique-key amount-error hypothesis.

Returned result: a review finding can name export line 4 and the one-row-per-invoice contract; the caller should investigate the export's source before applying a correction, then reconcile the regenerated output. Limits: this establishes a duplicate in the delivered data, not whether it arose from retry, join cardinality, or manual entry. No export generator, production ledger, or approval was available. The CSVs were not edited. This case used record inspection and arithmetic rather than software test requirements.

### Unsuccessful investigation, reported process constraint

Question: what explains the separately reported late approval? Bound: two evidence-availability checks. Expected timing cannot be established without an agreed deadline; actual timing is a report without a receipt. Candidate explanations remain unranked: a late handoff would predict a receipt after the deadline, while approval delay would predict a timely receipt followed by late approval. Neither has supporting observations.

Check one: `rg -n 'timestamp|deadline|approval|handoff'` against the scratch report and CSVs returned only report line 5, explicitly saying those facts were absent. Before the remaining check, the agent recorded that a handoff receipt could distinguish the explanations and that absence would leave the result inconclusive. Check two: `rg --files` for Markdown, CSV, log, and JSON inputs returned only README.md, report.md, ledger.csv, and export.csv. The accessible fixture set contains no timeline or receipt. No further probe within this bound can test the timing predictions.

Returned result: inconclusive, reproduction unavailable. Keep the late-approval report and both hypotheses unresolved; ask the process owner for the expected deadline, timezone, handoff receipt, and approval timestamp for the same instance. Resume by comparing those events. Missing evidence is a limitation, not proof of either cause or of no failure; the invoice duplicate does not establish a timing cause. This simulated missing input is not an outstanding user decision about the method implementation.

### Acceptance assessment

Primary-agent self-review examined the identified method, consumer declaration, and these demonstrations against the task and adopted boundary. All four criteria have evidence: failing software/data signals and an explicit reproduction limit; predictions and discriminating checks; a bounded inconclusive return retaining uncertainty; and software plus non-code contexts with different tooling. No actionable finding or human-only implementation judgment remains in this bounded scope.

Limits: the author knew the synthetic defects and executed the cases in the same context. This does not establish unseen-case reliability, independent review, model comparison, consumer invocation, selective installation, or a validated release. Those claims remain with the work-skills, bundling, and validation tasks. Structural check results are recorded in the task separately from this behavior evidence.

## Copied into

[Task 02](../plan/shared-methods/02-diagnose-with-evidence.md), [shared methods brief](../plan/shared-methods/brief.md), and [map](../MAP.md).

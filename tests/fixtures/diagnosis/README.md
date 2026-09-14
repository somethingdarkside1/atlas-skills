# Diagnosis cases

Copy this directory to scratch before executing or modifying it. These synthetic cases exercise [the diagnosis method](../../../methods/diagnosis.md); they are not production defects or an automated test of agent reasoning.

Software caller: a builder receives a missing-item report for the first page of A, B, C with size two. Run `python3 check_page.py` in the scratch copy; the intentionally faulty implementation must exit 1. Compare a direct function call with the report to distinguish pagination from presentation loss. A correction belongs only in scratch; rerun the original checks there.

Data caller: a reviewer receives [the report](report.md). Inspect [the ledger](ledger.csv) and [the export](export.csv) to distinguish repeated records from incorrect amounts. Keep the diagnosis separate from approving the export or editing the source of record.

Incomplete process caller: investigate the separate timing report using only these inputs, bounded to two evidence checks. Record the reproduction limit, missing evidence, and next action when timestamps and a deadline cannot be found. This case should remain inconclusive.

Record actual actions and outcomes against the method and fixture hashes. A scripted fixture pass is evidence of those data or code observations; claims about agent use require an observed execution record. The task's dated review note records the primary agent's demonstration and its limits.

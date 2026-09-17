# Verification cases

Copy this directory to scratch before running or changing it. These synthetic cases exercise [the verification method](../../../methods/verification.md). They are not production code or an automated test of agent reasoning. [The criteria](criteria.md) are the source of truth for both cases.

Code, builder and reviewer: `late_fee.py` has one seeded defect. `check_mirror.py` is a builder's check that copies the implementation's formula; `check_contract.py` takes its expected values from the criteria. In the scratch copy, run `python3 check_mirror.py` (it exits 0) and `python3 check_contract.py` (it exits 1). `ci.json` stands in for a platform status that ran only the mirror check. Put any correction in the scratch copy only, then rerun both checks.

Document, reviewer: `page.html` has one false opening time against `hours.csv`. Run `python3 check_page.py`; it checks the times, the notice order, and the declared notice colors, and exits 1. Phone layout needs a rendered page, and whether a visitor notices the notice needs a person.

Identity: from the scratch copy, run `shasum -a 256 <files in sorted order> | shasum -a 256 | cut -c1-12` over the files examined. The [evidence note](../../../notes/2026-09-17-review-verification-and-prototype-methods.md) records what was run and what was seen.

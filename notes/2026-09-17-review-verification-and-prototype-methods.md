---
date: 2026-09-17
kind: review
part: shared-methods
---

# Verification and prototype method demonstrations

## Summary

The primary agent followed the candidate verification method on a code delivery and a web page, and the candidate prototype method on a logic rule, a form layout, and an email subject line. Checks taken from the criteria caught both seeded defects while a check that copied the code passed, and the prototypes returned a measured answer, a choice left to a person, and `not clear yet`. These are synthetic, author-run demonstrations in one context, not independent validation or installed consumer behavior.

## Detail

### Setup and identity

Branch `codex/shared-methods-03-04` from `24b24ef`; macOS, Python 3.9.6. First run 2026-09-17; after review findings, every case was rerun on 2026-09-18 in a fresh `mktemp -d` folder under `$TMPDIR` that kept the repository paths, leaving the repository fixtures unchanged. Each identity is `shasum -a 256` over the listed files (repository paths, `LC_ALL=C sort` order) piped to `shasum -a 256 | cut -c1-12`; these replace the bare-name identities of 2026-09-17.

Methods: `methods/verification.md` `3e9a14fff873`, `methods/prototype.md` `38017700e61c`, `methods/README.md` `826b1fecad99`. Upstream sources, from the root of the local reference labeled 1.2.3: code-review `SKILL.md` with tdd `SKILL.md`, `mocking.md`, `tests.md` give `a41fec5755a8`; prototype `LOGIC.md`, `SKILL.md`, `UI.md` give `d95c20474ae4`.

### Verification: late fee code

Role: reviewer of a delivery that came with a builder's check and a platform status ([fixtures](../tests/fixtures/verification/README.md)). All files are in `tests/fixtures/verification/`. Delivery `check_mirror.py`, `late_fee.py`: `f15ffbb045b3`. Platform status `ci.json`: `cfcf91751ad2`. Criteria and reviewer check `check_contract.py`, `criteria.md`: `4400de0e1aea`.

| What was run | What was seen | Outcome |
|---|---|---|
| `python3 check_mirror.py` | 4 of 4 pass, exit 0; expected values reuse the code's `(days - 2) * 25` | Not a check: it repeats the code, so it cannot catch this defect |
| `cat ci.json` | `"state": "success"` for `python3 check_mirror.py`, marked synthetic | Platform status, quoted; covers only the mirror check |
| `python3 check_contract.py` | Criterion 2 fails: 4 days gives 50 (expected 25), 10 days gives 200 (expected 175); criteria 1, 3, 4 pass, including `ValueError`; exit 1 | Failed |
| Scratch fix to `(days_late - 3)`, delivery identity `912c87865ec1`, both checks again | Contract 7 of 7 pass, exit 0; mirror fails at 5 and 10 days, exit 1 | The contract check tracks the rule; the mirror check tracks the code |

Limits: seven chosen inputs; a stand-in for CI; the agent that seeded the defect wrote the check, so this does not show a reviewer finding an unknown defect.

### Verification: opening hours page

Role: reviewer. Delivery `page.html`: `95a49d78f795` (same bytes as on 2026-09-17). Source, criteria, and reviewer check `check_page.py`, `criteria.md`, `hours.csv`: `edb891b2b52c`.

| Criterion | What was run and seen | Outcome and limit |
|---|---|---|
| 1. Times match `hours.csv` | `python3 check_page.py`: Saturday is 10:00 to 16:00 in the source, 09:00 to 17:00 on the page; six days match; exit 1 | Failed. A row count (`grep -c '<tr><td>' page.html` gave 7) passed and could not see it |
| 2. Notice above table | Source order `['notice', 'table']` | Passed for source order only |
| 3. Contrast 4.5 to 1 | Declared `#ffffff` on `#b42318` gives 6.57; a scratch break to `#e57373` gave 2.99 and failed; the delivered file was restored and rechecked | Passed for declared colors, not the rendered page |
| 4. No sideways scroll at 375 pixels | No page was rendered | Not run: needs a browser at that width |
| 5. A visitor notices the notice | Nothing to run | Human-only |

Review of `9f7d0bc` found that the page check passed a page listing Saturday twice (wrong row, then right row) with exit 0, and stopped with a traceback on `background-color`; both were confirmed in scratch. After the fix, the repeated Saturday failed criterion 1 (exit 1), `background-color` was read as 6.57, and a three-digit `#fff` failed criterion 3 as unreadable, with no traceback. The delivered page's results did not change.

### Prototype: hold rule (logic)

Identity `tests/fixtures/prototype/holds.py`: `4c73ae44233c` ([fixtures](../tests/fixtures/prototype/README.md)). Question: can the proposed rule leave a returned book on the shelf while a member waits? Bound: three members, every legal sequence of up to six actions. `python3 holds.py` printed the state after each walkthrough action, refused a hold on a shelved book and a collect without an offer, and stopped after 228 legal sequences at the shortest case `hold Ben, return, hold Ana, cancel Ben`. `python3 holds.py pass-on` found no such state in all 1472 legal sequences. Both exited 0.

Measured facts within that bound. Proposed verdict `yes`, for the person to confirm; the pass-on result is not proof beyond the bound. The sequence search and refusals belong in the prototype because the question covers every sequence; saved data does not. Not modeled: offer expiry, several copies. Nothing was copied out; a copy of `step` would keep a pointer here and take normal verification.

### Prototype: renewal form (UI preference)

Identity `measure_options.py`, `options.html` in `tests/fixtures/prototype/`: `c9ba9ee0959b`. `python3 measure_options.py` (exit 0): option A has 5 fields, all before its one button, with 16 words before it; option B has 4 fields over 2 steps, with 2 fields and 11 words before its first button; no unlabeled fields. These are measured facts about the drafts; the agent did not render or view the page. Recommendation: B, because its first step asks for two fields and shows found details; this assumes the card lookup works. Verdict: waiting for the person.

### Prototype: renewal email subject (other media)

Identity `tests/fixtures/prototype/subjects.md`: `b0b549baf9da`. The two drafted lines were measured with the length one-liner in the fixture README, which printed 39 for A and 61 for B. A names the expiry date; B names the library and promises "two minutes", which nothing measured. The file has no list, send history, or past rates, so the deciding evidence is out of reach. Verdict: `not clear yet`. Next: send each line to a random half of the members due to renew and compare renewals, which needs the list, a way to send, and renewal counts.

### Limits

One agent wrote the fixtures, seeded the defects, and ran the cases in one context, on synthetic inputs. No consumer skill loaded either method (bundling is task 05), no page was rendered, and no real platform status exists. Structural check results and review records are in the tasks.

## Copied into

[Task 03](../plan/shared-methods/03-verify-by-medium.md), [task 04](../plan/shared-methods/04-prototype-to-learn.md), [shared methods brief](../plan/shared-methods/brief.md), [method consumers](../methods/README.md), and [map](../MAP.md).

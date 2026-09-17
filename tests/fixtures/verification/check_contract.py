"""Checks whose expected values come from criteria.md, including failure cases."""
import sys
from late_fee import late_fee

# (criterion, days late, expected cents or the expected error)
cases = [
    ("1", 0, 0), ("1", 3, 0),
    ("2", 4, 25), ("2", 10, 175),
    ("3", 23, 500), ("3", 30, 500),
    ("4", -1, "ValueError"),
]
failures = 0
for criterion, days, expected in cases:
    try:
        actual = late_fee(days)
    except ValueError:
        actual = "ValueError"
    passed = actual == expected
    failures += not passed
    print(f"criterion {criterion}: days={days} expected={expected} actual={actual} {'pass' if passed else 'fail'}")
sys.exit(1 if failures else 0)

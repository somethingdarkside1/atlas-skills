"""A builder's check whose expected values copy the implementation's formula."""
import sys
from late_fee import late_fee

failures = 0
for days in (1, 5, 10, 40):
    expected = 0 if days <= 3 else min((days - 2) * 25, 500)
    actual = late_fee(days)
    passed = actual == expected
    failures += not passed
    print(f"days={days} expected={expected} actual={actual} {'pass' if passed else 'fail'}")
sys.exit(1 if failures else 0)

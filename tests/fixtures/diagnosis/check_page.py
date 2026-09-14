"""Contract checks of visible page results, including the reported missing item."""
import json
import sys
from page import page

cases = [
    (["A", "B", "C"], 0, 2, ["A", "B"]),
    (["A", "B", "C"], 2, 2, ["C"]),
    ([], 0, 2, []),
    (["A", "B"], 0, 1, ["A"]),
]
results = []
for items, offset, size, expected in cases:
    actual = page(items, offset, size)
    results.append(dict(items=items, offset=offset, size=size,
                        expected=expected, actual=actual, passed=actual == expected))
print(json.dumps(results, indent=2))
sys.exit(0 if all(result["passed"] for result in results) else 1)

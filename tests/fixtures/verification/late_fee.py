"""Synthetic teaching fixture with one seeded defect. Do not use as production code."""


def late_fee(days_late):
    if days_late < 0:
        raise ValueError("days_late cannot be negative")
    if days_late <= 3:
        return 0
    return min((days_late - 2) * 25, 500)

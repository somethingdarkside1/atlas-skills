"""Intentionally faulty teaching fixture. Do not use as production code."""


def page(items, offset, size):
    return items[offset:offset + size - 1]

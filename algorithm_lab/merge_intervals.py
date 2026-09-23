"""Merge overlapping closed intervals, including intervals sharing an endpoint.

Return sorted (start, end) tuples in O(n log n) time and O(n) space. Reversed
bounds, non-integer bounds, and booleans are rejected; singleton intervals are valid.

>>> merge_intervals([(4, 7), (1, 3), (3, 5), (9, 9)])
[(1, 7), (9, 9)]
"""

from collections.abc import Iterable


def merge_intervals(intervals: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    rows = []
    for start, end in intervals:
        if any(isinstance(x, bool) or not isinstance(x, int) for x in (start, end)) or start > end:
            raise ValueError("intervals require integer start <= end")
        rows.append((start, end))
    result = []
    for start, end in sorted(rows):
        if result and start <= result[-1][1]:
            result[-1] = (result[-1][0], max(result[-1][1], end))
        else:
            result.append((start, end))
    return result

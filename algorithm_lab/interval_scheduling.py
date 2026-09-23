"""Select the most nonoverlapping half-open [start, end) integer intervals.

Intervals must have positive duration. Earliest finishing intervals are chosen;
ties prefer earlier starts, then original order. Time O(n log n), space O(n).
This maximizes the number of activities, not their total duration or value.

>>> interval_scheduling([(0, 6), (1, 3), (3, 5), (5, 7)])
[(1, 3), (3, 5), (5, 7)]
"""

from collections.abc import Iterable


def interval_scheduling(intervals: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    rows = []
    for start, end in intervals:
        if any(isinstance(x, bool) or not isinstance(x, int) for x in (start, end)) or start >= end:
            raise ValueError("activities require integer start < end")
        rows.append((start, end))
    result = []
    for row in sorted(rows, key=lambda pair: (pair[1], pair[0])):
        if not result or row[0] >= result[-1][1]:
            result.append(row)
    return result

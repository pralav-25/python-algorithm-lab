"""Sort signed integers in O(n + r) time and O(n + r) space, r = max-min+1.

A configurable max_range prevents allocating a huge counter array for sparse
values. Booleans and non-integers are rejected. The input is not modified.

>>> counting_sort([3, -2, 0, -2])
[-2, -2, 0, 3]
"""

from collections.abc import Iterable


def counting_sort(values: Iterable[int], *, max_range: int = 1_000_000) -> list[int]:
    if isinstance(max_range, bool) or not isinstance(max_range, int) or max_range < 1:
        raise ValueError("max_range must be a positive integer")
    data = list(values)
    if any(isinstance(value, bool) or not isinstance(value, int) for value in data):
        raise ValueError("values must be integers")
    if not data:
        return []
    low, high = min(data), max(data)
    if high - low + 1 > max_range:
        raise ValueError("value range exceeds max_range")
    counts = [0] * (high - low + 1)
    for value in data:
        counts[value - low] += 1
    return [offset + low for offset, count in enumerate(counts) for _ in range(count)]

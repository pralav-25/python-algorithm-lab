"""Select the kth smallest value without changing the caller's sequence.

Duplicates count separately. k must be an integer in [0, len(values)). Three-way
partitioning takes O(n) expected time on random data, O(n²) worst case, and O(n)
extra space. The median-of-three pivot is deterministic.

>>> quickselect([9, 2, 5, 2], 2)
5
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def quickselect(values: Sequence[T], k: int) -> T:
    if isinstance(k, bool) or not isinstance(k, int) or not 0 <= k < len(values):
        raise ValueError("k must be a valid zero-based index")
    data = list(values)
    while True:
        pivot = sorted((data[0], data[len(data) // 2], data[-1]))[1]
        lower = [value for value in data if value < pivot]
        upper = [value for value in data if value > pivot]
        equal_count = len(data) - len(lower) - len(upper)
        if k < len(lower):
            data = lower
        elif k < len(lower) + equal_count:
            return pivot
        else:
            k -= len(lower) + equal_count
            data = upper

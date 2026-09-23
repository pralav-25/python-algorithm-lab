"""Find a pair in O(n) time and space; return None when no pair exists.

Scan left to right: choose the earliest second index, then the earliest first
index. The same element cannot be used twice. Inputs are integers.

>>> two_sum([3, 3, 5], 6)
(0, 1)
"""

from collections.abc import Iterable


def two_sum(values: Iterable[int], target: int) -> tuple[int, int] | None:
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen.setdefault(value, index)
    return None

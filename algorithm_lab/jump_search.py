"""Find the first match in ascending sorted data with square-root jumps.

Accepts a random-access sequence whose values and target share a total order.
Sortedness is assumed without scanning. Absent targets return -1, including in
empty sequences. No mutation occurs. Time: O(sqrt(n)); auxiliary space: O(1).

>>> jump_search([1, 3, 3, 7], 3)
1
>>> jump_search([1, 3], 2)
-1
"""

from collections.abc import Sequence
from math import isqrt
from typing import TypeVar

T = TypeVar("T")


def jump_search(values: Sequence[T], target: T) -> int:
    size = len(values)
    if not size:
        return -1
    step = max(1, isqrt(size))
    left, right = 0, min(step, size)
    while values[right - 1] < target:
        left = right
        if left == size:
            return -1
        right = min(right + step, size)
    for i in range(left, right):
        if values[i] == target:
            return i
        if target < values[i]:
            break
    return -1

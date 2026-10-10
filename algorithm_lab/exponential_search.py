"""Find the first match in a sorted sequence by exponential bracketing.

Values and target must share a consistent total order. Ascending sortedness is
an unvalidated precondition. Return -1 when absent. No mutation occurs. Time is
O(log(i + 2)) for a match at index i, O(log(n + 1)) otherwise; space is O(1).

>>> exponential_search([1, 3, 3, 9], 3)
1
>>> exponential_search([], 3)
-1
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def exponential_search(values: Sequence[T], target: T) -> int:
    if not values:
        return -1
    bound = 1
    while bound < len(values) and values[bound] < target:
        bound *= 2
    left, right = bound // 2, min(bound + 1, len(values))
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left if left < len(values) and values[left] == target else -1

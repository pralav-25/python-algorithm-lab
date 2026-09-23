"""Find the first occurrence in ascending sorted data in O(log n) time, O(1) space.

The input must already be sorted; it is not scanned or modified. Missing values
return -1, including on empty inputs.

>>> binary_search([1, 3, 3, 8], 3)
1
>>> binary_search([], 3)
-1
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def binary_search(values: Sequence[T], target: T) -> int:
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left if left < len(values) and values[left] == target else -1

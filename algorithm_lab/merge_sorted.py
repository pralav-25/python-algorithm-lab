"""Merge two ascending iterables into a new list, retaining duplicates.

Both inputs must already be sorted by the same total order, optionally supplied
through key. Sortedness is not validated. The key is evaluated once per item.
Ties keep order within each input and put first-input items before second-input
items. No mutation occurs. Time: O(n + m); auxiliary space including output: O(n + m).

>>> merge_sorted([1, 3, 3], [2, 3, 5])
[1, 2, 3, 3, 3, 5]
>>> merge_sorted([], [])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def merge_sorted(
    first: Iterable[T], second: Iterable[T], *, key: Callable[[T], Any] | None = None
) -> list[T]:
    left = [(key(value) if key is not None else value, value) for value in first]
    right = [(key(value) if key is not None else value, value) for value in second]
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if right[j][0] < left[i][0]:
            result.append(right[j][1])
            j += 1
        else:
            result.append(left[i][1])
            i += 1
    result.extend(value for _, value in left[i:])
    result.extend(value for _, value in right[j:])
    return result

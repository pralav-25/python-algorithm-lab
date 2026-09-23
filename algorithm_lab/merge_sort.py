"""Stable merge sort returning a new list in O(n log n) time and O(n) space.

The optional key is evaluated once per value; ties keep their original order.
Values or keys must define a consistent total order.

>>> merge_sort([('b', 1), ('a', 2), ('b', 3)], key=lambda row: row[0])
[('a', 2), ('b', 1), ('b', 3)]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def merge_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key else value, value) for value in values]

    def sort(rows):
        if len(rows) < 2:
            return rows
        middle = len(rows) // 2
        left, right = sort(rows[:middle]), sort(rows[middle:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if right[j][0] < left[i][0]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
        return merged + left[i:] + right[j:]

    return [value for _, value in sort(data)]

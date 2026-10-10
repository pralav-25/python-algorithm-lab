"""Insertion sort returning a new ascending list.

Accepts any iterable of values with a consistent total order, or a key function
whose results have that order. The key is evaluated once per value. Equal keys preserve input order.
The input is never modified. Time: O(n²) worst-case and O(n) best-case; auxiliary space: O(n).

>>> insertion_sort([4, -2, 4, 1])
[-2, 1, 4, 4]
>>> insertion_sort([])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def insertion_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key is not None else value, value) for value in values]

    for i in range(1, len(data)):
        row = data[i]
        j = i
        while j and row[0] < data[j - 1][0]:
            data[j] = data[j - 1]
            j -= 1
        data[j] = row

    return [value for _, value in data]

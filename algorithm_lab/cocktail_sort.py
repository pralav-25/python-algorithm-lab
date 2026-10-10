"""Cocktail sort returning a new ascending list.

Accepts any iterable of values with a consistent total order, or a key function
whose results have that order. The key is evaluated once per value. Equal keys preserve input order.
The input is never modified. Time: O(n²) worst-case and O(n) best-case; auxiliary space: O(n).

>>> cocktail_sort([4, -2, 4, 1])
[-2, 1, 4, 4]
>>> cocktail_sort([])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def cocktail_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key is not None else value, value) for value in values]

    left, right = 0, len(data) - 1
    while left < right:
        swapped = False
        for i in range(left, right):
            if data[i + 1][0] < data[i][0]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break
        right -= 1
        swapped = False
        for i in range(right, left, -1):
            if data[i][0] < data[i - 1][0]:
                data[i], data[i - 1] = data[i - 1], data[i]
                swapped = True
        left += 1
        if not swapped:
            break

    return [value for _, value in data]

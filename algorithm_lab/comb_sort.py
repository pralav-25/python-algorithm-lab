"""Comb sort returning a new ascending list.

Accepts any iterable of values with a consistent total order, or a key function
whose results have that order. The key is evaluated once per value. Equal-key order is unspecified.
The input is never modified. Time: O(n²) worst-case; auxiliary space: O(n).

>>> comb_sort([4, -2, 4, 1])
[-2, 1, 4, 4]
>>> comb_sort([])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def comb_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key is not None else value, value) for value in values]

    gap = len(data)
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, gap * 10 // 13)
        swapped = False
        for i in range(len(data) - gap):
            if data[i + gap][0] < data[i][0]:
                data[i], data[i + gap] = data[i + gap], data[i]
                swapped = True

    return [value for _, value in data]

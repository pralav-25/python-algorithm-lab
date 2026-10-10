"""Pancake sort returning a new ascending list.

Accepts any iterable of values with a consistent total order, or a key function
whose results have that order. The key is evaluated once per value. Equal-key order is unspecified.
The input is never modified. Time: O(n²); auxiliary space: O(n).

>>> pancake_sort([4, -2, 4, 1])
[-2, 1, 4, 4]
>>> pancake_sort([])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def pancake_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key is not None else value, value) for value in values]

    for end in range(len(data) - 1, 0, -1):
        largest = 0
        for i in range(1, end + 1):
            if data[largest][0] < data[i][0]:
                largest = i
        if largest == end:
            continue
        if largest:
            data[: largest + 1] = reversed(data[: largest + 1])
        data[: end + 1] = reversed(data[: end + 1])

    return [value for _, value in data]

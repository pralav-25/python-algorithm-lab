"""Gnome sort returning a new ascending list.

Accepts any iterable of values with a consistent total order, or a key function
whose results have that order. The key is evaluated once per value. Equal keys preserve input order.
The input is never modified. Time: O(n²) worst-case and O(n) best-case; auxiliary space: O(n).

>>> gnome_sort([4, -2, 4, 1])
[-2, 1, 4, 4]
>>> gnome_sort([])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def gnome_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key is not None else value, value) for value in values]

    i = 1
    while i < len(data):
        if i == 0 or not data[i][0] < data[i - 1][0]:
            i += 1
        else:
            data[i], data[i - 1] = data[i - 1], data[i]
            i -= 1

    return [value for _, value in data]

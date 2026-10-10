"""Shell sort returning a new ascending list.

Accepts any iterable of values with a consistent total order, or a key function
whose results have that order. The key is evaluated once per value. Equal-key order is unspecified.
The input is never modified. Time: O(n²) worst-case; auxiliary space: O(n).

>>> shell_sort([4, -2, 4, 1])
[-2, 1, 4, 4]
>>> shell_sort([])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def shell_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key is not None else value, value) for value in values]

    gap = len(data) // 2
    while gap:
        for i in range(gap, len(data)):
            row = data[i]
            j = i
            while j >= gap and row[0] < data[j - gap][0]:
                data[j] = data[j - gap]
                j -= gap
            data[j] = row
        gap //= 2

    return [value for _, value in data]

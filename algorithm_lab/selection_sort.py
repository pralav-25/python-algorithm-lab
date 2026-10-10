"""Selection sort returning a new ascending list.

Accepts any iterable of values with a consistent total order, or a key function
whose results have that order. The key is evaluated once per value. Equal-key order is unspecified.
The input is never modified. Time: O(n²); auxiliary space: O(n).

>>> selection_sort([4, -2, 4, 1])
[-2, 1, 4, 4]
>>> selection_sort([])
[]
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")


def selection_sort(values: Iterable[T], *, key: Callable[[T], Any] | None = None) -> list[T]:
    data = [(key(value) if key is not None else value, value) for value in values]

    for i in range(len(data)):
        least = i
        for j in range(i + 1, len(data)):
            if data[j][0] < data[least][0]:
                least = j
        data[i], data[least] = data[least], data[i]

    return [value for _, value in data]

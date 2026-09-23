"""Return an ascending list using heap sort, without modifying the input.

Time is O(n log n). Sorting the copied list uses O(1) auxiliary space, in addition
to the O(n) output copy. This algorithm is not stable for equal keys.

>>> heap_sort([5, 1, 5, -2])
[-2, 1, 5, 5]
"""

from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def heap_sort(values: Iterable[T]) -> list[T]:
    data = list(values)

    def sift(root: int, end: int) -> None:
        while 2 * root + 1 < end:
            child = 2 * root + 1
            if child + 1 < end and data[child] < data[child + 1]:
                child += 1
            if not data[root] < data[child]:
                return
            data[root], data[child] = data[child], data[root]
            root = child

    for root in range(len(data) // 2 - 1, -1, -1):
        sift(root, len(data))
    for end in range(len(data) - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift(0, end)
    return data

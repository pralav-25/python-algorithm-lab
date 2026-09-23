"""Reconstruct a longest strictly increasing subsequence in O(n log n) time.

Space is O(n); equal values do not extend a subsequence. The deterministic result
is not guaranteed to be lexicographically smallest. Values must be totally ordered.

>>> longest_increasing_subsequence([3, 1, 2, 2, 4])
[1, 2, 4]
"""

from bisect import bisect_left
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def longest_increasing_subsequence(values: Sequence[T]) -> list[T]:
    tails, positions = [], []
    previous = [-1] * len(values)
    for index, value in enumerate(values):
        place = bisect_left(tails, value)
        if place < len(tails) and tails[place] == value:
            continue
        previous[index] = positions[place - 1] if place else -1
        if place == len(tails):
            tails.append(value)
            positions.append(index)
        else:
            tails[place], positions[place] = value, index
    result = []
    cursor = positions[-1] if positions else -1
    while cursor != -1:
        result.append(values[cursor])
        cursor = previous[cursor]
    return result[::-1]

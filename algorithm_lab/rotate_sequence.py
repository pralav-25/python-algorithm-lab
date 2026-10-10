"""Return a new list rotated right by an integer number of steps.

Accepts any iterable. steps must be an integer excluding bool; negative steps
rotate left. Full turns preserve the order, including duplicates. Empty input
returns an empty list. No input mutation occurs. Time and auxiliary space: O(n).

>>> rotate_sequence([1, 2, 3, 4], 1)
[4, 1, 2, 3]
>>> rotate_sequence([1, 2, 3], -1)
[2, 3, 1]
"""

from collections.abc import Iterable
from typing import TypeVar

from algorithm_lab._validation import integer

T = TypeVar("T")


def rotate_sequence(values: Iterable[T], steps: int) -> list[T]:
    integer(steps, "steps")
    data = list(values)
    if not data:
        return []
    steps %= len(data)
    return data[-steps:] + data[:-steps] if steps else data

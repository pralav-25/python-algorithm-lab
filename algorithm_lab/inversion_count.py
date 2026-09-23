"""Count pairs i < j with values[i] > values[j] in O(n log n) time, O(n) space.

Equal values are not inversions. Values must be totally ordered; the input is
not modified. An empty or already sorted sequence has zero inversions.

>>> inversion_count([3, 1, 2, 1])
4
"""

from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def inversion_count(values: Iterable[T]) -> int:
    def count(data):
        if len(data) < 2:
            return data, 0
        middle = len(data) // 2
        left, first = count(data[:middle])
        right, second = count(data[middle:])
        total, i, j, merged = first + second, 0, 0, []
        while i < len(left) and j < len(right):
            if right[j] < left[i]:
                total += len(left) - i
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
        return merged + left[i:] + right[j:], total

    return count(list(values))[1]

"""Prefix sums over integers: O(n) construction and space, O(1) range queries.

Queries use half-open [start, stop) bounds; negative indices are not accepted.
The input is copied into immutable cumulative totals.

>>> totals = PrefixSum([2, -1, 5])
>>> totals.sum(1, 3)
4
>>> totals.sum(2, 2)
0
"""

from collections.abc import Iterable


class PrefixSum:
    def __init__(self, values: Iterable[int]):
        totals = [0]
        for value in values:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("values must be integers")
            totals.append(totals[-1] + value)
        self._totals = tuple(totals)

    def __len__(self) -> int:
        return len(self._totals) - 1

    def sum(self, start: int, stop: int) -> int:
        if any(isinstance(i, bool) or not isinstance(i, int) for i in (start, stop)):
            raise ValueError("bounds must be integers")
        if not 0 <= start <= stop <= len(self):
            raise ValueError("bounds must satisfy 0 <= start <= stop <= length")
        return self._totals[stop] - self._totals[start]

"""Integer stream medians with O(log n) insertion, O(1) query and O(n) space.

median returns a Fraction, preserving arbitrary-size integer precision.
Empty queries raise ValueError. Booleans and non-integers are rejected.

>>> stream = MedianStream()
>>> for value in [4, 1, 9, 2]: stream.add(value)
>>> stream.median()
Fraction(3, 1)
"""

import heapq
from fractions import Fraction

from algorithm_lab._validation import integer


class MedianStream:
    def __init__(self):
        self._lower, self._upper = [], []

    def __len__(self):
        return len(self._lower) + len(self._upper)

    def add(self, value):
        integer(value)
        heapq.heappush(self._lower, -value)
        heapq.heappush(self._upper, -heapq.heappop(self._lower))
        if len(self._upper) > len(self._lower):
            heapq.heappush(self._lower, -heapq.heappop(self._upper))

    def median(self):
        if not self._lower:
            raise ValueError("median of an empty stream")
        if len(self._lower) > len(self._upper):
            return Fraction(-self._lower[0])
        return Fraction(self._upper[0] - self._lower[0], 2)

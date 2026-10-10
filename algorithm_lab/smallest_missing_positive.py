"""Return the smallest positive integer absent from the supplied values.

Accepts an iterable of signed integers excluding bool. Duplicates and nonpositive
values do not affect the result. Empty input returns 1. A cyclic-placement copy
keeps the input unchanged. Time: O(n); auxiliary space: O(n).

>>> smallest_missing_positive([3, 4, -1, 1])
2
>>> smallest_missing_positive([])
1
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def smallest_missing_positive(values: Iterable[int]) -> int:
    data = [integer(value) for value in values]
    for i in range(len(data)):
        while 1 <= data[i] <= len(data) and data[data[i] - 1] != data[i]:
            destination = data[i] - 1
            data[i], data[destination] = data[destination], data[i]
    for i, value in enumerate(data, 1):
        if value != i:
            return i
    return len(data) + 1

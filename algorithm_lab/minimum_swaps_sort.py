"""Return the minimum number of arbitrary pair swaps to sort distinct integers.

Accepts an iterable of signed integers excluding bool. Duplicate values raise
ValueError because the permutation-cycle contract requires distinct values.
Empty or already-sorted input gives zero. No mutation occurs. Time: O(n log n);
auxiliary space: O(n). Every cycle of length k contributes k - 1 swaps.

>>> minimum_swaps_sort([4, 3, 2, 1])
2
>>> minimum_swaps_sort([])
0
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def minimum_swaps_sort(values: Iterable[int]) -> int:
    data = [integer(value) for value in values]
    if len(set(data)) != len(data):
        raise ValueError("values must be distinct")
    destinations = {value: i for i, value in enumerate(sorted(data))}
    seen = [False] * len(data)
    swaps = 0
    for start in range(len(data)):
        length = 0
        i = start
        while not seen[i]:
            seen[i] = True
            length += 1
            i = destinations[data[i]]
        if length:
            swaps += length - 1
    return swaps

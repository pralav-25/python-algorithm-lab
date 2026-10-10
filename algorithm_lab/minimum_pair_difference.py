"""Return the minimum absolute difference between two distinct input positions.

Accepts an iterable of signed integers excluding bool. Duplicate values give
zero; fewer than two values return None. Only the difference is returned, so
ties need no pair selection. Input is unchanged. Time: O(n log n); space: O(n).

>>> minimum_pair_difference([8, -3, 4, 10])
2
>>> minimum_pair_difference([7]) is None
True
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def minimum_pair_difference(values: Iterable[int]) -> int | None:
    data = sorted(integer(value) for value in values)
    return min((b - a for a, b in zip(data, data[1:], strict=False)), default=None)

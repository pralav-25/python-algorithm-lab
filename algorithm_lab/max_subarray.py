"""Return (sum, start, stop) for the best nonempty integer slice.

Ties prefer the earliest start, then earliest stop. Empty or non-integer inputs
raise ValueError. Time O(n), auxiliary space O(1); indices use Python slice rules.

>>> max_subarray([-2, 3, -1, 4, -8])
(6, 1, 4)
"""

from collections.abc import Sequence


def max_subarray(values: Sequence[int]) -> tuple[int, int, int]:
    if not values or any(isinstance(x, bool) or not isinstance(x, int) for x in values):
        raise ValueError("provide a nonempty sequence of integers")
    best = running = values[0]
    best_start = start = 0
    best_stop = 1
    for index in range(1, len(values)):
        if running < 0:
            running, start = values[index], index
        else:
            running += values[index]
        if running > best:
            best, best_start, best_stop = running, start, index + 1
    return best, best_start, best_stop

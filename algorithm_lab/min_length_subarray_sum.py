"""Return half-open indices of the shortest subarray with sum at least target.

Accepts a sequence of nonnegative integers and a positive integer target,
excluding bool. Equal-length ties choose the earliest start. Return None when
no subarray qualifies, including empty input. Nonnegative values permit a
sliding window. The input is not changed. Time: O(n); auxiliary space: O(1).

>>> min_length_subarray_sum([2, 3, 1, 2, 4, 3], 7)
(4, 6)
>>> min_length_subarray_sum([1, 2], 4) is None
True
"""

from collections.abc import Sequence

from algorithm_lab._validation import integer


def min_length_subarray_sum(values: Sequence[int], target: int) -> tuple[int, int] | None:
    integer(target, "target", minimum=1)
    for value in values:
        integer(value, minimum=0)
    left = total = 0
    best = None
    for right, value in enumerate(values, 1):
        total += value
        while total >= target:
            if best is None or right - left < best[1] - best[0]:
                best = (left, right)
            total -= values[left]
            left += 1
    return best

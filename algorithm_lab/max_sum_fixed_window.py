"""Return (maximum_sum, start_index) among all windows of the requested size.

Accepts a sequence of signed integers excluding bool. size must be an integer
excluding bool in [1, len(values)]; invalid sizes raise ValueError. Ties choose
the smallest start index. The input is unchanged. Time: O(n); space: O(1).

>>> max_sum_fixed_window([2, -1, 4, -2, 3], 2)
(3, 1)
>>> max_sum_fixed_window([-3, -1, -2], 2)
(-3, 1)
"""

from collections.abc import Sequence

from algorithm_lab._validation import integer


def max_sum_fixed_window(values: Sequence[int], size: int) -> tuple[int, int]:
    integer(size, "size", minimum=1)
    if size > len(values):
        raise ValueError("size exceeds sequence length")
    for value in values:
        integer(value)
    total = sum(values[i] for i in range(size))
    best = (total, 0)
    for end in range(size, len(values)):
        total += values[end] - values[end - size]
        if total > best[0]:
            best = (total, end - size + 1)
    return best

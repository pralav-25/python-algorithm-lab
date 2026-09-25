"""Maximum nonempty circular slice sum.

Accept nonempty integer values excluding bool. Each index may be used at
most once. Return the maximum sum over all nonempty circular slices.
All-negative inputs return their greatest element. O(n) time and O(n) copied
input storage; the Kadane recurrence itself uses O(1) integers.

>>> circular_max_subarray([5, -3, 5])
10
"""

from algorithm_lab._validation import integer


def circular_max_subarray(values):
    values = list(values)
    if not values:
        raise ValueError("input must be nonempty")
    for value in values:
        integer(value)
    high = low = best = worst = total = values[0]
    for value in values[1:]:
        high, low = max(value, high + value), min(value, low + value)
        best, worst, total = max(best, high), min(worst, low), total + value
    return best if best < 0 else max(best, total - worst)

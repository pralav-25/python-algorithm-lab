"""Return (start, stop) for the longest nonempty integer slice summing to target.

Ties use earliest start; None means no matching nonempty slice. O(n) expected
time and O(n) space. Negative integers are supported; booleans are rejected.

>>> longest_subarray_sum([1, -1, 2, -2, 3], 0)
(0, 4)
"""

from algorithm_lab._validation import integer


def longest_subarray_sum(values, target):
    integer(target, "target")
    first, total, best = {0: 0}, 0, None
    for stop, value in enumerate(values, 1):
        total += integer(value)
        if total - target in first:
            start = first[total - target]
            if best is None or stop - start > best[1] - best[0]:
                best = start, stop
        first.setdefault(total, stop)
    return best

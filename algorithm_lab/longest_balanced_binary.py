"""Return half-open indices of the longest subarray with equal zeros and ones.

Accepts an iterable containing only integer 0 and 1, excluding bool. Invalid
values raise ValueError. Equal-length ties choose the smallest start index;
if there is no nonempty balanced subarray return (0, 0). The input is unchanged.
Expected time: O(n); auxiliary space: O(n).

>>> longest_balanced_binary([0, 1, 0])
(0, 2)
>>> longest_balanced_binary([1, 1])
(0, 0)
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def longest_balanced_binary(values: Iterable[int]) -> tuple[int, int]:
    first = {0: 0}
    balance = 0
    best = (0, 0)
    for end, value in enumerate(values, 1):
        integer(value)
        if value not in (0, 1):
            raise ValueError("values must be zero or one")
        balance += 1 if value else -1
        if balance in first:
            start = first[balance]
            if end - start > best[1] - best[0]:
                best = (start, end)
        else:
            first[balance] = end
    return best

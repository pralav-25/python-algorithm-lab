"""Return the length of the longest consecutive run in an integer iterable.

Accepts signed integers excluding bool. Duplicate values do not extend a run;
empty input returns zero. Ties share the same length. The input is never
modified. Expected time: O(n); auxiliary space: O(n), using a hash set.

>>> longest_consecutive([100, 4, 200, 1, 3, 2, 2])
4
>>> longest_consecutive([])
0
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def longest_consecutive(values: Iterable[int]) -> int:
    unique = {integer(value) for value in values}
    longest = 0
    for start in unique:
        if start - 1 not in unique:
            end = start
            while end + 1 in unique:
                end += 1
            longest = max(longest, end - start + 1)
    return longest

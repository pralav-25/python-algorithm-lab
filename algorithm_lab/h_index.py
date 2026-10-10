"""Return the largest h with at least h citation counts greater than or equal to h.

Accepts an iterable of nonnegative integers excluding bool; invalid counts
raise ValueError. Duplicates are separate papers. Empty input gives zero and
the input is not mutated. Time: O(n); auxiliary space: O(n).

>>> h_index([3, 0, 6, 1, 5])
3
>>> h_index([])
0
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def h_index(citations: Iterable[int]) -> int:
    data = [integer(value, "citation", minimum=0) for value in citations]
    counts = [0] * (len(data) + 1)
    for value in data:
        counts[min(value, len(data))] += 1
    papers = 0
    for h in range(len(data), -1, -1):
        papers += counts[h]
        if papers >= h:
            return h
    return 0

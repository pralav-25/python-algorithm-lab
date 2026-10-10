"""Count unordered integer partitions of n into positive parts.

n is a nonnegative integer excluding bool. Return an exact integer; the empty
partition makes p(0)=1. There are no ties. Coin-style dynamic programming uses
O(n**2) arithmetic steps and O(n) integer storage.

>>> partition_count(7)
15
"""

from algorithm_lab._validation import integer


def partition_count(n):
    integer(n, "n", minimum=0)
    counts = [1] + [0] * n
    for part in range(1, n + 1):
        for total in range(part, n + 1):
            counts[total] += counts[total - part]
    return counts[n]

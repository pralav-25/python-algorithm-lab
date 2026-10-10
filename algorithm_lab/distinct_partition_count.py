"""Count unordered partitions of n with distinct positive parts.

n is a nonnegative integer excluding bool. Return an exact integer; the empty
partition contributes 1 at n=0. There are no ties. Descending dynamic-programming
updates use O(n**2) arithmetic steps and O(n) integer storage.

>>> distinct_partition_count(7)
5
"""

from algorithm_lab._validation import integer


def distinct_partition_count(n):
    integer(n, "n", minimum=0)
    counts = [1] + [0] * n
    for part in range(1, n + 1):
        for total in range(n, part - 1, -1):
            counts[total] += counts[total - part]
    return counts[n]

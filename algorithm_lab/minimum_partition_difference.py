"""Minimize the absolute difference between sums of two complementary subsets.

Values are an iterable of nonnegative integers; bool is rejected. Every input
occurrence belongs to exactly one subset, and empty subsets are allowed. Return
the minimum integer difference, zero for empty input; tied subsets need no
selection. A bitset gives O(n*(S+1)) bit-operation time and O(S + n) space, where S
is the total sum. Inputs are copied, never changed.

>>> minimum_partition_difference([1, 6, 11, 5])
1
"""

from algorithm_lab._validation import integer


def minimum_partition_difference(values) -> int:
    values = list(values)
    for value in values:
        integer(value, "value", minimum=0)
    total = sum(values)
    limit = total // 2
    reachable = 1
    mask = (1 << (limit + 1)) - 1
    for value in values:
        if value <= limit:
            reachable |= (reachable << value) & mask
    closest = reachable.bit_length() - 1
    return total - 2 * closest

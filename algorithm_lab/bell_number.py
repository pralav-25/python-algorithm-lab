"""Count set partitions of n labeled objects.

n is a nonnegative integer excluding bool. Return the exact Bell number,
including B(0)=1. There are no ties. Bell's triangle takes O(n**2) arithmetic
steps and O(n) integer storage; arbitrary-precision integer costs are additional.

>>> bell_number(5)
52
"""

from algorithm_lab._validation import integer


def bell_number(n):
    integer(n, "n", minimum=0)
    row = [1]
    for _ in range(n):
        following = [row[-1]]
        for value in row:
            following.append(following[-1] + value)
        row = following
    return row[0]

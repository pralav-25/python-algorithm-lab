"""Yield tuples of positive integers summing to total, in reverse lexicographic order.

Zero has one partition: (). total must be a nonnegative integer. For p(n)
partitions, O(n*p(n)) time including output copying; O(n) working space.
Recursive generator depth can reach total, so large totals can hit Python's
recursion limit. This is intended for small enumeration problems.

>>> list(integer_partitions(4))
[(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
"""

from algorithm_lab._validation import integer


def integer_partitions(total):
    integer(total, "total", minimum=0)
    path = []

    def generate(remaining, maximum):
        if remaining == 0:
            yield tuple(path)
            return
        for part in range(min(remaining, maximum), 0, -1):
            path.append(part)
            yield from generate(remaining - part, part)
            path.pop()

    return generate(total, total)

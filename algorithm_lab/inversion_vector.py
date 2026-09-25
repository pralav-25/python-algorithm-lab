"""Count smaller successors for every position with a Fenwick tree.

Input contains integers excluding bool. Return result[i] as the number of
strictly smaller values to the right of i; equal values do not count.
Coordinate compression and a Fenwick tree take O(n log n) time and O(n)
space. The input remains unchanged.

>>> inversion_vector([5, 2, 6, 1])
[2, 1, 1, 0]
"""

from algorithm_lab._validation import integer


def inversion_vector(values):
    values = list(values)
    for value in values:
        integer(value)
    ranks = {value: i + 1 for i, value in enumerate(sorted(set(values)))}
    tree, result = [0] * (len(ranks) + 1), [0] * len(values)
    for i in range(len(values) - 1, -1, -1):
        index = ranks[values[i]] - 1
        while index:
            result[i] += tree[index]
            index -= index & -index
        index = ranks[values[i]]
        while index < len(tree):
            tree[index] += 1
            index += index & -index
    return result

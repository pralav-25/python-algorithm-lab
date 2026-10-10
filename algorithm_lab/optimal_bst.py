"""Minimize weighted successful-search comparisons in an ordered BST.

Frequencies are an iterable of nonnegative integers in sorted key order; bool is
rejected. Unsuccessful searches have no cost in this model. A root comparison
has depth one. Return the minimum sum of frequency*depth, or zero for no keys.
Tied trees need no selection. O(n cubed) time and O(n squared) space excluding
integer arithmetic. Inputs are copied, never changed.

>>> optimal_bst([34, 8, 50])
142
"""

from algorithm_lab._validation import integer


def optimal_bst(frequencies) -> int:
    frequencies = list(frequencies)
    for frequency in frequencies:
        integer(frequency, "frequency", minimum=0)
    size = len(frequencies)
    prefix = [0]
    for frequency in frequencies:
        prefix.append(prefix[-1] + frequency)
    costs = [[0] * (size + 1) for _ in range(size + 1)]
    for width in range(1, size + 1):
        for start in range(size - width + 1):
            stop = start + width
            costs[start][stop] = (
                prefix[stop]
                - prefix[start]
                + min(costs[start][root] + costs[root + 1][stop] for root in range(start, stop))
            )
    return costs[0][size]

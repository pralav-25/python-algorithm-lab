"""Generate distinct integer permutations in lexicographic order.

Accept an iterable of integers excluding bool. Yield tuples in sorted order
without repeating permutations of equal elements. Empty input yields ().
Successor generation avoids recursion and uses O(n) working space and O(n)
time per output after O(n log n) sorting; input is not modified.

>>> list(multiset_permutations([2, 1, 1]))
[(1, 1, 2), (1, 2, 1), (2, 1, 1)]
"""

from algorithm_lab._validation import integer


def multiset_permutations(values):
    values = list(values)
    for value in values:
        integer(value)
    values.sort()
    while True:
        yield tuple(values)
        i = len(values) - 2
        while i >= 0 and values[i] >= values[i + 1]:
            i -= 1
        if i < 0:
            return
        j = len(values) - 1
        while values[j] <= values[i]:
            j -= 1
        values[i], values[j] = values[j], values[i]
        values[i + 1 :] = reversed(values[i + 1 :])

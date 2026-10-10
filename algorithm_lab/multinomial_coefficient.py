"""Count words containing specified multiplicities of distinct symbols.

counts is an iterable of nonnegative integers excluding bool. Return
sum(counts)!/product(count!), with the empty iterable returning 1. The input is
not changed and there are no ties. Factorials use O(sum(counts)+len(counts))
arithmetic steps and O(len(counts)) integer storage, excluding big-integer costs.

>>> multinomial_coefficient([2, 1, 2])
30
"""

from math import factorial

from algorithm_lab._validation import integer


def multinomial_coefficient(counts):
    values = list(counts)
    denominator = 1
    for count in values:
        integer(count, "count", minimum=0)
        denominator *= factorial(count)
    return factorial(sum(values)) // denominator

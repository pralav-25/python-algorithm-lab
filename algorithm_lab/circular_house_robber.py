"""Choose nonadjacent houses on a circle to maximize their total value.

Values are a nonnegative integer iterable; bool is rejected. First and last
houses are neighbors when there are at least two houses. A single house may
be taken. Return only the maximum integer total, zero for empty input; tied
selections need no selection. O(n) time and space, excluding integer arithmetic.
Input values are copied and never mutated.

>>> circular_house_robber([2, 3, 2])
3
"""

from algorithm_lab._validation import integer


def circular_house_robber(values) -> int:
    values = list(values)
    for value in values:
        integer(value, "house value", minimum=0)
    if len(values) < 2:
        return sum(values)

    def linear(start, stop):
        previous, current = 0, 0
        for index in range(start, stop):
            previous, current = current, max(current, previous + values[index])
        return current

    return max(linear(0, len(values) - 1), linear(1, len(values)))

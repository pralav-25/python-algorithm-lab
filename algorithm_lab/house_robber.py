"""Choose nonadjacent houses on a line to maximize their total value.

Values are an iterable of nonnegative integers; bool is rejected. Taking no
houses is allowed. Return the maximum integer total, or zero for empty input;
tied selections need no selection. O(n) time, O(1) auxiliary space excluding
integer arithmetic. Input iterables are consumed without mutation.

>>> house_robber([2, 7, 9, 3, 1])
12
"""

from algorithm_lab._validation import integer


def house_robber(values) -> int:
    previous, current = 0, 0
    for value in values:
        integer(value, "house value", minimum=0)
        previous, current = current, max(current, previous + value)
    return current

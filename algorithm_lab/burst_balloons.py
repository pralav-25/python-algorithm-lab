"""Maximize coins earned by bursting balloons in any order.

Input is an iterable of nonnegative integers; bool is rejected. Bursting a
balloon earns its value times its current left and right neighbors, with virtual
value-one balloons at both ends. Return the maximum integer total, or zero for
empty input; tied orders need no selection. O(n cubed) time and O(n squared)
space excluding integer arithmetic. Inputs are copied, never mutated.

>>> burst_balloons([3, 1, 5, 8])
167
"""

from algorithm_lab._validation import integer


def burst_balloons(balloons) -> int:
    values = list(balloons)
    for value in values:
        integer(value, "balloon", minimum=0)
    values = [1, *values, 1]
    size = len(values)
    scores = [[0] * size for _ in range(size)]
    for width in range(2, size):
        for left in range(size - width):
            right = left + width
            scores[left][right] = max(
                scores[left][last]
                + scores[last][right]
                + values[left] * values[last] * values[right]
                for last in range(left + 1, right)
            )
    return scores[0][-1]

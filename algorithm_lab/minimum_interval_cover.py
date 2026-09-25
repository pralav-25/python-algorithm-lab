"""Greedy minimum-cardinality coverage of a closed target interval.

Input intervals and target endpoints are integers, excluding bool, with
start < stop. Return original indices of a minimum cover or None for a gap.
Touching endpoints cover continuously. Greedy ties prefer the lowest input
index among equal farthest endpoints. O(n log n) time and O(n) space.

>>> minimum_interval_cover([(0, 2), (1, 4), (3, 5)], 0, 5)
[0, 1, 2]
"""

from algorithm_lab._validation import integer


def minimum_interval_cover(intervals, start, stop):
    integer(start, "start")
    integer(stop, "stop")
    if start >= stop:
        raise ValueError("target must have positive length")
    ordered = []
    for i, (left, right) in enumerate(intervals):
        integer(left, "left")
        integer(right, "right")
        if left >= right:
            raise ValueError("intervals must have positive length")
        ordered.append((left, right, i))
    ordered.sort()
    cursor, current, result = 0, start, []
    while current < stop:
        farthest, index = current, None
        while cursor < len(ordered) and ordered[cursor][0] <= current:
            _, right, i = ordered[cursor]
            if right > farthest or (right == farthest and index is not None and i < index):
                farthest, index = right, i
            cursor += 1
        if index is None:
            return None
        result.append(index)
        current = farthest
    return result

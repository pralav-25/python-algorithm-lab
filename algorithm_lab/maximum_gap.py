"""Return the largest adjacent gap in the sorted order of signed integers.

Accepts an iterable of integers excluding bool. Fewer than two values or all
equal values return zero. The input is not modified. Bucket bounds give O(n)
time and O(n) auxiliary space under unit-cost integer arithmetic.

>>> maximum_gap([3, 6, 9, 1])
3
>>> maximum_gap([-10, 4, 4])
14
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def maximum_gap(values: Iterable[int]) -> int:
    data = [integer(value) for value in values]
    if len(data) < 2:
        return 0
    low, high = min(data), max(data)
    if low == high:
        return 0
    width = (high - low + len(data) - 2) // (len(data) - 1)
    size = (high - low) // width + 1
    minima: list[int | None] = [None] * size
    maxima: list[int | None] = [None] * size
    for value in data:
        bucket = (value - low) // width
        if minima[bucket] is None or value < minima[bucket]:
            minima[bucket] = value
        if maxima[bucket] is None or value > maxima[bucket]:
            maxima[bucket] = value
    answer = 0
    previous = low
    for minimum, maximum in zip(minima, maxima, strict=True):
        if minimum is not None:
            answer = max(answer, minimum - previous)
            previous = maximum
    return answer

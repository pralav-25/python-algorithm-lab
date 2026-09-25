"""Sweep-line maximum overlap for half-open integer intervals.

Intervals satisfy start < stop with integer endpoints excluding bool. Return
(maximum_count, earliest_coordinate), or (0, None) for no intervals. Ending
intervals do not overlap intervals beginning at the same coordinate.
O(n log n) time and O(n) space.

>>> interval_overlap_peak([(0, 3), (2, 4), (3, 5)])
(2, 2)
"""

from algorithm_lab._validation import integer


def interval_overlap_peak(intervals):
    events = {}
    for start, stop in intervals:
        integer(start, "start")
        integer(stop, "stop")
        if start >= stop:
            raise ValueError("intervals must have positive length")
        events[start] = events.get(start, 0) + 1
        events[stop] = events.get(stop, 0) - 1
    count, best, coordinate = 0, 0, None
    for point, delta in sorted(events.items()):
        count += delta
        if count > best:
            best, coordinate = count, point
    return best, coordinate

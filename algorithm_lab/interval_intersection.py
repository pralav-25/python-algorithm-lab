"""Intersect two sorted disjoint lists of closed integer intervals.

Each input has integer endpoints excluding bool, start <= stop, and strict
separation between successive intervals. Return closed intersections in
ascending order, including singleton endpoints. O(n+m) time and space for
copied inputs/output; the two-pointer scan uses O(1) auxiliary integers.

>>> interval_intersection([(0, 2), (5, 8)], [(2, 6)])
[(2, 2), (5, 6)]
"""

from algorithm_lab._validation import integer


def interval_intersection(left, right):
    def validate(intervals):
        result = []
        for start, stop in intervals:
            integer(start, "start")
            integer(stop, "stop")
            if start > stop or (result and start <= result[-1][1]):
                raise ValueError("intervals must be sorted, disjoint, and closed")
            result.append((start, stop))
        return result

    left, right = validate(left), validate(right)
    i, j, result = 0, 0, []
    while i < len(left) and j < len(right):
        start, stop = max(left[i][0], right[j][0]), min(left[i][1], right[j][1])
        if start <= stop:
            result.append((start, stop))
        if left[i][1] < right[j][1]:
            i += 1
        else:
            j += 1
    return result

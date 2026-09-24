"""Choose half-open integer intervals maximizing total integer value.

Input triples are (start, stop, value), with start < stop. Adjacent intervals
are compatible; negative values may be skipped. Returns (total, original_indices)
with indices in chronological order. Equal DP totals prefer skipping the current
interval; sorting is by stop, start, original index. O(n log n) time, O(n) space.

>>> weighted_interval_scheduling([(0, 2, 4), (1, 4, 7), (2, 5, 6)])
(10, [0, 2])
"""

from bisect import bisect_right

from algorithm_lab._validation import integer


def weighted_interval_scheduling(intervals):
    jobs = []
    for i, (start, stop, value) in enumerate(intervals):
        integer(start, "start")
        integer(stop, "stop")
        integer(value, "value")
        if start >= stop:
            raise ValueError("intervals must have positive length")
        jobs.append((stop, start, i, value))
    jobs.sort()
    ends = [stop for stop, _, _, _ in jobs]
    previous = [bisect_right(ends, start, 0, j) for j, (_, start, _, _) in enumerate(jobs)]
    scores, selected = [0] * (len(jobs) + 1), [False] * len(jobs)
    for j, (_, _, _, value) in enumerate(jobs):
        take = value + scores[previous[j]]
        if take > scores[j]:
            scores[j + 1], selected[j] = take, True
        else:
            scores[j + 1] = scores[j]
    result, count = [], len(jobs)
    while count:
        j = count - 1
        if selected[j]:
            result.append(jobs[j][2])
            count = previous[j]
        else:
            count -= 1
    return scores[-1], result[::-1]

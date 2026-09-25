"""Window minima with a monotonic deque.

Values must be mutually comparable under a total order; NaN is unsupported.
width is an integer in 1..len(values), excluding bool. Return one minimum
per window; equal values retain the earliest candidate. O(n) time and O(n)
copied/output storage, with O(width) deque storage.

>>> sliding_window_min([4, 2, 2, 5, 1], 3)
[2, 2, 1]
"""

from collections import deque

from algorithm_lab._validation import integer


def sliding_window_min(values, width):
    values = list(values)
    integer(width, "width", minimum=1)
    if width > len(values):
        raise ValueError("width must not exceed input length")
    candidates, result = deque(), []
    for i, value in enumerate(values):
        while candidates and candidates[0] <= i - width:
            candidates.popleft()
        while candidates and value < values[candidates[-1]]:
            candidates.pop()
        candidates.append(i)
        if i + 1 >= width:
            result.append(values[candidates[0]])
    return result

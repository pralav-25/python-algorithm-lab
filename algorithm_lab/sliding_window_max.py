"""Return maxima of all consecutive windows in O(n) time and O(window) workspace.

window is an integer from 1 through len(values); no window exists for empty data.
Values must be totally ordered (NaN is not supported). Input is not modified.

>>> sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
[3, 3, 5, 5, 6, 7]
"""

from collections import deque
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def sliding_window_max(values: Sequence[T], window: int) -> list[T]:
    if isinstance(window, bool) or not isinstance(window, int) or not 1 <= window <= len(values):
        raise ValueError("window must be between 1 and the input length")
    candidates = deque()
    result = []
    for index, value in enumerate(values):
        while candidates and candidates[0] <= index - window:
            candidates.popleft()
        while candidates and not value < values[candidates[-1]]:
            candidates.pop()
        candidates.append(index)
        if index >= window - 1:
            result.append(values[candidates[0]])
    return result

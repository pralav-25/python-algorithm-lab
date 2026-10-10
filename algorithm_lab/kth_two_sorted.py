"""Select the zero-based kth value from the merge of two sorted sequences.

Inputs must already be ascending with values sharing a total order. Sortedness
is not scanned. k must be an integer excluding bool in [0, len(a)+len(b)).
Equal values are interchangeable. Inputs are not modified. Time: O(log(k + 2));
auxiliary space: O(1). Invalid k raises ValueError.

>>> kth_two_sorted([1, 3, 5], [2, 3, 8], 3)
3
>>> kth_two_sorted([], [7], 0)
7
"""

from collections.abc import Sequence
from typing import TypeVar

from algorithm_lab._validation import integer

T = TypeVar("T")


def kth_two_sorted(a: Sequence[T], b: Sequence[T], k: int) -> T:
    integer(k, "k", minimum=0)
    if k >= len(a) + len(b):
        raise ValueError("k is out of range")
    i = j = 0
    while True:
        if i == len(a):
            return b[j + k]
        if j == len(b):
            return a[i + k]
        if k == 0:
            return b[j] if b[j] < a[i] else a[i]
        step = (k + 1) // 2
        take_a, take_b = min(step, len(a) - i), min(step, len(b) - j)
        if b[j + take_b - 1] < a[i + take_a - 1]:
            j += take_b
            k -= take_b
        else:
            i += take_a
            k -= take_a

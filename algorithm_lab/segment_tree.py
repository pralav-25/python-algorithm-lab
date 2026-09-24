"""Integer segment tree with O(n) construction/storage and O(log n) operations.

set replaces one value. sum queries half-open ranges, including empty ranges.
Invalid indices or non-integer values raise ValueError before changing state.

>>> tree = SegmentTree([1, 4, 2])
>>> tree.set(1, 9)
>>> tree.range_sum(0, 2)
10
"""

from algorithm_lab._validation import index, integer


class SegmentTree:
    def __init__(self, values):
        data = [integer(v) for v in values]
        self._n = len(data)
        self._tree = [0] * self._n + data
        for i in range(self._n - 1, 0, -1):
            self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]

    def __len__(self):
        return self._n

    def set(self, position, value):
        i = index(position, self._n) + self._n
        integer(value)
        self._tree[i] = value
        while i > 1:
            i //= 2
            self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]

    def range_sum(self, start, stop):
        index(start, self._n, allow_end=True)
        index(stop, self._n, allow_end=True)
        if start > stop:
            raise ValueError("start must not exceed stop")
        left, right, result = start + self._n, stop + self._n, 0
        while left < right:
            if left % 2:
                result += self._tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self._tree[right]
            left //= 2
            right //= 2
        return result

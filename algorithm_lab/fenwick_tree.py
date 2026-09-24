"""Integer Fenwick tree with O(n) construction and O(log n) updates and queries.

Storage is O(n). Indices are zero-based; range_sum(start, stop) is half-open.
Empty ranges sum to zero. Invalid indices and non-integer deltas raise ValueError.

>>> tree = FenwickTree([2, 5, -1])
>>> tree.add(1, 3)
>>> tree.range_sum(1, 3)
7
"""

from algorithm_lab._validation import index, integer


class FenwickTree:
    def __init__(self, values):
        data = [integer(v) for v in values]
        self._tree = [0] + data
        for i in range(1, len(self._tree)):
            parent = i + (i & -i)
            if parent < len(self._tree):
                self._tree[parent] += self._tree[i]

    def __len__(self):
        return len(self._tree) - 1

    def add(self, position, delta):
        i = index(position, len(self)) + 1
        integer(delta, "delta")
        while i < len(self._tree):
            self._tree[i] += delta
            i += i & -i

    def prefix_sum(self, stop):
        i = index(stop, len(self), allow_end=True)
        total = 0
        while i:
            total += self._tree[i]
            i -= i & -i
        return total

    def range_sum(self, start, stop):
        index(start, len(self), allow_end=True)
        index(stop, len(self), allow_end=True)
        if start > stop:
            raise ValueError("start must not exceed stop")
        return self.prefix_sum(stop) - self.prefix_sum(start)

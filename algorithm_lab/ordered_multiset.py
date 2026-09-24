"""Sorted-list multiset for comparable values with a total order.

Construction O(n log n); add/discard O(n); rank/count O(log n); select O(1).
Space O(n). rank counts strictly smaller values. discard removes one copy and
returns whether one existed. select uses zero-based nonnegative indices.

>>> values = OrderedMultiset([3, 1, 3])
>>> values.rank(3), values.count(3), values.select(1)
(1, 2, 3)
"""

from bisect import bisect_left, bisect_right, insort_right

from algorithm_lab._validation import index


class OrderedMultiset:
    def __init__(self, values=()):
        self._data = sorted(values)

    def __len__(self):
        return len(self._data)

    def add(self, value):
        insort_right(self._data, value)

    def discard(self, value):
        position = bisect_left(self._data, value)
        if position < len(self) and self._data[position] == value:
            self._data.pop(position)
            return True
        return False

    def rank(self, value):
        return bisect_left(self._data, value)

    def count(self, value):
        return bisect_right(self._data, value) - self.rank(value)

    def select(self, position):
        return self._data[index(position, len(self))]

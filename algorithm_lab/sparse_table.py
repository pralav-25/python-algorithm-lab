"""Range minima on comparable values; O(n log n) preprocessing and space.

query(start, stop) takes O(1) and requires a nonempty half-open range.
Values must have a total order (no NaN). Input is copied; there are no updates.

>>> SparseTable([5, 2, 7, 1]).query(0, 3)
2
"""

from algorithm_lab._validation import index


class SparseTable:
    def __init__(self, values):
        data = list(values)
        self._n = len(data)
        self._rows = [data]
        width = 2
        while width <= self._n:
            half = width // 2
            previous = self._rows[-1]
            self._rows.append(
                [min(previous[i], previous[i + half]) for i in range(self._n - width + 1)]
            )
            width *= 2

    def __len__(self):
        return self._n

    def query(self, start, stop):
        index(start, self._n)
        index(stop, self._n, allow_end=True)
        if start >= stop:
            raise ValueError("range must be nonempty")
        level = (stop - start).bit_length() - 1
        return min(self._rows[level][start], self._rows[level][stop - (1 << level)])

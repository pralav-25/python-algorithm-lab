"""Streaming floating-point mean and variance using Welford's recurrence.

Each add uses O(1) time and space. Only finite int/float observations are accepted;
nonfinite or unrepresentable updates raise ValueError before changing state.
An empty mean/population variance, or sample variance with fewer than two values,
raises ValueError. extend applies observations sequentially, not as one transaction.

>>> stats = RunningStats([1, 2, 3])
>>> stats.mean, stats.variance(sample=True)
(2.0, 1.0)
"""

import math
from collections.abc import Iterable


class RunningStats:
    def __init__(self, values: Iterable[float] = ()):
        self._count, self._mean, self._m2 = 0, 0.0, 0.0
        self.extend(values)

    @property
    def count(self) -> int:
        return self._count

    @property
    def mean(self) -> float:
        if not self._count:
            raise ValueError("mean requires at least one observation")
        return self._mean

    def add(self, value: float) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("observations must be finite numbers")
        try:
            value = float(value)
        except OverflowError as exc:
            raise ValueError("observation exceeds the floating-point range") from exc
        if not math.isfinite(value):
            raise ValueError("observations must be finite numbers")
        count = self._count + 1
        delta = value - self._mean
        mean = self._mean + delta / count
        m2 = self._m2 + delta * (value - mean)
        if not math.isfinite(mean) or not math.isfinite(m2):
            raise ValueError("update exceeds the floating-point range")
        self._count, self._mean, self._m2 = count, mean, max(0.0, m2)

    def extend(self, values: Iterable[float]) -> None:
        for value in values:
            self.add(value)

    def variance(self, *, sample: bool = False) -> float:
        if not isinstance(sample, bool):
            raise ValueError("sample must be a boolean")
        denominator = self._count - int(sample)
        if denominator <= 0:
            raise ValueError("not enough observations for this variance")
        return self._m2 / denominator

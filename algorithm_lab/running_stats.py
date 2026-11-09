"""Streaming floating-point mean and variance using Welford's recurrence.

Observations are shifted by the first value before updating the mean and moment,
preserving small differences near large common offsets. Each add uses O(1) time
and space. Only finite int/float observations are accepted;
nonfinite or unrepresentable updates raise ValueError before changing state.
An empty mean/population variance, or sample variance with fewer than two values,
raises ValueError. extend applies observations sequentially, not as one transaction.

>>> stats = RunningStats([1, 2, 3])
>>> stats.mean, stats.variance(sample=True)
(2.0, 1.0)
"""

import math
from collections.abc import Iterable

from algorithm_lab._numeric import finite


class RunningStats:
    def __init__(self, values: Iterable[float] = ()):
        self._count, self._mean, self._m2 = 0, 0.0, 0.0
        self._origin = 0.0
        self.extend(values)

    @property
    def count(self) -> int:
        return self._count

    @property
    def mean(self) -> float:
        if not self._count:
            raise ValueError("mean requires at least one observation")
        return self._origin + self._mean

    def add(self, value: float) -> None:
        try:
            value = finite(value)
        except ValueError as exc:
            raise ValueError("observations must be finite numbers") from exc
        origin = self._origin if self._count else value
        value -= origin
        count = self._count + 1
        delta = value - self._mean
        mean = self._mean + delta / count
        m2 = self._m2 + delta * (value - mean)
        if not math.isfinite(mean) or not math.isfinite(m2):
            raise ValueError("update exceeds the floating-point range")
        self._count, self._mean, self._m2 = count, mean, max(0.0, m2)
        self._origin = origin

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

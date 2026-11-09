"""Streaming exact-total mean and shifted Welford variance, returned as floats.

Observations are shifted by the first value before updating the variance moment,
preserving small differences near large common offsets. The reported mean uses
an exact rational total of the validated floats so cancellation against a distant
first observation does not erase a residual. Each add uses O(1) arithmetic
operations and a fixed number of accumulators; the exact total's integer storage
can grow with the observation count. Only finite int/float observations are accepted;
nonfinite or unrepresentable updates raise ValueError before changing state.
An empty mean/population variance, or sample variance with fewer than two values,
raises ValueError. extend applies observations sequentially, not as one transaction.

>>> stats = RunningStats([1, 2, 3])
>>> stats.mean, stats.variance(sample=True)
(2.0, 1.0)
"""

import math
from collections.abc import Iterable
from fractions import Fraction

from algorithm_lab._numeric import finite


class RunningStats:
    def __init__(self, values: Iterable[float] = ()):
        self._count, self._mean, self._m2 = 0, 0.0, 0.0
        self._origin = 0.0
        self._total = Fraction(0)
        self.extend(values)

    @property
    def count(self) -> int:
        return self._count

    @property
    def mean(self) -> float:
        if not self._count:
            raise ValueError("mean requires at least one observation")
        return float(self._total / self._count)

    def add(self, value: float) -> None:
        try:
            observation = finite(value)
        except ValueError as exc:
            raise ValueError("observations must be finite numbers") from exc
        origin = self._origin if self._count else observation
        value = observation - origin
        count = self._count + 1
        delta = value - self._mean
        mean = self._mean + delta / count
        m2 = self._m2 + delta * (value - mean)
        if not math.isfinite(mean) or not math.isfinite(m2):
            raise ValueError("update exceeds the floating-point range")
        total = self._total + Fraction(observation)
        self._count, self._mean, self._m2 = count, mean, max(0.0, m2)
        self._origin = origin
        self._total = total

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

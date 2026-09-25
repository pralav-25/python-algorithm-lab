"""One-pass covariance for paired numeric observations.

observations yields (x,y) pairs of finite int/float values, excluding bool.
sample is a bool selecting n-1 rather than n as divisor. Require one pair
for population or two for sample covariance. Return a float; unrepresentable
intermediate state raises ValueError. O(n) time and O(1) state using a
paired Welford recurrence; observations need not fit in memory.

>>> online_covariance([(1, 2), (2, 4), (3, 6)], sample=True)
2.0
"""

from math import isfinite

from algorithm_lab._numeric import finite


def online_covariance(observations, *, sample=False):
    if not isinstance(sample, bool):
        raise ValueError("sample must be a boolean")
    count, mean_x, mean_y, moment = 0, 0.0, 0.0, 0.0
    for x, y in observations:
        x, y = finite(x), finite(y)
        count += 1
        delta_x, delta_y = x - mean_x, y - mean_y
        mean_x += delta_x / count
        mean_y += delta_y / count
        moment += delta_x * (y - mean_y)
        if not all(isfinite(v) for v in (mean_x, mean_y, moment)):
            raise ValueError("covariance exceeds floating-point range")
    denominator = count - int(sample)
    if denominator <= 0:
        raise ValueError("not enough observations")
    return moment / denominator

"""Linearly interpolated sample quantiles.

Values are nonempty finite int/float observations excluding bool. q is a
finite number in [0,1], excluding bool. Return a float at position
q*(n-1) in sorted data (the common type-7 convention). O(n log n) time and
O(n) space. Input order is irrelevant and input is unchanged.

>>> percentile([0, 10, 20, 30], 0.25)
7.5
"""

from math import floor

from algorithm_lab._numeric import finite


def percentile(values, q):
    values = sorted(finite(value) for value in values)
    q = finite(q)
    if not values or not 0 <= q <= 1:
        raise ValueError("nonempty values and q in [0,1] are required")
    position = q * (len(values) - 1)
    index = floor(position)
    if index == len(values) - 1:
        return values[index]
    fraction = position - index
    return (1 - fraction) * values[index] + fraction * values[index + 1]

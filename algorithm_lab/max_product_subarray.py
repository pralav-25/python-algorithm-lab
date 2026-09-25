"""Maximum contiguous integer product with signed extrema.

Accept a nonempty iterable of integers excluding bool. Return the largest
product of any nonempty contiguous slice. Tracking both maximum and minimum
products handles negative factors and zeros. O(n) arithmetic steps and O(1)
stored integers; integer multiplication cost depends on operand bit length.

>>> max_product_subarray([-2, 3, -4])
24
"""

from algorithm_lab._validation import integer


def max_product_subarray(values):
    low = high = best = None
    for value in values:
        integer(value)
        if best is None:
            low = high = best = value
        else:
            low, high = min(value, low * value, high * value), max(value, low * value, high * value)
            best = max(best, high)
    if best is None:
        raise ValueError("input must be nonempty")
    return best

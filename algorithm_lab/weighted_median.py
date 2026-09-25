"""Lower weighted medians with exact integer weights.

Values and weights are equally sized integer iterables, excluding bool.
Weights are nonnegative with positive total; zero weights have no influence.
Return the smallest observed value whose cumulative weight reaches half the
total. This minimizes weighted absolute deviation. O(n log n) time, O(n) space.

>>> weighted_median([10, 1, 5], [1, 2, 1])
1
"""

from algorithm_lab._validation import integer


def weighted_median(values, weights):
    values, weights = list(values), list(weights)
    if len(values) != len(weights):
        raise ValueError("values and weights must have equal length")
    for value in values:
        integer(value)
    for weight in weights:
        integer(weight, "weight", minimum=0)
    total = sum(weights)
    if not total:
        raise ValueError("total weight must be positive")
    cumulative = 0
    for value, weight in sorted(zip(values, weights, strict=True)):
        cumulative += weight
        if cumulative * 2 >= total:
            return value
    raise AssertionError("positive total must produce a median")

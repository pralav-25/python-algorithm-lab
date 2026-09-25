"""Stable softmax by subtracting the maximum logit.

Accept a nonempty iterable of finite int/float logits, excluding bool.
Return nonnegative probabilities summing to approximately 1. Subtracting
the maximum avoids exponential overflow; very small tails can underflow
to zero. O(n) time and space, leaving input unchanged.

>>> softmax([1000, 1000])
[0.5, 0.5]
"""

from math import exp, fsum

from algorithm_lab._numeric import finite


def softmax(logits):
    logits = [finite(value) for value in logits]
    if not logits:
        raise ValueError("logits must be nonempty")
    maximum = max(logits)
    values = [exp(value - maximum) for value in logits]
    total = fsum(values)
    return [value / total for value in values]

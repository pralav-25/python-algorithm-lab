"""Symmetric Jensen-Shannon divergence in bits.

Inputs are equal-length vectors of finite nonnegative int/float weights,
excluding bool, each with positive mass. Normalize each independently and
compare against their equally weighted mixture. Return divergence in [0,1]
up to floating-point rounding; this is not the square-root distance.
O(n) time and space. Tiny probabilities may underflow to zero.

>>> jensen_shannon_divergence([1, 0], [0, 1])
1.0
"""

from math import fsum, log2

from algorithm_lab._numeric import probabilities


def jensen_shannon_divergence(left, right):
    left, right = probabilities(left), probabilities(right)
    if len(left) != len(right):
        raise ValueError("distributions must have equal length")
    terms = []
    for p, q in zip(left, right, strict=True):
        if p:
            terms.append(p * (log2(p) - log2(p + q) + 1) / 2)
        if q:
            terms.append(q * (log2(q) - log2(p + q) + 1) / 2)
    return max(0.0, min(1.0, fsum(terms)))

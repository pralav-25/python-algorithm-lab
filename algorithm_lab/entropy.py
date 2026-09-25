"""Shannon entropy in bits from nonnegative weights.

Accept finite int/float weights, excluding bool, with positive total mass.
Normalize by the largest weight before summing to avoid overflow. Zero-mass
categories contribute zero. Return entropy in bits. O(n) time and space.
Extremely small probabilities may underflow to zero in floating point.

>>> entropy([1, 1, 1, 1])
2.0
"""

from math import fsum, log2

from algorithm_lab._numeric import probabilities


def entropy(weights):
    return fsum(-p * log2(p) for p in probabilities(weights) if p > 0)

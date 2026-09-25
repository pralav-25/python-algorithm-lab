"""Exact unweighted isotonic regression with pooled adjacent violators.

Accept int/Fraction values, excluding bool and float. Return nondecreasing
Fraction fitted values minimizing the sum of squared residuals. Adjacent
blocks merge only for a strict decrease. Empty input returns []. O(n)
rational operations and O(n) space; no observations are reordered.

>>> isotonic_regression([3, 1, 2, 5])
[Fraction(2, 1), Fraction(2, 1), Fraction(2, 1), Fraction(5, 1)]
"""

from fractions import Fraction


def isotonic_regression(values):
    blocks = []
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
            raise ValueError("values must be integers or Fractions")
        blocks.append((Fraction(value), 1))
        while len(blocks) > 1 and blocks[-2][0] * blocks[-1][1] > blocks[-1][0] * blocks[-2][1]:
            right, count_right = blocks.pop()
            left, count_left = blocks.pop()
            blocks.append((left + right, count_left + count_right))
    return [total / count for total, count in blocks for _ in range(count)]

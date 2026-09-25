"""Evaluate the interpolating polynomial with exact rationals.

Points and x contain int or Fraction values, excluding bool and float.
Require at least one point and distinct abscissas. Return a Fraction; the
polynomial has degree less than the number of points. O(n^2) rational
operations and O(n) space. Point order does not affect the answer.

>>> lagrange_interpolation([(0, 1), (1, 2), (2, 5)], 3)
Fraction(10, 1)
"""

from fractions import Fraction


def lagrange_interpolation(points, x):
    def rational(value):
        if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
            raise ValueError("coordinates must be integers or Fractions")
        return Fraction(value)

    x = rational(x)
    points = [(rational(a), rational(b)) for a, b in points]
    if not points or len({a for a, _ in points}) != len(points):
        raise ValueError("points must be nonempty with distinct abscissas")
    result = Fraction(0)
    for i, (a, b) in enumerate(points):
        term = b
        for j, (other, _) in enumerate(points):
            if i != j:
                term *= (x - other) / (a - other)
        result += term
    return result

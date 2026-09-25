import unittest
from fractions import Fraction

from algorithm_lab.lagrange_interpolation import lagrange_interpolation


class Tests(unittest.TestCase):
    def test_recover_polynomials(self):
        for coefficients in [[3], [1, -2], [4, 0, -3, 2]]:

            def evaluate(x, coefficients=coefficients):
                return sum(c * x**i for i, c in enumerate(coefficients))

            points = [(x, evaluate(x)) for x in range(len(coefficients))]
            for x in [Fraction(1, 2), -5, 9]:
                self.assertEqual(lagrange_interpolation(reversed(points), x), evaluate(x))

    def test_invalid(self):
        for points in [[], [(1, 2), (1, 3)], [(True, 2)], [(1, 2.0)]]:
            with self.assertRaises(ValueError):
                lagrange_interpolation(points, 0)

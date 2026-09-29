import unittest
from fractions import Fraction
from itertools import permutations

from algorithm_lab.lagrange_interpolation import lagrange_interpolation


class Tests(unittest.TestCase):
    def test_rational_nodes_and_exact_node_evaluation(self):
        def polynomial(x):
            return Fraction(2, 7) * x**3 - Fraction(5, 11) * x + Fraction(3, 13)

        nodes = [Fraction(-3, 2), Fraction(1, 3), Fraction(7, 4), Fraction(11, 5)]
        points = [(x, polynomial(x)) for x in nodes]
        original = points[:]
        for ordered in permutations(points):
            for x in [*nodes, Fraction(-8, 9), Fraction(17, 6)]:
                self.assertEqual(lagrange_interpolation(iter(ordered), x), polynomial(x))
        self.assertEqual(points, original)
        with self.assertRaises(ValueError):
            lagrange_interpolation([(1, 2), (Fraction(2, 2), 3)], 0)

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

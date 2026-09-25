import unittest
from fractions import Fraction

from algorithm_lab.continued_fraction_convergents import continued_fraction_convergents


class Tests(unittest.TestCase):
    def test_prefix_oracle(self):
        for terms in [[], [-3], [0, 2], [3, 7, 15, 1, 292], [-2, 1, 3, 2]]:
            result = continued_fraction_convergents(iter(terms))
            for i, actual in enumerate(result):
                expected = Fraction(terms[i])
                for term in reversed(terms[:i]):
                    expected = term + 1 / expected
                self.assertEqual(actual, expected)

    def test_invalid(self):
        for terms in [[True], [1, 0], [1, -2], [1, 2.0]]:
            with self.assertRaises(ValueError):
                continued_fraction_convergents(terms)

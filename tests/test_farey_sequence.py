import unittest
from fractions import Fraction

from algorithm_lab.farey_sequence import farey_sequence


class Tests(unittest.TestCase):
    def test_fraction_set_oracle(self):
        for order in range(1, 40):
            expected = sorted(
                {
                    Fraction(numerator, denominator)
                    for denominator in range(1, order + 1)
                    for numerator in range(denominator + 1)
                }
            )
            result = farey_sequence(order)
            self.assertEqual(result, expected)
            self.assertTrue(all(isinstance(value, Fraction) for value in result))

    def test_fresh_result(self):
        values = farey_sequence(1)
        values.clear()
        self.assertEqual(farey_sequence(1), [Fraction(0), Fraction(1)])

    def test_invalid(self):
        for order in (0, -1, True, 2.5, "3", None):
            with self.assertRaises(ValueError):
                farey_sequence(order)

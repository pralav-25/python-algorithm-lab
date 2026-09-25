import unittest
from math import gcd

from algorithm_lab.multiplicative_order import multiplicative_order


class Tests(unittest.TestCase):
    def test_minimal_exponent(self):
        for modulus in range(2, 60):
            for value in range(-10, 30):
                if gcd(value, modulus) == 1:
                    expected = next(k for k in range(1, modulus) if pow(value, k, modulus) == 1)
                    self.assertEqual(multiplicative_order(value, modulus), expected)
                else:
                    with self.assertRaises(ValueError):
                        multiplicative_order(value, modulus)

    def test_invalid(self):
        for args in [(1, 1), (True, 3), (1, 3.5)]:
            with self.assertRaises(ValueError):
                multiplicative_order(*args)

import math
import unittest

from algorithm_lab.carmichael_function import carmichael_function


class Tests(unittest.TestCase):
    def test_group_exponent_oracle(self):
        self.assertEqual(carmichael_function(1), 1)
        for modulus in range(2, 100):
            units = [value for value in range(1, modulus) if math.gcd(value, modulus) == 1]
            expected = next(
                exponent
                for exponent in range(1, modulus + 1)
                if all(pow(value, exponent, modulus) == 1 for value in units)
            )
            self.assertEqual(carmichael_function(modulus), expected)

    def test_invalid(self):
        for n in (0, -1, True, 2.5, "3", None):
            with self.assertRaises(ValueError):
                carmichael_function(n)

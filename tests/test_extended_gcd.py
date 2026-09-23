import math
import unittest

from algorithm_lab.extended_gcd import extended_gcd


class ExtendedGCDTests(unittest.TestCase):
    def test_signed_bezout_identity(self):
        for a in range(-30, 31):
            for b in range(-30, 31):
                divisor, x, y = extended_gcd(a, b)
                self.assertEqual(divisor, math.gcd(a, b))
                self.assertEqual(a * x + b * y, divisor)

    def test_large_integers_and_validation(self):
        a, b = 10**150 + 6, 10**100 + 2
        divisor, x, y = extended_gcd(a, b)
        self.assertEqual((divisor, a * x + b * y), (math.gcd(a, b), math.gcd(a, b)))
        for a, b in [(True, 1), (2, 1.0), ("1", 2)]:
            with self.assertRaises(ValueError):
                extended_gcd(a, b)

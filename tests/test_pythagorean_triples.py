import math
import unittest

from algorithm_lab.pythagorean_triples import pythagorean_triples


class Tests(unittest.TestCase):
    def test_leg_enumeration_oracle(self):
        for limit in (0, 1, 4, 5, 13, 25, 65, 100):
            expected = []
            for a in range(1, limit + 1):
                for b in range(a + 1, limit + 1):
                    square = a * a + b * b
                    c = math.isqrt(square)
                    if c <= limit and c * c == square and math.gcd(a, b) == 1:
                        expected.append((a, b, c))
            expected.sort(key=lambda triple: (triple[2], triple[0], triple[1]))
            self.assertEqual(pythagorean_triples(limit), expected)

    def test_equal_hypotenuse_order(self):
        at_65 = [triple for triple in pythagorean_triples(65) if triple[2] == 65]
        self.assertEqual(at_65, [(16, 63, 65), (33, 56, 65)])

    def test_invalid(self):
        for limit in (-1, True, 2.5, "3", None):
            with self.assertRaises(ValueError):
                pythagorean_triples(limit)

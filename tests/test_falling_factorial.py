import itertools
import math
import unittest

from algorithm_lab.falling_factorial import falling_factorial


class Tests(unittest.TestCase):
    def test_injective_word_oracle(self):
        for n in range(6):
            for k in range(6):
                expected = sum(
                    len(set(word)) == k for word in itertools.product(range(n), repeat=k)
                )
                self.assertEqual(falling_factorial(n, k), expected)

    def test_negative_factorial_identity(self):
        for magnitude in range(1, 8):
            for k in range(8):
                expected = (-1) ** k * math.factorial(magnitude + k - 1)
                expected //= math.factorial(magnitude - 1)
                self.assertEqual(falling_factorial(-magnitude, k), expected)

    def test_invalid(self):
        for args in ((True, 0), (2, True), (1.5, 0), (2, -1), (2, "1")):
            with self.assertRaises(ValueError):
                falling_factorial(*args)

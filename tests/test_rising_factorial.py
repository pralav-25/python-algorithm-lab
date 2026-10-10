import itertools
import math
import unittest

from algorithm_lab.rising_factorial import rising_factorial


class Tests(unittest.TestCase):
    def test_multiset_enumeration_identity(self):
        for n in range(6):
            for k in range(6):
                multisets = sum(1 for _ in itertools.combinations_with_replacement(range(n), k))
                self.assertEqual(rising_factorial(n, k), multisets * math.factorial(k))

    def test_negative_and_zero_boundaries(self):
        expected = [1, -4, 12, -24, 24, 0, 0]
        self.assertEqual([rising_factorial(-4, k) for k in range(7)], expected)
        self.assertEqual(rising_factorial(0, 0), 1)

    def test_invalid(self):
        for args in ((True, 0), (2, True), (1.5, 0), (2, -1), (2, "1")):
            with self.assertRaises(ValueError):
                rising_factorial(*args)

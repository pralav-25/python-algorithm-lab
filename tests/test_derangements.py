import itertools
import math
import unittest

from algorithm_lab.derangements import derangements


class DerangementTests(unittest.TestCase):
    def test_enumeration(self):
        for n in range(9):
            count = sum(
                all(i != v for i, v in enumerate(p)) for p in itertools.permutations(range(n))
            )
            self.assertEqual(derangements(n), count)
        n = 70
        factorial = math.factorial(n)
        expected = sum((-1) ** k * (factorial // math.factorial(k)) for k in range(n + 1))
        self.assertEqual(derangements(n), expected)

    def test_invalid(self):
        for n in [-1, True, 2.5]:
            with self.assertRaises(ValueError):
                derangements(n)

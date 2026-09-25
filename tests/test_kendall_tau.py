import math
import unittest
from itertools import permutations

from algorithm_lab.kendall_tau import kendall_tau


class Tests(unittest.TestCase):
    def test_permutation_inversion_oracle(self):
        for n in range(2, 7):
            pairs = n * (n - 1) // 2
            for p in permutations(range(n)):
                inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
                self.assertAlmostEqual(kendall_tau(range(n), p), (pairs - 2 * inversions) / pairs)
        self.assertAlmostEqual(kendall_tau([1, 1, 2], [1, 2, 3]), 2 / math.sqrt(6))

    def test_invalid(self):
        for a, b in [
            ([], []),
            ([1], [1]),
            ([1, 1], [1, 2]),
            ([1, 2], [1]),
            ([True, 2], [1, 2]),
            ([math.nan, 2], [1, 2]),
        ]:
            with self.assertRaises(ValueError):
                kendall_tau(a, b)

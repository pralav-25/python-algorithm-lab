import math
import unittest
from itertools import permutations

from algorithm_lab.kendall_tau import kendall_tau


class Tests(unittest.TestCase):
    def test_mixed_ties_and_axis_reversal(self):
        pairs = [(0, 0), (0, 0), (0, 2), (1, 1), (2, 1), (3, 3)]
        concordant = discordant = tied_left = tied_right = 0
        for i, (x, y) in enumerate(pairs):
            for u, v in pairs[i + 1 :]:
                if x == u and y == v:
                    continue
                if x == u:
                    tied_left += 1
                elif y == v:
                    tied_right += 1
                elif (x < u) == (y < v):
                    concordant += 1
                else:
                    discordant += 1
        untied = concordant + discordant
        expected = (concordant - discordant) / math.sqrt(
            (untied + tied_left) * (untied + tied_right)
        )
        x, y = zip(*pairs, strict=True)
        self.assertAlmostEqual(kendall_tau(iter(x), iter(y)), expected)
        self.assertAlmostEqual(kendall_tau(y, x), expected)
        self.assertAlmostEqual(kendall_tau([-v for v in x], y), -expected)
        self.assertAlmostEqual(kendall_tau(reversed(x), reversed(y)), expected)

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

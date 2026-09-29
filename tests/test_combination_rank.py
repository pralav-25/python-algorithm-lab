import unittest
from itertools import combinations
from math import comb

from algorithm_lab.combination_rank import combination_rank


class Tests(unittest.TestCase):
    def test_large_lexicographic_blocks(self):
        n, k = 100, 50
        self.assertEqual(combination_rank(n, range(k)), 0)
        self.assertEqual(combination_rank(n, range(n - k, n)), comb(n, k) - 1)
        # Fixing the first element at zero occupies exactly C(n-1, k-1) ranks.
        self.assertEqual(combination_rank(n, range(1, k + 1)), comb(n - 1, k - 1))
        values = [0, *range(n - k + 1, n)]
        original = values[:]
        self.assertEqual(combination_rank(n, iter(values)), comb(n - 1, k - 1) - 1)
        self.assertEqual(combination_rank(n, values), comb(n - 1, k - 1) - 1)
        self.assertEqual(values, original)

    def test_enumeration_oracle(self):
        for n in range(9):
            for k in range(n + 1):
                for rank, values in enumerate(combinations(range(n), k)):
                    self.assertEqual(combination_rank(n, values), rank)

    def test_invalid(self):
        for n, values in [(3, [1, 1]), (3, [2, 1]), (3, [3]), (3, [True]), (-1, [])]:
            with self.assertRaises(ValueError):
                combination_rank(n, values)

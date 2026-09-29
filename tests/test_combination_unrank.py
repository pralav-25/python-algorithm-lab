import unittest
from itertools import combinations
from math import comb

from algorithm_lab.combination_unrank import combination_unrank


class Tests(unittest.TestCase):
    def test_large_rank_block_transitions(self):
        n, k = 100, 50
        boundary = comb(n - 1, k - 1)
        self.assertGreater(boundary, 2**64)
        self.assertEqual(combination_unrank(n, k, boundary - 1), [0, *range(n - k + 1, n)])
        self.assertEqual(combination_unrank(n, k, boundary), list(range(1, k + 1)))
        self.assertEqual(combination_unrank(n, k, comb(n, k) - 1), list(range(n - k, n)))
        with self.assertRaises(ValueError):
            combination_unrank(n, k, comb(n, k))
        self.assertEqual(combination_unrank(100, 0, 0), [])
        self.assertEqual(combination_unrank(100, 100, 0), list(range(100)))

    def test_enumeration_oracle(self):
        for n in range(9):
            for k in range(n + 1):
                for rank, values in enumerate(combinations(range(n), k)):
                    self.assertEqual(combination_unrank(n, k, rank), list(values))

    def test_invalid(self):
        for args in [(2, 3, 0), (2, 1, 2), (2, 1, -1), (True, 1, 0), (2, False, 0)]:
            with self.assertRaises(ValueError):
                combination_unrank(*args)

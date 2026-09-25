import unittest
from itertools import combinations

from algorithm_lab.combination_unrank import combination_unrank


class Tests(unittest.TestCase):
    def test_enumeration_oracle(self):
        for n in range(9):
            for k in range(n + 1):
                for rank, values in enumerate(combinations(range(n), k)):
                    self.assertEqual(combination_unrank(n, k, rank), list(values))

    def test_invalid(self):
        for args in [(2, 3, 0), (2, 1, 2), (2, 1, -1), (True, 1, 0), (2, False, 0)]:
            with self.assertRaises(ValueError):
                combination_unrank(*args)

import unittest
from itertools import combinations

from algorithm_lab.combination_rank import combination_rank


class Tests(unittest.TestCase):
    def test_enumeration_oracle(self):
        for n in range(9):
            for k in range(n + 1):
                for rank, values in enumerate(combinations(range(n), k)):
                    self.assertEqual(combination_rank(n, values), rank)

    def test_invalid(self):
        for n, values in [(3, [1, 1]), (3, [2, 1]), (3, [3]), (3, [True]), (-1, [])]:
            with self.assertRaises(ValueError):
                combination_rank(n, values)

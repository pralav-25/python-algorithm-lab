import unittest
from itertools import permutations

from algorithm_lab.permutation_unrank import permutation_unrank


class Tests(unittest.TestCase):
    def test_enumeration_oracle(self):
        for n in range(7):
            for rank, values in enumerate(permutations(range(n))):
                self.assertEqual(permutation_unrank(n, rank), list(values))

    def test_invalid(self):
        for args in [(0, 1), (3, 6), (2, -1), (-1, 0), (True, 0)]:
            with self.assertRaises(ValueError):
                permutation_unrank(*args)

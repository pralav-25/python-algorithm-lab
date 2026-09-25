import unittest
from itertools import permutations

from algorithm_lab.permutation_rank import permutation_rank


class Tests(unittest.TestCase):
    def test_enumeration_oracle(self):
        for n in range(7):
            for rank, values in enumerate(permutations(range(n))):
                self.assertEqual(permutation_rank(values), rank)

    def test_invalid(self):
        for values in [[0, 0], [1], [-1, 0], [True, 0], [0.0]]:
            with self.assertRaises(ValueError):
                permutation_rank(values)

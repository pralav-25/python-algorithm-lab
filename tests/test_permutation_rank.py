import unittest
from itertools import permutations
from math import factorial

from algorithm_lab.permutation_rank import permutation_rank


class Tests(unittest.TestCase):
    def test_large_factorial_blocks_and_exact_rank(self):
        n = 30
        self.assertEqual(permutation_rank(reversed(range(n))), factorial(n) - 1)
        # A fixed leading value skips a whole block for each smaller value.
        for first in [1, 7, n - 1]:
            values = [first] + [v for v in range(n) if v != first]
            original = values[:]
            self.assertEqual(permutation_rank(iter(values)), first * factorial(n - 1))
            self.assertEqual(permutation_rank(values), first * factorial(n - 1))
            self.assertEqual(values, original)
        values = list(range(n))
        values[-2:] = reversed(values[-2:])
        self.assertEqual(permutation_rank(values), 1)

    def test_enumeration_oracle(self):
        for n in range(7):
            for rank, values in enumerate(permutations(range(n))):
                self.assertEqual(permutation_rank(values), rank)

    def test_invalid(self):
        for values in [[0, 0], [1], [-1, 0], [True, 0], [0.0]]:
            with self.assertRaises(ValueError):
                permutation_rank(values)

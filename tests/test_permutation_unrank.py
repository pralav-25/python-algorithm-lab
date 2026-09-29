import unittest
from itertools import permutations
from math import factorial

from algorithm_lab.permutation_unrank import permutation_unrank


class Tests(unittest.TestCase):
    def test_large_factorial_block_boundaries(self):
        n = 30
        block = factorial(n - 1)
        self.assertEqual(permutation_unrank(n, block - 1), [0, *range(n - 1, 0, -1)])
        self.assertEqual(permutation_unrank(n, block), [1, 0, *range(2, n)])
        self.assertEqual(permutation_unrank(n, factorial(n) - 1), list(reversed(range(n))))
        with self.assertRaises(ValueError):
            permutation_unrank(n, factorial(n))
        first = permutation_unrank(n, block)
        first[0] = -1
        self.assertEqual(permutation_unrank(n, block), [1, 0, *range(2, n)])

    def test_enumeration_oracle(self):
        for n in range(7):
            for rank, values in enumerate(permutations(range(n))):
                self.assertEqual(permutation_unrank(n, rank), list(values))

    def test_invalid(self):
        for args in [(0, 1), (3, 6), (2, -1), (-1, 0), (True, 0)]:
            with self.assertRaises(ValueError):
                permutation_unrank(*args)

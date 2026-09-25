import unittest
from itertools import permutations, product

from algorithm_lab.multiset_permutations import multiset_permutations


class Tests(unittest.TestCase):
    def test_deduplicated_oracle(self):
        for size in range(6):
            for values in product(range(2), repeat=size):
                self.assertEqual(
                    list(multiset_permutations(values)), sorted(set(permutations(values)))
                )
        self.assertEqual(next(multiset_permutations([1] * 2000)), (1,) * 2000)

    def test_invalid(self):
        for values in [[True], [1.5]]:
            with self.assertRaises(ValueError):
                list(multiset_permutations(values))

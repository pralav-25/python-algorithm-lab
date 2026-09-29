import unittest
from itertools import permutations, product
from math import factorial

from algorithm_lab.multiset_permutations import multiset_permutations


class Tests(unittest.TestCase):
    def test_signed_multinomial_count_and_yielded_snapshots(self):
        values = [-(10**80), -(10**80), 0, 0, 0, 10**80]
        original = values[:]
        generator = multiset_permutations(iter(values))
        first = next(generator)
        rest = list(generator)
        results = [first, *rest]
        self.assertEqual(len(results), factorial(6) // (factorial(2) * factorial(3)))
        self.assertEqual(len(set(results)), len(results))
        self.assertEqual(results, sorted(results))
        self.assertEqual(first, tuple(sorted(values)))
        self.assertEqual(results[-1], tuple(sorted(values, reverse=True)))
        for result in results:
            self.assertEqual(sorted(result), sorted(values))
        list(multiset_permutations(values))
        self.assertEqual(values, original)

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

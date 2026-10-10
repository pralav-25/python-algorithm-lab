import itertools
import unittest

from algorithm_lab.minimum_pair_difference import minimum_pair_difference


class MinimumDifferenceTests(unittest.TestCase):
    def test_all_pairs_oracle(self):
        for n in range(7):
            for data in itertools.product((-4, 0, 1, 9), repeat=n):
                expected = min(
                    (abs(a - b) for a, b in itertools.combinations(data, 2)), default=None
                )
                self.assertEqual(minimum_pair_difference(iter(data)), expected)

    def test_huge_numbers_no_mutation_and_validation(self):
        data = [10**100, -(10**100), 10**100 + 1]
        original = data[:]
        self.assertEqual(minimum_pair_difference(data), 1)
        self.assertEqual(data, original)
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                minimum_pair_difference([bad])

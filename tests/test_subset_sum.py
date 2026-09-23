import random
import unittest

from algorithm_lab.subset_sum import subset_sum


class SubsetSumTests(unittest.TestCase):
    def test_exhaustive_subsets(self):
        rng = random.Random(53)
        for _ in range(50):
            values = [rng.randrange(10) for _ in range(8)]
            totals = {sum(values[i] for i in range(8) if mask & (1 << i)) for mask in range(256)}
            for target in range(35):
                self.assertEqual(subset_sum(iter(values), target), target in totals)

    def test_boundaries_and_huge_irrelevant_values(self):
        self.assertTrue(subset_sum([], 0))
        self.assertFalse(subset_sum([], 1))
        self.assertFalse(subset_sum([10**100], 7))
        for values, target in [([-1], 0), ([True], 1), ([1.2], 2), ([1], -1), ([1], True)]:
            with self.assertRaises(ValueError):
                subset_sum(values, target)

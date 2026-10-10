import itertools
import random
import unittest

from algorithm_lab.three_sum import three_sum


class SumTests(unittest.TestCase):
    def test_independent_position_combination_oracle(self):
        rng = random.Random(3)
        for n in range(10):
            for _ in range(25):
                values = [rng.randrange(-4, 5) for _ in range(n)]
                original = values[:]
                target = rng.randrange(-5, 6)
                expected = sorted(
                    {
                        tuple(sorted(items))
                        for items in itertools.combinations(values, 3)
                        if sum(items) == target
                    }
                )
                self.assertEqual(three_sum(iter(values), target), expected)
                self.assertEqual(values, original)

    def test_repeated_values_and_validation(self):
        self.assertEqual(three_sum([0] * 7), [(0,) * 3])
        self.assertEqual(three_sum([]), [])
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                three_sum([bad])
            with self.assertRaises(ValueError):
                three_sum([], bad)

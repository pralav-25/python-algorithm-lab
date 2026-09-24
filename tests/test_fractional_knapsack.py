import itertools
import random
import unittest
from fractions import Fraction

from algorithm_lab.fractional_knapsack import fractional_knapsack


class FractionalTests(unittest.TestCase):
    def test_extreme_point_oracle(self):
        rng = random.Random(158)
        for _ in range(150):
            n = rng.randrange(7)
            items = [(rng.randrange(1, 8), rng.randrange(12)) for _ in range(n)]
            capacity = rng.randrange(20)
            best = Fraction(0)
            for flags in itertools.product([0, 1], repeat=n):
                weight = sum(flag * w for flag, (w, _) in zip(flags, items, strict=True))
                if weight > capacity:
                    continue
                value = sum(flag * v for flag, (_, v) in zip(flags, items, strict=True))
                best = max(best, value)
                for i, (w, v) in enumerate(items):
                    if not flags[i]:
                        best = max(best, value + Fraction(min(capacity - weight, w), w) * v)
            value, fractions = fractional_knapsack(iter(items), capacity)
            self.assertEqual(value, best)
            self.assertEqual(
                sum(f * w for f, (w, _) in zip(fractions, items, strict=True)) <= capacity, True
            )
            self.assertTrue(all(0 <= f <= 1 for f in fractions))
            self.assertEqual(value, sum(f * v for f, (_, v) in zip(fractions, items, strict=True)))

    def test_invalid_and_ties(self):
        self.assertEqual(fractional_knapsack([(2, 2), (2, 2)], 3)[1], [Fraction(1), Fraction(1, 2)])
        for items, capacity in [
            ([(0, 1)], 1),
            ([(1, -1)], 1),
            ([(True, 1)], 1),
            ([], -1),
            ([], True),
        ]:
            with self.assertRaises(ValueError):
                fractional_knapsack(items, capacity)

import random
import unittest
from itertools import product

from algorithm_lab.bounded_knapsack import bounded_knapsack


class Tests(unittest.TestCase):
    def test_quantity_enumeration(self):
        rng = random.Random(234)
        for _ in range(100):
            items = [
                (rng.randrange(1, 5), rng.randrange(-3, 9), rng.randrange(4)) for _ in range(4)
            ]
            capacity = rng.randrange(15)
            expected = max(
                sum(k * v for k, (_, v, _) in zip(counts, items, strict=True))
                for counts in product(*(range(c + 1) for _, _, c in items))
                if sum(k * w for k, (w, _, _) in zip(counts, items, strict=True)) <= capacity
            )
            self.assertEqual(bounded_knapsack(items, capacity), expected)

    def test_invalid(self):
        for items, capacity in [([(0, 1, 1)], 2), ([(1, 2, -1)], 2), ([(1, True, 1)], 2), ([], -1)]:
            with self.assertRaises(ValueError):
                bounded_knapsack(items, capacity)

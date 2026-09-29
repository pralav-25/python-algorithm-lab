import random
import unittest
from itertools import product

from algorithm_lab.bounded_knapsack import bounded_knapsack


class Tests(unittest.TestCase):
    def test_binary_group_remainders_match_quantity_oracle(self):
        for count in [4, 5, 6, 7, 8, 9, 15, 16, 17]:
            items = [(3, 5, count), (4, 9, 2)]
            for capacity in range(3 * count + 10):
                expected = max(
                    5 * a + 9 * b
                    for a in range(count + 1)
                    for b in range(3)
                    if 3 * a + 4 * b <= capacity
                )
                self.assertEqual(bounded_knapsack(iter(items), capacity), expected)

    def test_huge_quantity_is_capped_without_losing_exact_values(self):
        value = 10**100
        items = [(3, value, 10**100), (1, -value, 10**100), (2, value * 100, 0)]
        original = items[:]
        self.assertEqual(bounded_knapsack(items, 17), 5 * value)
        self.assertEqual(items, original)

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

import random
import unittest

from algorithm_lab.knapsack import knapsack


class KnapsackTests(unittest.TestCase):
    def test_subset_oracle_and_reconstruction(self):
        rng = random.Random(9)
        for _ in range(80):
            weights = [rng.randrange(6) for _ in range(8)]
            values = [rng.randrange(-3, 10) for _ in range(8)]
            capacity = rng.randrange(15)
            candidates = [
                sum(values[i] for i in range(8) if mask & (1 << i))
                for mask in range(256)
                if sum(weights[i] for i in range(8) if mask & (1 << i)) <= capacity
            ]
            total, selected = knapsack(weights, values, capacity)
            self.assertEqual(total, max(candidates))
            self.assertEqual(total, sum(values[i] for i in selected))
            self.assertLessEqual(sum(weights[i] for i in selected), capacity)
            self.assertEqual(len(selected), len(set(selected)))

    def test_zero_weight_ties_and_validation(self):
        self.assertEqual(knapsack([0, 0], [3, -1], 0), (3, [0]))
        self.assertEqual(knapsack([1, 1], [2, 2], 1), (2, [0]))
        self.assertEqual(knapsack([], [], 0), (0, []))
        for weights, values, capacity in [
            ([1], [], 2),
            ([-1], [1], 2),
            ([1], [True], 2),
            ([1], [1], -1),
            ([True], [1], 2),
        ]:
            with self.assertRaises(ValueError):
                knapsack(weights, values, capacity)

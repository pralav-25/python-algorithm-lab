import itertools
import random
import unittest

from algorithm_lab.unbounded_knapsack import unbounded_knapsack


class Tests(unittest.TestCase):
    def test_quantity_enumeration(self):
        rng = random.Random(327)
        for size in range(4):
            for _ in range(15):
                weights = [rng.randrange(1, 5) for _ in range(size)]
                values = [rng.randrange(6) for _ in range(size)]
                original = weights[:], values[:]
                for capacity in range(9):
                    expected = max(
                        sum(count * value for count, value in zip(counts, values, strict=True))
                        for counts in itertools.product(
                            *(range(capacity // weight + 1) for weight in weights)
                        )
                        if sum(
                            count * weight for count, weight in zip(counts, weights, strict=True)
                        )
                        <= capacity
                    )
                    self.assertEqual(
                        unbounded_knapsack(iter(weights), iter(values), capacity), expected
                    )
                    self.assertEqual((weights, values), original)

    def test_duplicates_and_invalid(self):
        self.assertEqual(unbounded_knapsack([2, 2], [3, 3], 7), 9)
        for args in [
            ([0], [1], 0),
            ([True], [1], 0),
            ([1], [False], 0),
            ([1], [-1], 2),
            ([1.5], [2], 2),
            ([1], [2.0], 2),
            ([1], [], 0),
            ([], [], True),
            ([], [], -1),
        ]:
            with self.assertRaises(ValueError):
                unbounded_knapsack(*args)

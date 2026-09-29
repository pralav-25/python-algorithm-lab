import unittest
from itertools import product

from algorithm_lab.coin_change_count import coin_change_count


class Tests(unittest.TestCase):
    def test_scaled_denominations_and_duplicate_generator(self):
        coins = [1, 3, 4]
        original = coins[:]
        for target in range(20):
            expected = sum(
                1
                for a in range(target + 1)
                for b in range(target // 3 + 1)
                if target - a - 3 * b >= 0 and (target - a - 3 * b) % 4 == 0
            )
            self.assertEqual(coin_change_count(iter([4, 1, 3, 1, 4]), target), expected)
            self.assertEqual(coin_change_count([7 * c for c in coins], 7 * target), expected)
            self.assertEqual(coin_change_count([7 * c for c in coins], 7 * target + 1), 0)
        self.assertEqual(coins, original)

    def test_zero_target_still_validates_every_coin(self):
        for coins in [[0], [-1], [1, True], [1, 1.5]]:
            with self.assertRaises(ValueError):
                coin_change_count(iter(coins), 0)

    def test_quantity_enumeration(self):
        for coins in [[], [2], [1, 3], [2, 3, 5], [1, 1, 2]]:
            unique = sorted(set(coins))
            for target in range(16):
                expected = sum(
                    sum(c * k for c, k in zip(unique, counts, strict=True)) == target
                    for counts in product(*(range(target // c + 1) for c in unique))
                )
                self.assertEqual(coin_change_count(coins, target), expected)

    def test_invalid(self):
        for coins, target in [([0], 1), ([True], 1), ([2], -1), ([2], False)]:
            with self.assertRaises(ValueError):
                coin_change_count(coins, target)

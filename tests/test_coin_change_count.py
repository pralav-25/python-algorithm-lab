import unittest
from itertools import product

from algorithm_lab.coin_change_count import coin_change_count


class Tests(unittest.TestCase):
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

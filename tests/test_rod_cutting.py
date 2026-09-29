import random
import unittest

from algorithm_lab.rod_cutting import rod_cutting


class Tests(unittest.TestCase):
    def test_negative_revenues_and_smallest_cut_ties(self):
        for prices, expected in [
            ([-4, -9, -15], (-12, [1, 1, 1])),
            ([-5, -6, -7], (-7, [3])),
            ([2, 4, 6, 8], (8, [1, 1, 1, 1])),
            ([0, 0, 0, 0], (0, [1, 1, 1, 1])),
            ([10**100, 2 * 10**100, 3 * 10**100], (3 * 10**100, [1, 1, 1])),
        ]:
            original = prices[:]
            with self.subTest(prices=prices):
                self.assertEqual(rod_cutting(iter(prices)), expected)
                self.assertEqual(rod_cutting(prices), expected)
                self.assertEqual(prices, original)

    def test_cut_mask_oracle(self):
        rng = random.Random(235)
        self.assertEqual(rod_cutting([]), (0, []))
        for n in range(1, 9):
            prices = [rng.randrange(-5, 11) for _ in range(n)]
            revenues = []
            for mask in range(1 << (n - 1)):
                ends = [0] + [i for i in range(1, n) if mask >> (i - 1) & 1] + [n]
                revenues.append(
                    sum(prices[b - a - 1] for a, b in zip(ends, ends[1:], strict=False))
                )
            revenue, pieces = rod_cutting(prices)
            self.assertEqual(revenue, max(revenues))
            self.assertEqual(sum(pieces), n)
            self.assertEqual(sum(prices[size - 1] for size in pieces), revenue)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            rod_cutting([True])

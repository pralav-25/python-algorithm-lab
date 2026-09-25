import random
import unittest

from algorithm_lab.rod_cutting import rod_cutting


class Tests(unittest.TestCase):
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

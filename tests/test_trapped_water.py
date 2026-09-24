import itertools
import unittest

from algorithm_lab.trapped_water import trapped_water


class WaterTests(unittest.TestCase):
    def test_exhaustive(self):
        for n in range(7):
            for heights in itertools.product(range(3), repeat=n):
                expected = sum(
                    min(max(heights[: i + 1]), max(heights[i:])) - h for i, h in enumerate(heights)
                )
                self.assertEqual(trapped_water(heights), expected)

    def test_invalid(self):
        for heights in [[-2], [False], [0.5]]:
            with self.assertRaises(ValueError):
                trapped_water(heights)

import random
import unittest

from algorithm_lab.rectangle_union_area import rectangle_union_area


class Tests(unittest.TestCase):
    def test_unit_cell_oracle(self):
        rng = random.Random(426)
        for _ in range(200):
            rectangles, cells = [], set()
            for _ in range(rng.randrange(10)):
                a, c = sorted(rng.sample(range(-5, 6), 2))
                b, d = sorted(rng.sample(range(-5, 6), 2))
                rectangles.append((a, b, c, d))
                cells.update((x, y) for x in range(a, c) for y in range(b, d))
            self.assertEqual(rectangle_union_area(iter(rectangles)), len(cells))

    def test_duplicates_exactness_and_invalid(self):
        n = 10**100
        self.assertEqual(rectangle_union_area([(0, 0, n, n)] * 2), n * n)
        for rectangle in [(0, 0, 0, 1), (2, 0, 1, 1), (0, 1, 1, 0), (False, 0, 1, 1)]:
            with self.assertRaises(ValueError):
                rectangle_union_area([rectangle])

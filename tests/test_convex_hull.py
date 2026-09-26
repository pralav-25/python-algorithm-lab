import itertools
import unittest

from algorithm_lab.convex_hull import convex_hull


class Tests(unittest.TestCase):
    def test_grid_subsets_against_supporting_edges(self):
        grid = list(itertools.product(range(3), repeat=2))
        for mask in range(1 << len(grid)):
            points = [p for i, p in enumerate(grid) if mask & (1 << i)]
            hull = convex_hull(iter(points + points))
            if len(hull) < 3:
                self.assertEqual(
                    hull, sorted(set(points))[:1] if len(points) < 2 else [min(points), max(points)]
                )
                continue
            self.assertEqual(hull[0], min(points))
            self.assertEqual(len(hull), len(set(hull)))
            for i, a in enumerate(hull):
                b, c = hull[(i + 1) % len(hull)], hull[(i + 2) % len(hull)]
                self.assertGreater((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]), 0)
                for p in points:
                    self.assertGreaterEqual(
                        (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]), 0
                    )

    def test_large_coordinates_and_invalid(self):
        n = 10**100
        self.assertEqual(convex_hull([(0, 0), (n, n), (2 * n, 2 * n)]), [(0, 0), (2 * n, 2 * n)])
        for value in [True, 1.0, "1"]:
            with self.assertRaises(ValueError):
                convex_hull([(value, 0)])

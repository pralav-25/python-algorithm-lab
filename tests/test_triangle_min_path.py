import random
import unittest
from itertools import product

from algorithm_lab.triangle_min_path import triangle_min_path


class Tests(unittest.TestCase):
    def test_tie_paths_prefer_left_at_every_row(self):
        rows = [[5], [2, 2], [-3, -3, -3], [8, 8, 8, 8]]
        original = [row[:] for row in rows]
        self.assertEqual(triangle_min_path(iter(iter(row) for row in rows)), (12, [0, 0, 0, 0]))
        score, path = triangle_min_path(rows)
        path[0] = 99
        self.assertEqual(score, 12)
        self.assertEqual(rows, original)

    def test_large_signed_costs_preserve_exact_path(self):
        huge = 10**100
        rows = [[huge], [huge, -huge], [huge, huge, -huge], [huge, huge, huge, -huge]]
        self.assertEqual(triangle_min_path(rows), (-2 * huge, [0, 1, 2, 3]))

    def test_path_enumeration(self):
        rng = random.Random(238)
        self.assertEqual(triangle_min_path([]), (0, []))
        for n in range(1, 10):
            rows = [[rng.randrange(-5, 8) for _ in range(i + 1)] for i in range(n)]
            totals = []
            for steps in product(range(2), repeat=n - 1):
                column, total = 0, rows[0][0]
                for i, step in enumerate(steps, 1):
                    column += step
                    total += rows[i][column]
                totals.append(total)
            score, path = triangle_min_path(rows)
            self.assertEqual(score, min(totals))
            self.assertEqual(sum(rows[i][j] for i, j in enumerate(path)), score)

    def test_invalid(self):
        for rows in [[[]], [[1], [2]], [[True]]]:
            with self.assertRaises(ValueError):
                triangle_min_path(rows)

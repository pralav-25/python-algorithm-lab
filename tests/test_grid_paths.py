import math
import unittest

from algorithm_lab.grid_paths import grid_paths


def paths(grid, row=0, column=0):
    if row >= len(grid) or column >= len(grid[0]) or grid[row][column]:
        return 0
    if row == len(grid) - 1 and column == len(grid[0]) - 1:
        return 1
    return paths(grid, row + 1, column) + paths(grid, row, column + 1)


class GridPathTests(unittest.TestCase):
    def test_every_small_obstacle_layout(self):
        for mask in range(512):
            grid = [[int(bool(mask & (1 << (r * 3 + c)))) for c in range(3)] for r in range(3)]
            self.assertEqual(grid_paths(grid), paths(grid))

    def test_exact_large_combinatorial_count(self):
        self.assertEqual(grid_paths([[0] * 35 for _ in range(40)]), math.comb(73, 34))
        self.assertEqual(grid_paths([[0]]), 1)
        self.assertEqual(grid_paths([]), 0)
        self.assertEqual(grid_paths([[], []]), 0)
        for grid in [[[0], []], [[2]], [[0.0]]]:
            with self.assertRaises(ValueError):
                grid_paths(grid)

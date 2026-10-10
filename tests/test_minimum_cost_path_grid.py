import itertools
import random
import unittest

from algorithm_lab.minimum_cost_path_grid import minimum_cost_path_grid


class Tests(unittest.TestCase):
    @staticmethod
    def path_oracle(grid):
        rows, columns = len(grid), len(grid[0])
        scores = []
        for downs in itertools.combinations(range(rows + columns - 2), rows - 1):
            downs = set(downs)
            row = column = 0
            cost = grid[0][0]
            for step in range(rows + columns - 2):
                if step in downs:
                    row += 1
                else:
                    column += 1
                cost += grid[row][column]
            scores.append(cost)
        return min(scores)

    def test_all_monotone_paths_with_negative_costs(self):
        rng = random.Random(618)
        self.assertEqual(minimum_cost_path_grid([]), 0)
        for rows, columns in itertools.product(range(1, 5), repeat=2):
            for _ in range(8):
                grid = [[rng.randrange(-5, 6) for _ in range(columns)] for _ in range(rows)]
                original = [row[:] for row in grid]
                self.assertEqual(
                    minimum_cost_path_grid(iter(map(iter, grid))), self.path_oracle(grid)
                )
                self.assertEqual(grid, original)

    def test_invalid(self):
        for grid in [[[]], [[], []], [[1], [1, 2]], [[True]], [[1.5]], [[1, None]]]:
            with self.assertRaises(ValueError):
                minimum_cost_path_grid(grid)

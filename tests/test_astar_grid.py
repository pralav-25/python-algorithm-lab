import random
import unittest
from collections import deque

from algorithm_lab.astar_grid import astar_grid


class AStarTests(unittest.TestCase):
    def test_breadth_first_distance_oracle(self):
        rng = random.Random(71)
        for _ in range(100):
            grid = [[int(rng.random() < 0.3) for _ in range(6)] for _ in range(5)]
            grid[0][0] = grid[4][5] = 0
            queue, distances = deque([(0, 0)]), {(0, 0): 0}
            while queue:
                r, c = queue.popleft()
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if (
                        0 <= nr < 5
                        and 0 <= nc < 6
                        and not grid[nr][nc]
                        and (nr, nc) not in distances
                    ):
                        distances[nr, nc] = distances[r, c] + 1
                        queue.append((nr, nc))
            result = astar_grid(grid, (0, 0), (4, 5))
            if (4, 5) not in distances:
                self.assertIsNone(result)
            else:
                self.assertEqual(len(result) - 1, distances[4, 5])
                self.assertEqual((result[0], result[-1]), ((0, 0), (4, 5)))
                self.assertTrue(all(not grid[r][c] for r, c in result))
                self.assertTrue(
                    all(
                        abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1
                        for a, b in zip(result, result[1:], strict=False)
                    )
                )

    def test_blocked_same_and_invalid_inputs(self):
        self.assertIsNone(astar_grid([[1]], (0, 0), (0, 0)))
        self.assertEqual(astar_grid([[0]], (0, 0), (0, 0)), [(0, 0)])
        for grid in [[], [[]], [[0], [0, 0]], [[2]], [[0.0]]]:
            with self.assertRaises(ValueError):
                astar_grid(grid, (0, 0), (0, 0))
        with self.assertRaises(ValueError):
            astar_grid([[0]], (-1, 0), (0, 0))

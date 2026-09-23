import itertools
import math
import random
import unittest

from algorithm_lab.floyd_warshall import floyd_warshall


class FloydWarshallTests(unittest.TestCase):
    def test_simple_path_oracle(self):
        rng = random.Random(51)
        for _ in range(20):
            matrix = [
                [
                    0 if i == j else rng.randrange(8) if rng.random() < 0.5 else math.inf
                    for j in range(4)
                ]
                for i in range(4)
            ]
            before = [row[:] for row in matrix]
            result = floyd_warshall(matrix)
            for start in range(4):
                for end in range(4):
                    others = [v for v in range(4) if v not in (start, end)]
                    costs = [0] if start == end else []
                    for size in range(len(others) + 1):
                        for middle in itertools.permutations(others, size):
                            costs.append(
                                sum(
                                    matrix[a][b]
                                    for a, b in itertools.pairwise((start, *middle, end))
                                )
                            )
                    self.assertEqual(result[start][end], min(costs))
            self.assertEqual(matrix, before)

    def test_invalid_negative_cycles_and_empty(self):
        for matrix in [[[0, -2], [1, 0]], [[-1]], [[0, 1]], [[math.nan]], [[-math.inf]], [[True]]]:
            with self.assertRaises(ValueError):
                floyd_warshall(matrix)
        self.assertEqual(floyd_warshall([]), [])
        self.assertEqual(floyd_warshall([[7]]), [[0]])

import itertools
import math
import random
import unittest

from algorithm_lab.dijkstra import dijkstra


class DijkstraTests(unittest.TestCase):
    def test_simple_path_oracle(self):
        rng = random.Random(8)
        for _ in range(40):
            graph = {
                i: [(j, rng.randrange(6)) for j in range(5) if rng.random() < 0.3] for i in range(5)
            }
            weights = {(a, b): w for a, rows in graph.items() for b, w in rows}
            costs = []
            for count in range(4):
                for middle in itertools.permutations([1, 2, 3], count):
                    edges = list(itertools.pairwise((0, *middle, 4)))
                    if all(edge in weights for edge in edges):
                        costs.append(sum(weights[edge] for edge in edges))
            self.assertEqual(dijkstra(graph, 0)[4], min(costs, default=math.inf))

    def test_mixed_labels_zero_weights_and_large_integers(self):
        distances = dijkstra({None: [("x", 0), (1, 0)], "x": [(1, 0)], "z": []}, None)
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances["z"], math.inf)
        self.assertEqual(dijkstra({0: [(1, 10**100)]}, 0)[1], 10**100)

    def test_invalid_and_overflowing_weights(self):
        for weight in [-1, math.inf, math.nan, True]:
            with self.assertRaises(ValueError):
                dijkstra({"disconnected": [("leaf", weight)]}, "source")
        with self.assertRaises(ValueError):
            dijkstra({0: [(1, 1e308)], 1: [(2, 1e308)]}, 0)

import random
import unittest
from collections import Counter

from algorithm_lab.eulerian_trail import eulerian_trail


class EulerTests(unittest.TestCase):
    def test_generated_walks(self):
        rng = random.Random(142)
        for _ in range(200):
            walk = [rng.randrange(6) for _ in range(rng.randrange(2, 35))]
            graph = {v: [] for v in range(7)}
            edges = list(zip(walk, walk[1:], strict=False))
            for a, b in edges:
                graph[a].append(b)
            before = {v: rows[:] for v, rows in graph.items()}
            trail = eulerian_trail(graph)
            self.assertEqual(Counter(zip(trail, trail[1:], strict=False)), Counter(edges))
            self.assertEqual(graph, before)

    def test_invalid_and_empty(self):
        for graph in [{0: [1, 2]}, {0: [0], 1: [1]}, {0: [1], 2: [3]}]:
            with self.assertRaises(ValueError):
                eulerian_trail(graph)
        self.assertEqual(eulerian_trail({None: []}), [])
        self.assertEqual(eulerian_trail({None: [None]}), [None, None])

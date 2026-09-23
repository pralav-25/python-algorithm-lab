import math
import random
import unittest

from algorithm_lab.bellman_ford import bellman_ford


class BellmanFordTests(unittest.TestCase):
    def test_negative_dags_against_forward_relaxation(self):
        rng = random.Random(32)
        for _ in range(100):
            graph = {
                i: [(j, rng.randrange(-8, 9)) for j in range(i + 1, 10) if rng.random() < 0.35]
                for i in range(10)
            }
            expected = dict.fromkeys(graph, math.inf)
            expected[0] = 0
            for node in range(10):
                for child, weight in graph[node]:
                    expected[child] = min(expected[child], expected[node] + weight)
            self.assertEqual(bellman_ford(graph, 0), expected)

    def test_reachable_and_unreachable_cycles(self):
        graph = {0: [(1, 1)], 1: [(0, -2)], 2: []}
        with self.assertRaises(ValueError):
            bellman_ford(graph, 0)
        self.assertEqual(bellman_ford(graph, 2), {0: math.inf, 1: math.inf, 2: 0})
        with self.assertRaises(ValueError):
            bellman_ford({0: [(0, -1)]}, 0)

    def test_missing_source_and_bad_weights(self):
        self.assertEqual(bellman_ford({}, "alone"), {"alone": 0})
        with self.assertRaises(ValueError):
            bellman_ford({1: [(2, math.nan)]}, 0)
        with self.assertRaises(ValueError):
            bellman_ford({0: [(1, 10**1000)], 1: [(2, 1.0)]}, 0)

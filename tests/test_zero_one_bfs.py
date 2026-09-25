import random
import unittest

from algorithm_lab.zero_one_bfs import zero_one_bfs


class Tests(unittest.TestCase):
    def test_repeated_relaxation_oracle(self):
        rng = random.Random(249)
        for n in range(1, 10):
            for _ in range(20):
                graph = {
                    i: [(j, rng.randrange(2)) for j in range(n) if rng.random() < 0.2]
                    for i in range(n)
                }
                expected = {0: 0}
                for _ in range(n):
                    for i, edges in graph.items():
                        if i in expected:
                            for j, w in edges:
                                expected[j] = min(expected.get(j, n + 1), expected[i] + w)
                self.assertEqual(zero_one_bfs(graph, 0), expected)
        self.assertEqual(zero_one_bfs({"a": iter([("b", 0)])}, "a"), {"a": 0, "b": 0})

    def test_invalid_unreachable_edge(self):
        for weight in [-1, 2, True, 0.0]:
            with self.assertRaises(ValueError):
                zero_one_bfs({"unreachable": [("x", weight)]}, "start")

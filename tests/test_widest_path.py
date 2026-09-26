import math
import random
import unittest

from algorithm_lab.widest_path import widest_path


class Tests(unittest.TestCase):
    def test_exhaustive_simple_path_oracle(self):
        rng = random.Random(428)
        for _ in range(100):
            graph = {
                i: [(j, rng.randrange(6)) for j in range(5) if rng.random() < 0.3] for i in range(5)
            }
            expected = dict.fromkeys(graph, -1)

            def visit(node, capacity, seen, graph=graph, expected=expected):
                expected[node] = max(expected[node], capacity)
                for neighbor, weight in graph[node]:
                    if neighbor not in seen:
                        visit(neighbor, min(capacity, weight), seen | {neighbor})

            visit(0, math.inf, {0})
            self.assertEqual(widest_path(graph, 0), expected)

    def test_mixed_labels_zero_weights_and_invalid(self):
        graph = {None: [("x", 0), (1, 0)], "lost": []}
        self.assertEqual(widest_path(graph, None), {None: math.inf, "x": 0, 1: 0, "lost": -1})
        for value in [-1, True, float("inf"), float("nan")]:
            with self.assertRaises(ValueError):
                widest_path({"other": [("lost", value)]}, "source")

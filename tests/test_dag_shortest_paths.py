import random
import unittest

from algorithm_lab.dag_shortest_paths import dag_shortest_paths


class DAGTests(unittest.TestCase):
    def test_bellman_relaxation_oracle(self):
        rng = random.Random(143)
        for _ in range(150):
            n = rng.randrange(1, 12)
            graph = {
                i: {j: rng.randrange(-9, 10) for j in range(i + 1, n) if rng.randrange(3) == 0}
                for i in range(n)
            }
            source = rng.randrange(n)
            distance = {source: 0}
            for _ in range(n):
                for a, neighbors in graph.items():
                    for b, weight in neighbors.items():
                        if a in distance:
                            distance[b] = min(distance.get(b, float("inf")), distance[a] + weight)
            self.assertEqual(dag_shortest_paths(graph, source), distance)

    def test_validation_and_neighbor_only(self):
        self.assertEqual(
            dag_shortest_paths({None: {"x": -(10**100)}}, None), {None: 0, "x": -(10**100)}
        )
        for graph, source in [({}, 0), ({0: {}, 1: {1: 1}}, 0), ({0: {1: True}}, 0)]:
            with self.assertRaises(ValueError):
                dag_shortest_paths(graph, source)

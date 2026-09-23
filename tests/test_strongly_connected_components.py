import random
import unittest

from algorithm_lab.strongly_connected_components import strongly_connected_components as scc


class SCCTests(unittest.TestCase):
    def test_transitive_closure_oracle(self):
        rng = random.Random(7)
        for _ in range(100):
            graph = {i: [j for j in range(7) if rng.random() < 0.2] for i in range(7)}
            reach = [[i == j or j in graph[i] for j in range(7)] for i in range(7)]
            for k in range(7):
                for i in range(7):
                    for j in range(7):
                        reach[i][j] |= reach[i][k] and reach[k][j]
            expected = {
                frozenset(j for j in range(7) if reach[i][j] and reach[j][i]) for i in range(7)
            }
            self.assertEqual(set(scc(graph)), expected)

    def test_deep_graph_and_neighbor_only_nodes(self):
        self.assertEqual(
            set(scc({i: [i + 1] for i in range(1500)})), {frozenset({i}) for i in range(1501)}
        )
        self.assertEqual(scc({}), [])
        self.assertEqual(scc({None: [None]}), [frozenset({None})])

import random
import unittest

from algorithm_lab.max_flow import max_flow


class FlowTests(unittest.TestCase):
    def test_exhaustive_cut_oracle(self):
        rng = random.Random(144)
        for n in range(2, 8):
            for _ in range(50):
                graph = {
                    a: {b: rng.randrange(5) for b in range(n) if rng.randrange(3) == 0}
                    for a in range(n)
                }

                def cut_capacity(side, graph=graph):
                    return sum(c for a in side for b, c in graph[a].items() if b not in side)

                cuts = [
                    {0} | {i + 1 for i in range(n - 2) if mask & (1 << i)}
                    for mask in range(1 << (n - 2))
                ]
                expected = min(map(cut_capacity, cuts))
                before = {v: rows.copy() for v, rows in graph.items()}
                flow, cut = max_flow(graph, 0, n - 1)
                self.assertEqual(flow, expected)
                self.assertEqual(cut_capacity(cut), flow)
                self.assertIn(0, cut)
                self.assertNotIn(n - 1, cut)
                self.assertEqual(graph, before)

    def test_validation_and_labels(self):
        self.assertEqual(max_flow({None: {"t": 10**100}}, None, "t"), (10**100, frozenset([None])))
        for graph, source, sink in [
            ({}, 0, 1),
            ({0: {1: 1}}, 0, 0),
            ({0: {1: -1}}, 0, 1),
            ({0: {1: True}}, 0, 1),
        ]:
            with self.assertRaises(ValueError):
                max_flow(graph, source, sink)

    def test_residual_reverse_edge_reroutes_an_earlier_augmentation(self):
        # First path is s-a-x-t; reaching value 2 requires undoing a-x.
        for unit in (1, 10**100):
            graph = {
                "s": {"a": unit, "b": unit},
                "a": {"x": unit, "y": unit},
                "b": {"x": unit},
                "x": {"t": unit},
                "y": {"t": unit},
            }
            before = {node: rows.copy() for node, rows in graph.items()}
            value, cut = max_flow(graph, "s", "t")
            self.assertEqual(value, 2 * unit)
            self.assertEqual(cut, {"s"})
            self.assertEqual(graph, before)

    def test_zero_capacity_neighbor_only_sink_and_isolated_components(self):
        graph = {None: {"t": 0, "a": 4}, "a": {None: 3}, "island": {"island": 9}}
        self.assertEqual(max_flow(graph, None, "t"), (0, frozenset([None, "a"])))

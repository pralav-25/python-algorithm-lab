import random
import unittest

from algorithm_lab.topological_sort import topological_sort


class TopologicalTests(unittest.TestCase):
    def test_seeded_dags_respect_every_edge(self):
        rng = random.Random(8)
        for _ in range(100):
            ordering = list(range(12))
            rng.shuffle(ordering)
            graph = {
                node: [other for other in ordering[i + 1 :] if rng.random() < 0.3]
                for i, node in enumerate(ordering)
            }
            result = topological_sort(graph)
            self.assertEqual(set(result), set(ordering))
            positions = {node: i for i, node in enumerate(result)}
            self.assertTrue(
                all(
                    positions[node] < positions[child]
                    for node, children in graph.items()
                    for child in children
                )
            )

    def test_cycles_duplicates_and_mixed_labels(self):
        for graph in [{0: [0]}, {0: [1], 1: [0]}, {"ok": [], "a": ["b"], "b": ["a"]}]:
            with self.assertRaises(ValueError):
                topological_sort(graph)
        self.assertEqual(topological_sort({None: ["x", "x"], 1: []}), [None, 1, "x"])
        self.assertEqual(topological_sort({}), [])

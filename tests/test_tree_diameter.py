import random
import unittest
from collections import deque

from algorithm_lab.tree_diameter import tree_diameter


class DiameterTests(unittest.TestCase):
    def test_all_pairs_distance_oracle(self):
        rng = random.Random(147)
        for n in range(1, 45):
            graph = {i: [] for i in range(n)}
            for node in range(1, n):
                parent = rng.randrange(node)
                graph[parent].append(node)
                graph[node].append(parent)
            maximum = 0
            for source in graph:
                distance, queue = {source: 0}, deque([source])
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in distance:
                            distance[neighbor] = distance[node] + 1
                            queue.append(neighbor)
                maximum = max(maximum, max(distance.values()))
            path = tree_diameter(graph)
            self.assertEqual(len(path) - 1, maximum)
            self.assertTrue(all(b in graph[a] for a, b in zip(path, path[1:], strict=False)))
            self.assertEqual(len(path), len(set(path)))

    def test_validation(self):
        for graph in [{0: [0]}, {0: [], 1: []}, {0: [1, 2], 1: [2]}, {0: [1, 2], 1: [2], 3: []}]:
            with self.assertRaises(ValueError):
                tree_diameter(graph)
        self.assertEqual(tree_diameter({}), [])
        self.assertEqual(tree_diameter({None: []}), [None])

    def test_deep_asymmetric_chain_with_duplicate_edges(self):
        size = 3000
        graph = {i: [i + 1, i + 1] for i in range(size)}
        self.assertEqual(tree_diameter(graph), list(range(size, -1, -1)))
        self.assertEqual(graph[0], [1, 1])
        self.assertEqual(graph[size - 1], [size, size])

    def test_mixed_labels_and_neighbor_iterators(self):
        graph = {None: ["hub"], "hub": [1, ("leaf",)], 1: ["end"]}
        before = {node: rows[:] for node, rows in graph.items()}
        path = tree_diameter({node: iter(rows) for node, rows in graph.items()})
        edges = {frozenset((a, b)) for a, rows in graph.items() for b in rows}
        self.assertEqual(len(path), 4)
        self.assertEqual(len(set(path)), 4)
        self.assertTrue(
            all(frozenset((a, b)) in edges for a, b in zip(path, path[1:], strict=False))
        )
        self.assertEqual(graph, before)

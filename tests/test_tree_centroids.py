import random
import unittest

from algorithm_lab.tree_centroids import tree_centroids


class Tests(unittest.TestCase):
    def test_removal_component_oracle(self):
        rng = random.Random(429)
        for n in range(1, 40):
            graph = {v: [] for v in range(n)}
            for v in range(1, n):
                parent = rng.randrange(v)
                graph[v].append(parent)
                graph[parent].append(v)
            expected = []
            for removed in graph:
                seen, sizes = {removed}, []
                for start in graph:
                    if start in seen:
                        continue
                    queue = [start]
                    seen.add(start)
                    for node in queue:
                        for neighbor in graph[node]:
                            if neighbor not in seen:
                                seen.add(neighbor)
                                queue.append(neighbor)
                    sizes.append(len(queue))
                if max(sizes, default=0) * 2 <= n:
                    expected.append(removed)
            self.assertEqual(tree_centroids(graph), expected)

    def test_validation_and_long_path(self):
        self.assertEqual(tree_centroids({}), [])
        self.assertEqual(tree_centroids({None: [1, 1]}), [None, 1])
        self.assertEqual(tree_centroids({i: [i + 1] for i in range(3000)}), [1500])
        for graph in [
            {0: [0]},
            {0: [], 1: []},
            {0: [1], 1: [2], 2: [0]},
            {0: [1, 2], 1: [2], 3: []},
        ]:
            with self.assertRaises(ValueError):
                tree_centroids(graph)

    def test_centroid_is_not_necessarily_a_diameter_midpoint(self):
        # Five leaves outweigh a long thin arm: the centroid remains the hub.
        graph = {
            "hub": ["a", "b", "c", "d", "e", 1],
            1: [2],
            2: [3],
            3: [4],
        }
        self.assertEqual(tree_centroids(graph), ["hub"])

    def test_two_centroids_follow_normalized_input_order(self):
        graph = {"right": ["left", 2, 2], "left": [None, None]}
        before = {node: rows[:] for node, rows in graph.items()}
        self.assertEqual(tree_centroids(graph), ["right", "left"])
        self.assertEqual(graph, before)
        self.assertEqual(
            tree_centroids({node: iter(rows) for node, rows in graph.items()}), ["right", "left"]
        )

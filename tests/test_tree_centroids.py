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

import itertools
import random
import unittest

from algorithm_lab.bfs_shortest_path import bfs_shortest_path


class BFSTests(unittest.TestCase):
    def test_brute_force_simple_paths(self):
        rng = random.Random(16)
        for _ in range(40):
            graph = {i: [j for j in range(5) if rng.random() < 0.25] for i in range(5)}
            lengths = []
            for size in range(4):
                for middle in itertools.permutations([1, 2, 3], size):
                    path = (0, *middle, 4)
                    if all(b in graph[a] for a, b in itertools.pairwise(path)):
                        lengths.append(len(path))
            result = bfs_shortest_path(graph, 0, 4)
            if not lengths:
                self.assertIsNone(result)
            else:
                self.assertEqual(len(result), min(lengths))
                self.assertTrue(all(b in graph[a] for a, b in itertools.pairwise(result)))

    def test_missing_none_and_neighbor_iterators(self):
        self.assertEqual(bfs_shortest_path({}, None, None), [None])
        self.assertEqual(bfs_shortest_path({None: iter(["x"])}, None, "x"), [None, "x"])
        self.assertIsNone(bfs_shortest_path({}, "x", "y"))

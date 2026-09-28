import itertools
import random
import unittest
from collections import Counter
from functools import cache

from algorithm_lab.eulerian_trail import eulerian_trail


class EulerTests(unittest.TestCase):
    def test_generated_walks(self):
        rng = random.Random(142)
        for _ in range(200):
            walk = [rng.randrange(6) for _ in range(rng.randrange(2, 35))]
            graph = {v: [] for v in range(7)}
            edges = list(zip(walk, walk[1:], strict=False))
            for a, b in edges:
                graph[a].append(b)
            before = {v: rows[:] for v, rows in graph.items()}
            trail = eulerian_trail(graph)
            self.assertEqual(Counter(zip(trail, trail[1:], strict=False)), Counter(edges))
            self.assertEqual(graph, before)

    def test_invalid_and_empty(self):
        for graph in [{0: [1, 2]}, {0: [0], 1: [1]}, {0: [1], 2: [3]}]:
            with self.assertRaises(ValueError):
                eulerian_trail(graph)
        self.assertEqual(eulerian_trail({None: []}), [])
        self.assertEqual(eulerian_trail({None: [None]}), [None, None])

    def test_every_two_vertex_multigraph_against_edge_walk_search(self):
        possible = list(itertools.product(range(2), repeat=2))
        for counts in itertools.product(range(3), repeat=len(possible)):
            graph = {0: [], 1: []}
            for (a, b), count in zip(possible, counts, strict=True):
                graph[a].extend([b] * count)

            @cache
            def can_finish(node, remaining):
                if not any(remaining):
                    return True
                for i, (a, b) in enumerate(possible):
                    if a == node and remaining[i]:
                        rest = list(remaining)
                        rest[i] -= 1
                        if can_finish(b, tuple(rest)):
                            return True
                return False

            possible_trail = any(can_finish(start, counts) for start in graph)
            with self.subTest(counts=counts):
                if possible_trail:
                    route = eulerian_trail(graph)
                    actual = Counter(zip(route, route[1:], strict=False))
                    expected = Counter({edge: n for edge, n in zip(possible, counts, strict=True)})
                    self.assertEqual(actual, expected)
                    self.assertEqual(len(route), sum(counts) + 1 if any(counts) else 0)
                else:
                    with self.assertRaises(ValueError):
                        eulerian_trail(graph)

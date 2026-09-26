import random
import unittest

from algorithm_lab.multi_source_bfs import multi_source_bfs


class Tests(unittest.TestCase):
    def test_against_distance_matrix(self):
        rng = random.Random(427)
        for _ in range(100):
            n = 6
            graph = {i: [j for j in range(n) if rng.random() < 0.2] for i in range(n)}
            sources = rng.sample(range(n), rng.randrange(n + 1))
            distance = [
                [0 if i == j else 1 if j in graph[i] else 100 for j in range(n)] for i in range(n)
            ]
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
            expected = (
                {j: min(distance[i][j] for i in sources) for j in range(n)} if sources else {}
            )
            expected = {j: d for j, d in expected.items() if d < 100}
            self.assertEqual(multi_source_bfs(graph, sources), expected)

    def test_iterators_and_isolated_sources(self):
        self.assertEqual(
            multi_source_bfs({"a": iter([None])}, ["a", "a", 3]), {"a": 0, 3: 0, None: 1}
        )
        self.assertEqual(multi_source_bfs({}, []), {})

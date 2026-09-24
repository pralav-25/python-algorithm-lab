import itertools
import unittest

from algorithm_lab.articulation_points import articulation_points


class ArticulationTests(unittest.TestCase):
    def test_vertex_removal_oracle(self):
        vertices = set(range(5))
        possible = list(itertools.combinations(sorted(vertices), 2))

        def count(nodes, edges):
            remaining, result = set(nodes), 0
            while remaining:
                stack = [remaining.pop()]
                result += 1
                while stack:
                    node = stack.pop()
                    for a, b in edges:
                        neighbor = b if a == node else a if b == node else None
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            stack.append(neighbor)
            return result

        for mask in range(1 << len(possible)):
            edges = [e for i, e in enumerate(possible) if mask & (1 << i)]
            graph = {v: [] for v in vertices}
            for a, b in edges:
                graph[a].append(b)
            expected = {
                v
                for v in vertices
                if count(vertices - {v}, [e for e in edges if v not in e]) > count(vertices, edges)
            }
            self.assertEqual(articulation_points(graph), expected)

    def test_long_chain(self):
        self.assertEqual(
            articulation_points({i: [i + 1] for i in range(2000)}), set(range(1, 2000))
        )
        self.assertEqual(articulation_points({None: ["a", "b"]}), {None})

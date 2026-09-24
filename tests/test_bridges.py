import itertools
import unittest

from algorithm_lab.bridges import bridges


class BridgeTests(unittest.TestCase):
    def test_edge_removal_oracle(self):
        vertices = range(5)
        possible = list(itertools.combinations(vertices, 2))

        def components(edges):
            remaining, count = set(vertices), 0
            while remaining:
                stack = [remaining.pop()]
                count += 1
                while stack:
                    node = stack.pop()
                    neighbors = {b if a == node else a for a, b in edges if node in (a, b)}
                    for v in neighbors & remaining:
                        remaining.remove(v)
                        stack.append(v)
            return count

        for mask in range(1 << len(possible)):
            edges = [edge for i, edge in enumerate(possible) if mask & (1 << i)]
            graph = {v: [] for v in vertices}
            for a, b in edges:
                graph[a].append(b)
            expected = {
                frozenset(e)
                for e in edges
                if components([x for x in edges if x != e]) > components(edges)
            }
            self.assertEqual({frozenset(e) for e in bridges(graph)}, expected)

    def test_long_chain_and_labels(self):
        self.assertEqual(len(bridges({i: [i + 1] for i in range(3000)})), 3000)
        self.assertEqual(
            {frozenset(e) for e in bridges({None: ["a", "a", None]})}, {frozenset([None, "a"])}
        )

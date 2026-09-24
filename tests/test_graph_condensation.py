import random
import unittest

from algorithm_lab.graph_condensation import graph_condensation


class CondensationTests(unittest.TestCase):
    def test_mutual_reachability_oracle(self):
        rng = random.Random(149)
        for _ in range(200):
            n = rng.randrange(10)
            graph = {a: [b for b in range(n) if rng.randrange(4) == 0] for a in range(n)}
            reach = {}
            for source in graph:
                seen, stack = {source}, [source]
                while stack:
                    for v in graph[stack.pop()]:
                        if v not in seen:
                            seen.add(v)
                            stack.append(v)
                reach[source] = seen
            expected = {
                frozenset(b for b in graph if b in reach[a] and a in reach[b]) for a in graph
            }
            components, dag = graph_condensation(graph)
            self.assertEqual(set(components), expected)
            membership = {v: i for i, c in enumerate(components) for v in c}
            expected_edges = {
                (membership[a], membership[b])
                for a in graph
                for b in graph[a]
                if membership[a] != membership[b]
            }
            self.assertEqual({(a, b) for a in dag for b in dag[a]}, expected_edges)
        components, dag = graph_condensation({None: iter(["x"])})
        self.assertEqual(set(components), {frozenset([None]), frozenset(["x"])})

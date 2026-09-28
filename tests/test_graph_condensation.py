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

    def test_deep_cycle_with_a_tail_is_condensed_without_recursion(self):
        size, tail = 1800, 40
        graph = {i: [i + 1] for i in range(size + tail)}
        graph[size - 1].append(0)
        components, dag = graph_condensation(graph)
        membership = {node: i for i, group in enumerate(components) for node in group}
        cycle = membership[0]
        self.assertEqual(components[cycle], frozenset(range(size)))
        self.assertEqual(len(components), tail + 2)
        self.assertEqual(dag[cycle], {membership[size]})
        for node in range(size, size + tail):
            self.assertEqual(dag[membership[node]], {membership[node + 1]})
        self.assertEqual(dag[membership[size + tail]], set())

    def test_internal_loops_and_duplicate_cross_edges_vanish(self):
        graph = {None: [None, "a", "a"], "a": [None, 1, 1], 1: [1], "alone": []}
        before = {node: rows[:] for node, rows in graph.items()}
        components, dag = graph_condensation(graph)
        membership = {node: i for i, group in enumerate(components) for node in group}
        self.assertEqual(
            set(components), {frozenset([None, "a"]), frozenset([1]), frozenset(["alone"])}
        )
        self.assertEqual(
            {(a, b) for a, rows in dag.items() for b in rows},
            {(membership[None], membership[1])},
        )
        self.assertEqual(graph, before)

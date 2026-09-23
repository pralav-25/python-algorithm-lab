import unittest

from algorithm_lab.connected_components import connected_components


class ComponentTests(unittest.TestCase):
    def test_asymmetric_edges_isolated_and_cycles(self):
        graph = {"a": ["b", "b"], "c": ["b"], "d": [], "e": ["f"], "f": ["e"]}
        self.assertEqual(
            set(connected_components(graph)), {frozenset("abc"), frozenset("d"), frozenset("ef")}
        )
        self.assertEqual(graph["a"], ["b", "b"])

    def test_partition_and_edge_membership(self):
        graph = {0: [1], 1: [2], 3: [4], 5: [], 6: [6]}
        groups = connected_components(graph)
        self.assertEqual(set().union(*groups), set(range(7)))
        self.assertEqual(sum(map(len, groups)), 7)
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                self.assertTrue(any(node in group and neighbor in group for group in groups))
        self.assertEqual(connected_components({}), [])

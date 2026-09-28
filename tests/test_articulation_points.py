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

    def test_normalization_preserves_cut_vertices_with_mixed_labels(self):
        leaf = ("leaf", 1)
        graph = {
            None: [None, "hub", "hub"],
            "hub": [1, 1, leaf, "hub"],
            1: [leaf],
            "isolated": ["isolated"],
        }
        before = {node: neighbors[:] for node, neighbors in graph.items()}
        self.assertEqual(articulation_points(graph), {"hub"})
        self.assertEqual(graph, before)
        self.assertEqual(
            articulation_points({node: iter(rows) for node, rows in graph.items()}), {"hub"}
        )

    def test_dfs_root_needs_two_independent_child_subtrees(self):
        # The root has two neighbors, but they belong to a single DFS subtree.
        self.assertEqual(articulation_points({0: [1, 2], 1: [2]}), set())
        self.assertEqual(articulation_points({0: [1, 2], 3: []}), {0})

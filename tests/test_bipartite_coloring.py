import itertools
import unittest

from algorithm_lab.bipartite_coloring import bipartite_coloring


class BipartiteTests(unittest.TestCase):
    def test_all_four_vertex_graphs_and_colorings(self):
        possible = list(itertools.combinations(range(4), 2))
        for mask in range(1 << len(possible)):
            edges = [edge for i, edge in enumerate(possible) if mask & (1 << i)]
            graph = {v: [b for a, b in edges if a == v] for v in range(4)}
            valid = any(
                all(colors[a] != colors[b] for a, b in edges)
                for colors in itertools.product(range(2), repeat=4)
            )
            result = bipartite_coloring(graph)
            self.assertEqual(result is not None, valid)
            if result is not None:
                self.assertEqual(set(result), set(range(4)))
                self.assertTrue(all(result[a] != result[b] for a, b in edges))

    def test_self_loop_empty_and_mixed_vertices(self):
        self.assertIsNone(bipartite_coloring({0: [0]}))
        self.assertEqual(bipartite_coloring({}), {})
        self.assertEqual(bipartite_coloring({None: ["x"]}), {None: 0, "x": 1})

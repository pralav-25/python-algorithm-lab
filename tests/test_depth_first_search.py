import random
import unittest

from algorithm_lab.depth_first_search import depth_first_search


class DFSTests(unittest.TestCase):
    def test_recursive_order_oracle(self):
        rng = random.Random(76)
        for _ in range(50):
            graph = {i: [j for j in range(8) if rng.random() < 0.3] for i in range(8)}
            expected, visited = [], set()

            def visit(node, visited=visited, expected=expected, graph=graph):
                if node in visited:
                    return
                visited.add(node)
                expected.append(node)
                for child in graph[node]:
                    visit(child)

            visit(0)
            self.assertEqual(depth_first_search(graph, 0), expected)

    def test_deep_cycle_and_missing_vertex(self):
        graph = {i: [i + 1] for i in range(3000)}
        graph[3000] = [0]
        self.assertEqual(depth_first_search(graph, 0), list(range(3001)))
        self.assertEqual(depth_first_search({}, "alone"), ["alone"])

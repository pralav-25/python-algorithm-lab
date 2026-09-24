import random
import unittest

from algorithm_lab.bipartite_matching import bipartite_matching


class MatchingTests(unittest.TestCase):
    def test_exhaustive_assignment_oracle(self):
        rng = random.Random(145)

        def best(graph, lefts, used):
            if not lefts:
                return 0
            left, *rest = lefts
            return max(
                [best(graph, rest, used)]
                + [
                    1 + best(graph, rest, used | {right})
                    for right in graph[left]
                    if right not in used
                ]
            )

        for _ in range(250):
            graph = {a: [b for b in range(5) if rng.randrange(2)] for a in range(5)}
            result = bipartite_matching(graph)
            self.assertEqual(len(result), best(graph, list(graph), set()))
            self.assertEqual(len(set(result.values())), len(result))
            self.assertTrue(all(right in graph[left] for left, right in result.items()))

    def test_none_and_duplicate_labels(self):
        graph = {None: [None, None, "x"], "x": [None]}
        result = bipartite_matching(graph)
        self.assertEqual(len(result), 2)
        self.assertEqual(set(result.values()), {None, "x"})
        self.assertEqual(bipartite_matching({}), {})

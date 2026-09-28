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

    def test_long_augmenting_path_reassigns_every_previous_match(self):
        # The last left vertex forces an alternating path beyond recursion depth.
        size = 1500
        graph = {left: [left, left + 1] for left in range(size)}
        graph[size] = [0]
        result = bipartite_matching(graph)
        self.assertEqual(result, {**dict(enumerate(range(1, size + 1))), size: 0})
        self.assertEqual(graph[0], [0, 1])
        self.assertEqual(graph[size], [0])

    def test_neighbor_iterators_and_repeated_calls(self):
        graph = {"a": [1, 1, 2], "b": [1], "c": []}
        before = {left: rows[:] for left, rows in graph.items()}
        expected = {"a": 2, "b": 1}
        self.assertEqual(bipartite_matching(graph), expected)
        self.assertEqual(bipartite_matching(graph), expected)
        self.assertEqual(graph, before)
        self.assertEqual(
            bipartite_matching({left: iter(rows) for left, rows in graph.items()}), expected
        )

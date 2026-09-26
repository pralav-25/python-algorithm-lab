import itertools
import unittest
from functools import lru_cache

from algorithm_lab.huffman_codes import huffman_codes


@lru_cache(None)
def optimal_merge_cost(weights):
    if len(weights) <= 1:
        return 0
    return min(
        weights[i]
        + weights[j]
        + optimal_merge_cost(
            tuple(
                sorted(
                    [w for k, w in enumerate(weights) if k not in (i, j)]
                    + [weights[i] + weights[j]]
                )
            )
        )
        for i in range(len(weights))
        for j in range(i + 1, len(weights))
    )


class Tests(unittest.TestCase):
    def test_prefix_codes_have_minimum_weighted_length(self):
        for weights in itertools.product(range(1, 4), repeat=4):
            codes = huffman_codes(dict(enumerate(weights)))
            for a, b in itertools.permutations(codes.values(), 2):
                self.assertFalse(b.startswith(a))
            self.assertEqual(
                sum(weights[i] * len(code) for i, code in codes.items()),
                optimal_merge_cost(tuple(sorted(weights))),
            )

    def test_empty_single_and_tie_order(self):
        self.assertEqual(huffman_codes({}), {})
        self.assertEqual(huffman_codes({None: 4}), {None: "0"})
        self.assertEqual(huffman_codes({None: 1, "a": 1, 2: 1}), {2: "0", None: "10", "a": "11"})
        for weight in [0, -1, True, 1.5]:
            with self.assertRaises(ValueError):
                huffman_codes({"a": weight})

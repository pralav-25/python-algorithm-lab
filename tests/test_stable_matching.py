import random
import unittest
from itertools import permutations

from algorithm_lab.stable_matching import stable_matching


def stable(a, b, matching):
    reverse = {r: p for p, r in enumerate(matching)}
    return all(
        not (a[p].index(r) < a[p].index(matching[p]) and b[r].index(p) < b[r].index(reverse[r]))
        for p in range(len(a))
        for r in range(len(a))
    )


class Tests(unittest.TestCase):
    def test_stability_and_proposer_optimality(self):
        rng = random.Random(248)
        for n in range(5):
            for _ in range(15):
                a = [rng.sample(range(n), n) for _ in range(n)]
                b = [rng.sample(range(n), n) for _ in range(n)]
                result = stable_matching(a, b)
                self.assertEqual(sorted(result), list(range(n)))
                self.assertTrue(stable(a, b, result))
                for candidate in permutations(range(n)):
                    if stable(a, b, candidate):
                        for p in range(n):
                            self.assertLessEqual(a[p].index(result[p]), a[p].index(candidate[p]))

    def test_invalid(self):
        for a, b in [([[0]], []), ([[True]], [[0]]), ([[0, 0], [0, 1]], [[0, 1], [1, 0]])]:
            with self.assertRaises(ValueError):
                stable_matching(a, b)

    def test_repeated_displacements_with_one_pass_preference_rows(self):
        size = 40
        proposers = [list(range(size)) for _ in range(size)]
        receivers = [list(reversed(range(size))) for _ in range(size)]
        before = ([row[:] for row in proposers], [row[:] for row in receivers])
        expected = list(reversed(range(size)))
        self.assertEqual(stable_matching(proposers, receivers), expected)
        self.assertEqual((proposers, receivers), before)
        self.assertEqual(
            stable_matching((iter(row) for row in proposers), (iter(row) for row in receivers)),
            expected,
        )

    def test_invalid_preference_domains_on_either_side(self):
        valid = [[0, 1], [1, 0]]
        for malformed in [
            [[0], [1, 0]],
            [[0, 2], [1, 0]],
            [[0, -1], [1, 0]],
            [[0, 1.0], [1, 0]],
            [[0, 1], [True, 0]],
        ]:
            for a, b in ((valid, malformed), (malformed, valid)):
                with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                    stable_matching(a, b)

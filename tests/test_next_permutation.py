import itertools
import unittest

from algorithm_lab.next_permutation import next_permutation


class PermutationTests(unittest.TestCase):
    def test_enumeration_oracle(self):
        for source in [[], [1], [1, 1], [1, 2, 2, 3], [0, 1, 2, 3, 4]]:
            arrangements = sorted(set(itertools.permutations(source)))
            for i, data in enumerate(arrangements):
                expected = list(arrangements[i + 1]) if i + 1 < len(arrangements) else None
                mutable = list(data)
                self.assertEqual(next_permutation(mutable), expected)
                self.assertEqual(mutable, list(data))

import itertools
import unittest

from algorithm_lab.n_queens import n_queens


class QueenTests(unittest.TestCase):
    def test_permutation_oracle(self):
        for n in range(9):
            expected = [
                p
                for p in itertools.permutations(range(n))
                if len({i + v for i, v in enumerate(p)}) == n
                and len({i - v for i, v in enumerate(p)}) == n
            ]
            self.assertEqual(list(n_queens(n)), expected)

    def test_invalid_and_independent_generators(self):
        first, second = n_queens(4), n_queens(4)
        self.assertEqual(next(first), next(second))
        self.assertEqual(list(first), list(second))
        for n in [-1, True, 1.5]:
            with self.assertRaises(ValueError):
                n_queens(n)

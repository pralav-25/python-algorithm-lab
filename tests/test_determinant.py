import itertools
import math
import random
import unittest

from algorithm_lab.determinant import determinant


class Tests(unittest.TestCase):
    def test_leibniz_oracle(self):
        rng = random.Random(217)
        for n in range(5):
            for _ in range(15):
                a = [[rng.randrange(-3, 4) for _ in range(n)] for _ in range(n)]
                expected = 0
                for p in itertools.permutations(range(n)):
                    inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
                    expected += (-1) ** inversions * math.prod(a[i][p[i]] for i in range(n))
                self.assertEqual(determinant(a), expected)

    def test_invalid(self):
        for a in [[[1, 2]], [[True]], [[1.0]]]:
            with self.assertRaises(ValueError):
                determinant(a)

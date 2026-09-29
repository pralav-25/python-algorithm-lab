import itertools
import math
import random
import unittest
from fractions import Fraction

from algorithm_lab.determinant import determinant


class Tests(unittest.TestCase):
    def test_rational_row_operations_and_input_isolation(self):
        matrix = [[Fraction(2, 3), 4, -7], [0, Fraction(-5, 7), 2], [0, 0, Fraction(11, 13)]]
        expected = Fraction(-110, 273)
        original = [row[:] for row in matrix]
        self.assertEqual(determinant(matrix), expected)
        for order in itertools.permutations(range(3)):
            inversions = sum(order[i] > order[j] for i in range(3) for j in range(i + 1, 3))
            self.assertEqual(
                determinant(iter(matrix[i]) for i in order), (-1) ** inversions * expected
            )
        changed = [row[:] for row in matrix]
        changed[2] = [a + Fraction(17, 19) * b for a, b in zip(changed[2], changed[0], strict=True)]
        self.assertEqual(determinant(changed), expected)
        self.assertEqual(matrix, original)

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

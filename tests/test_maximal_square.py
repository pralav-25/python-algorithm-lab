import unittest
from itertools import product

from algorithm_lab.maximal_square import maximal_square


class Tests(unittest.TestCase):
    def test_enumerate_squares(self):
        for values in product(range(2), repeat=9):
            matrix = [list(values[i : i + 3]) for i in range(0, 9, 3)]
            candidates = [
                (size, i, j)
                for size in range(1, 4)
                for i in range(4 - size)
                for j in range(4 - size)
                if all(matrix[r][c] for r in range(i, i + size) for c in range(j, j + size))
            ]
            expected = (
                min(candidates, key=lambda x: (-x[0], x[1], x[2]))
                if candidates
                else (0, None, None)
            )
            self.assertEqual(maximal_square(matrix), expected)
        self.assertEqual(maximal_square([[]]), (0, None, None))

    def test_invalid(self):
        for matrix in [[[1], [1, 0]], [[True]], [[2]]]:
            with self.assertRaises(ValueError):
                maximal_square(matrix)

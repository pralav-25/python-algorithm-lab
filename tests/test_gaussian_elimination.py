import unittest
from fractions import Fraction

from algorithm_lab.gaussian_elimination import gaussian_elimination


class Tests(unittest.TestCase):
    def test_known_solutions_and_row_swap(self):
        for matrix, solution in [
            ([[0, 2], [3, 4]], [Fraction(1, 3), -7]),
            ([[1, 2, 3], [0, 1, 4], [5, 6, 0]], [2, -1, 3]),
        ]:
            before = [row[:] for row in matrix]
            rhs = [sum(a * b for a, b in zip(row, solution, strict=True)) for row in matrix]
            self.assertEqual(gaussian_elimination(matrix, rhs), solution)
            self.assertEqual(matrix, before)
        self.assertEqual(gaussian_elimination([], []), [])

    def test_invalid(self):
        for a, b in [([[1, 2], [2, 4]], [1, 2]), ([[1, 2]], [1]), ([[True]], [1]), ([[1]], [])]:
            with self.assertRaises(ValueError):
                gaussian_elimination(a, b)

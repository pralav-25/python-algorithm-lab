import unittest
from fractions import Fraction
from itertools import permutations

from algorithm_lab.gaussian_elimination import gaussian_elimination


class Tests(unittest.TestCase):
    def test_rational_system_under_all_row_permutations(self):
        matrix = [[0, Fraction(1, 2), 0], [0, 0, Fraction(-2, 3)], [Fraction(3, 5), 0, 0]]
        solution = [Fraction(2, 7), Fraction(-5, 11), Fraction(13, 17)]
        rhs = [sum(a * b for a, b in zip(row, solution, strict=True)) for row in matrix]
        original = ([row[:] for row in matrix], rhs[:])
        for ordering in permutations(range(3)):
            rows = (iter(matrix[i]) for i in ordering)
            result = gaussian_elimination(rows, (rhs[i] for i in ordering))
            self.assertEqual(result, solution)
            self.assertTrue(all(type(value) is Fraction for value in result))
        self.assertEqual(gaussian_elimination(matrix, rhs), solution)
        self.assertEqual((matrix, rhs), original)

    def test_singular_system_rejects_both_consistent_and_inconsistent_rhs(self):
        for rhs in [[1, 2], [1, 3]]:
            with self.subTest(rhs=rhs), self.assertRaises(ValueError):
                gaussian_elimination([[1, 2], [2, 4]], rhs)

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

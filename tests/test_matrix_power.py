import unittest

from algorithm_lab.matrix_power import matrix_power


class Tests(unittest.TestCase):
    def test_dense_matrix_against_linear_multiplication(self):
        matrix = [[2, -1, 3], [0, 4, 1], [-2, 5, 0]]
        original = [row[:] for row in matrix]
        expected = [[int(i == j) for j in range(3)] for i in range(3)]
        for exponent in range(10):
            self.assertEqual(matrix_power((iter(row) for row in matrix), exponent), expected)
            expected = [
                [sum(expected[i][k] * matrix[k][j] for k in range(3)) for j in range(3)]
                for i in range(3)
            ]
        for exponent in [0, 1, 4]:
            result = matrix_power(matrix, exponent)
            other_rows = [row[:] for row in result[1:]]
            result[0][0] = 999
            self.assertEqual(result[1:], other_rows)
            self.assertEqual(matrix, original)

    def test_known_powers(self):
        for n in range(20):
            self.assertEqual(matrix_power([[1, 3], [0, 1]], n), [[1, 3 * n], [0, 1]])
            self.assertEqual(matrix_power([[2, 0], [0, -3]], n), [[2**n, 0], [0, (-3) ** n]])
        self.assertEqual(matrix_power([], 10), [])
        a = [[1, 2], [3, 4]]
        matrix_power(a, 5)
        self.assertEqual(a, [[1, 2], [3, 4]])

    def test_invalid(self):
        for a, n in [([[1, 2]], 2), ([[1]], -1), ([[True]], 1), ([[1]], False)]:
            with self.assertRaises(ValueError):
                matrix_power(a, n)

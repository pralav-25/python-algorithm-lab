import unittest

from algorithm_lab.matrix_power import matrix_power


class Tests(unittest.TestCase):
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

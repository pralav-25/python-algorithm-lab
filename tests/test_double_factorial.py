import math
import unittest

from algorithm_lab.double_factorial import double_factorial


def matching_count(vertices):
    if not vertices:
        return 1
    return sum(
        matching_count(vertices[1:index] + vertices[index + 1 :])
        for index in range(1, len(vertices))
    )


class Tests(unittest.TestCase):
    def test_perfect_matching_oracle(self):
        for vertices in range(0, 12, 2):
            self.assertEqual(double_factorial(vertices - 1), matching_count(tuple(range(vertices))))

    def test_even_factorial_identity(self):
        for half in range(21):
            self.assertEqual(double_factorial(2 * half), 2**half * math.factorial(half))

    def test_invalid(self):
        for n in (-2, True, 1.5, "3", None):
            with self.assertRaises(ValueError):
                double_factorial(n)

import random
import unittest

from algorithm_lab.matrix_chain import matrix_chain


def all_costs(dimensions):
    if len(dimensions) == 2:
        return [0]
    return [
        left + right + dimensions[0] * dimensions[split] * dimensions[-1]
        for split in range(1, len(dimensions) - 1)
        for left in all_costs(dimensions[: split + 1])
        for right in all_costs(dimensions[split:])
    ]


class MatrixChainTests(unittest.TestCase):
    def test_all_parenthesizations_oracle(self):
        rng = random.Random(5)
        for size in range(2, 9):
            dimensions = [rng.randrange(1, 20) for _ in range(size)]
            cost, expression = matrix_chain(dimensions)
            self.assertEqual(cost, min(all_costs(dimensions)))
            self.assertEqual(expression.count("@"), size - 2)
            for item in range(1, size):
                self.assertEqual(expression.count(f"A{item}"), 1)

    def test_single_matrix_known_case_and_validation(self):
        self.assertEqual(matrix_chain([4, 5]), (0, "A1"))
        self.assertEqual(matrix_chain([30, 35, 15, 5, 10, 20, 25])[0], 15125)
        for dimensions in [[], [1], [1, 0], [1, True], [1.5, 2]]:
            with self.assertRaises(ValueError):
                matrix_chain(dimensions)

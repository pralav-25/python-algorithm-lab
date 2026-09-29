import random
import unittest

from algorithm_lab.linear_recurrence import linear_recurrence


class Tests(unittest.TestCase):
    def test_sparse_periodic_recurrence_at_large_indices(self):
        initial = [10**80, -7, 3, 19]
        coefficients = [0, 0, 0, 1]
        for n in [0, 3, 4, 5, 10**12 + 1, 10**12 + 3]:
            self.assertEqual(
                linear_recurrence(iter(initial), iter(coefficients), n), initial[n % 4]
            )
        self.assertEqual(linear_recurrence([9], [-1], 10**12 + 1), -9)
        self.assertEqual(linear_recurrence(initial, [0] * 4, 4), 0)
        self.assertEqual(initial, [10**80, -7, 3, 19])

    def test_initial_term_still_validates_all_coefficients(self):
        for coefficients in [[1, True], [1, 1.5]]:
            with self.assertRaises(ValueError):
                linear_recurrence([2, 3], coefficients, 0)

    def test_direct_recurrence_oracle(self):
        rng = random.Random(219)
        for k in range(1, 6):
            initial = [rng.randrange(-3, 4) for _ in range(k)]
            coefficients = [rng.randrange(-2, 3) for _ in range(k)]
            direct = initial[:]
            for n in range(k, 30):
                direct.append(sum(c * direct[n - j - 1] for j, c in enumerate(coefficients)))
            for n, expected in enumerate(direct):
                self.assertEqual(linear_recurrence(initial, coefficients, n), expected)

    def test_invalid(self):
        for a, c, n in [([], [], 0), ([1], [1, 2], 0), ([True], [1], 0), ([1], [1], -1)]:
            with self.assertRaises(ValueError):
                linear_recurrence(a, c, n)

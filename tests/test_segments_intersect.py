import itertools
import unittest
from fractions import Fraction

from algorithm_lab.segments_intersect import segments_intersect


def oracle(a, b, c, d):
    # Solve the two parametric line equations, independently of orientation tests.
    u, v, w = [tuple(q[i] - p[i] for i in (0, 1)) for p, q in [(a, b), (c, d), (a, c)]]
    determinant = u[0] * v[1] - u[1] * v[0]
    if determinant:
        t = Fraction(w[0] * v[1] - w[1] * v[0], determinant)
        s = Fraction(w[0] * u[1] - w[1] * u[0], determinant)
        return 0 <= t <= 1 and 0 <= s <= 1

    # Grid endpoints ensure every collinear overlap contains a grid point.
    def contains(p, start, vector):
        if vector == (0, 0):
            return p == start
        axis = 0 if vector[0] else 1
        t = Fraction(p[axis] - start[axis], vector[axis])
        return 0 <= t <= 1 and all(start[i] + t * vector[i] == p[i] for i in (0, 1))

    return any(contains(p, a, u) and contains(p, c, v) for p in (a, b, c, d))


class Tests(unittest.TestCase):
    def test_all_small_segments(self):
        points = list(itertools.product(range(2), repeat=2)) + [(2, 0), (0, 2)]
        for a, b, c, d in itertools.product(points, repeat=4):
            self.assertEqual(segments_intersect(a, b, c, d), oracle(a, b, c, d), (a, b, c, d))

    def test_exact_large_coordinates(self):
        n = 10**100
        self.assertTrue(segments_intersect((0, 0), (n, n), (0, n), (n, 0)))
        with self.assertRaises(ValueError):
            segments_intersect((0, True), (0, 0), (0, 0), (0, 0))

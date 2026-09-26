import unittest

from algorithm_lab.point_in_polygon import point_in_polygon


class Tests(unittest.TestCase):
    def test_rectangle_membership_and_orientation(self):
        polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]
        for x in range(-1, 6):
            for y in range(-1, 5):
                for vertices in [polygon, polygon[::-1], polygon + [polygon[0]]]:
                    self.assertEqual(
                        point_in_polygon((x, y), vertices), 0 <= x <= 4 and 0 <= y <= 3
                    )
                    self.assertEqual(
                        point_in_polygon((x, y), vertices, include_boundary=False),
                        0 < x < 4 and 0 < y < 3,
                    )

    def test_concave_shape_and_large_integers(self):
        polygon = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)]
        self.assertTrue(point_in_polygon((1, 3), polygon))
        self.assertFalse(point_in_polygon((3, 3), polygon))
        n = 10**100
        self.assertTrue(point_in_polygon((n, n), [(0, 0), (3 * n, 0), (0, 3 * n)]))
        with self.assertRaises(ValueError):
            point_in_polygon((0, 0), [])
        with self.assertRaises(ValueError):
            point_in_polygon((0, 0), polygon, include_boundary=1)

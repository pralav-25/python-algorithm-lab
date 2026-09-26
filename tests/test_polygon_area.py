import unittest
from fractions import Fraction

from algorithm_lab.polygon_area import polygon_area


class Tests(unittest.TestCase):
    def test_triangles_rectangles_and_translations(self):
        for width in range(1, 10):
            for height in range(1, 10):
                for offset in [0, -11, 10**80]:
                    triangle = [
                        (offset, offset),
                        (offset + width, offset),
                        (offset, offset + height),
                    ]
                    self.assertEqual(polygon_area(triangle), Fraction(width * height, 2))
                    self.assertEqual(polygon_area(reversed(triangle)), Fraction(width * height, 2))
                    rectangle = [(0, 0), (width, 0), (width, height), (0, height), (0, 0)]
                    self.assertEqual(polygon_area(rectangle), width * height)

    def test_concave_and_degenerate(self):
        self.assertEqual(polygon_area([(0, 0), (3, 0), (3, 1), (1, 1), (1, 3), (0, 3)]), 5)
        for points in [[], [(1, 2)], [(0, 0), (1, 1)], [(0, 0), (1, 1), (2, 2)]]:
            self.assertEqual(polygon_area(points), 0)
        with self.assertRaises(ValueError):
            polygon_area([(False, 0)])

import unittest

from algorithm_lab.rotated_search import rotated_search


class RotatedTests(unittest.TestCase):
    def test_every_rotation(self):
        for size in range(1, 35):
            original = list(range(0, size * 2, 2))
            for pivot in range(size):
                data = original[pivot:] + original[:pivot]
                for target in range(-1, size * 2 + 1):
                    expected = data.index(target) if target in data else -1
                    self.assertEqual(rotated_search(data, target), expected)
        self.assertEqual(rotated_search([], 1), -1)

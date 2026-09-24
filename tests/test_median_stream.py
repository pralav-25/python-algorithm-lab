import random
import unittest
from fractions import Fraction

from algorithm_lab.median_stream import MedianStream


class MedianTests(unittest.TestCase):
    def test_sorted_oracle(self):
        rng = random.Random(115)
        stream, data = MedianStream(), []
        for value in [10**100, -(10**100)] + [rng.randrange(-50, 51) for _ in range(200)]:
            data.append(value)
            stream.add(value)
            ordered = sorted(data)
            expected = Fraction(ordered[(len(data) - 1) // 2] + ordered[len(data) // 2], 2)
            self.assertEqual(stream.median(), expected)
            self.assertEqual(len(stream), len(data))

    def test_invalid(self):
        stream = MedianStream()
        with self.assertRaises(ValueError):
            stream.median()
        for value in [True, 1.5, float("nan")]:
            with self.assertRaises(ValueError):
                stream.add(value)
        self.assertEqual(len(stream), 0)

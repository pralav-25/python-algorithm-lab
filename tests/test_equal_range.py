import bisect
import random
import unittest

from algorithm_lab.equal_range import equal_range


class EqualRangeTests(unittest.TestCase):
    def test_bisect_oracle(self):
        rng = random.Random(120)
        for n in range(70):
            values = sorted(rng.randrange(-5, 6) for _ in range(n))
            for target in range(-7, 8):
                self.assertEqual(
                    equal_range(values, target),
                    (bisect.bisect_left(values, target), bisect.bisect_right(values, target)),
                )
        self.assertEqual(equal_range(["a", "b", "b"], "b"), (1, 3))

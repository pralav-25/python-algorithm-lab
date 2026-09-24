import random
import unittest

from algorithm_lab.lcp_array import lcp_array


class LCPTests(unittest.TestCase):
    def test_naive_oracle(self):
        rng = random.Random(133)
        for n in range(80):
            text = "".join(rng.choice("ab🙂") for _ in range(n))
            order = sorted(range(n), key=lambda i: text[i:])
            expected = [0] * n
            for i in range(1, n):
                first, second = text[order[i - 1] :], text[order[i] :]
                for a, b in zip(first, second, strict=False):
                    if a != b:
                        break
                    expected[i] += 1
            self.assertEqual(lcp_array(text, order), expected)

    def test_invalid_arrays(self):
        for order in [[], [0, 0], [0, 2], [0, True], [-1, 0]]:
            with self.assertRaises(ValueError):
                lcp_array("ab", order)

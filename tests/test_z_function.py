import itertools
import unittest

from algorithm_lab.z_function import z_function


class ZTests(unittest.TestCase):
    def test_direct_prefix_oracle(self):
        for n in range(8):
            for chars in itertools.product("a🙂", repeat=n):
                text = "".join(chars)
                expected = [0] * n
                for i in range(1, n):
                    while i + expected[i] < n and text[expected[i]] == text[i + expected[i]]:
                        expected[i] += 1
                self.assertEqual(z_function(text), expected)

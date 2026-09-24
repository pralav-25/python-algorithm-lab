import itertools
import random
import unittest

from algorithm_lab.suffix_array import suffix_array


class SuffixTests(unittest.TestCase):
    def test_sorted_suffix_oracle(self):
        for n in range(8):
            for chars in itertools.product("a🙂", repeat=n):
                text = "".join(chars)
                self.assertEqual(suffix_array(text), sorted(range(n), key=lambda i: text[i:]))
        rng = random.Random(132)
        for _ in range(100):
            text = "".join(rng.choice("banana🙂" + chr(0)) for _ in range(100))
            self.assertEqual(suffix_array(text), sorted(range(len(text)), key=lambda i: text[i:]))

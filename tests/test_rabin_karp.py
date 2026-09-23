import random
import unittest

from algorithm_lab.rabin_karp import rabin_karp


class RabinKarpTests(unittest.TestCase):
    def test_seeded_substring_oracle(self):
        rng = random.Random(54)
        for _ in range(500):
            text = "".join(rng.choices("abé🙂", k=rng.randrange(30)))
            pattern = "".join(rng.choices("abé🙂", k=rng.randrange(8)))
            self.assertEqual(
                rabin_karp(text, pattern),
                [i for i in range(len(text) + 1) if text.startswith(pattern, i)],
            )

    def test_hash_collision_is_verified(self):
        # Both two-character polynomials equal 257, but the strings differ.
        self.assertEqual(rabin_karp(chr(1) + chr(0), chr(0) + chr(257)), [])
        self.assertEqual(rabin_karp("aaaa", "aa"), [0, 1, 2])

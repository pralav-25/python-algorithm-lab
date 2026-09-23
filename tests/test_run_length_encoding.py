import random
import unittest

from algorithm_lab.run_length_encoding import decode_runs, encode_runs


class RunLengthTests(unittest.TestCase):
    def test_round_trips_and_canonical_runs(self):
        rng = random.Random(40)
        for size in range(100):
            text = "".join(rng.choices("ab🙂", k=size))
            runs = encode_runs(text)
            self.assertEqual(decode_runs(iter(runs), max_output=size), text)
            self.assertEqual(sum(count for _, count in runs), size)
            self.assertTrue(all(a[0] != b[0] for a, b in zip(runs, runs[1:], strict=False)))

    def test_malformed_and_oversized_runs(self):
        for runs in [[("", 1)], [("ab", 1)], [("x", 0)], [("x", True)], [("x", 2.5)]]:
            with self.assertRaises(ValueError):
                decode_runs(runs)
        with self.assertRaises(ValueError):
            decode_runs([("x", 10**100)], max_output=10)
        self.assertEqual(decode_runs([], max_output=0), "")

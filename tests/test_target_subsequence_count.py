import itertools
import unittest

from algorithm_lab.target_subsequence_count import target_subsequence_count


class Tests(unittest.TestCase):
    def test_index_subset_oracle(self):
        texts = ["".join(chars) for n in range(6) for chars in itertools.product("ab", repeat=n)]
        targets = ["".join(chars) for n in range(4) for chars in itertools.product("ab", repeat=n)]
        for text in texts:
            for target in targets:
                expected = sum(
                    "".join(text[i] for i in indices) == target
                    for indices in itertools.combinations(range(len(text)), len(target))
                )
                self.assertEqual(target_subsequence_count(text, target), expected)
        self.assertEqual(target_subsequence_count("🙂🙂a🙂", "🙂🙂"), 3)

    def test_invalid(self):
        for args in [(None, ""), ("", []), (b"a", "a")]:
            with self.assertRaises(ValueError):
                target_subsequence_count(*args)

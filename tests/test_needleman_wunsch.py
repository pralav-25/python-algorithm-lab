import itertools
import unittest

from algorithm_lab.needleman_wunsch import needleman_wunsch


class Tests(unittest.TestCase):
    @staticmethod
    def scores(first, second, match, mismatch, gap):
        if not first and not second:
            yield 0
        if first and second:
            for score in Tests.scores(first[1:], second[1:], match, mismatch, gap):
                yield score + (match if first[0] == second[0] else mismatch)
        if first:
            for score in Tests.scores(first[1:], second, match, mismatch, gap):
                yield score + gap
        if second:
            for score in Tests.scores(first, second[1:], match, mismatch, gap):
                yield score + gap

    def test_all_alignment_paths(self):
        words = ["".join(chars) for n in range(4) for chars in itertools.product("ab", repeat=n)]
        for first, second in itertools.product(words, repeat=2):
            for match, mismatch, gap in [(1, -1, -1), (3, -3, -2), (0, 1, 2), (-2, -3, -1)]:
                expected = max(self.scores(first, second, match, mismatch, gap))
                self.assertEqual(
                    needleman_wunsch(first, second, match=match, mismatch=mismatch, gap=gap),
                    expected,
                )
        self.assertEqual(needleman_wunsch("🙂a", "🙂b"), 0)

    def test_invalid_scores_even_empty(self):
        for name in ["match", "mismatch", "gap"]:
            for value in [True, 1.0, None]:
                with self.assertRaises(ValueError):
                    needleman_wunsch("", "", **{name: value})
        for args in [(None, ""), ("", []), (b"a", "a")]:
            with self.assertRaises(ValueError):
                needleman_wunsch(*args)

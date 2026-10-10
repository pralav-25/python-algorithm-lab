import itertools
import unittest

from algorithm_lab.smith_waterman import smith_waterman


class Tests(unittest.TestCase):
    @staticmethod
    def alignment_scores(first, second, match, mismatch, gap):
        if not first and not second:
            yield 0
        if first and second:
            for score in Tests.alignment_scores(first[1:], second[1:], match, mismatch, gap):
                yield score + (match if first[0] == second[0] else mismatch)
        if first:
            for score in Tests.alignment_scores(first[1:], second, match, mismatch, gap):
                yield score + gap
        if second:
            for score in Tests.alignment_scores(first, second[1:], match, mismatch, gap):
                yield score + gap

    def test_enumerate_local_intervals_and_all_alignments(self):
        words = ["".join(chars) for n in range(3) for chars in itertools.product("ab", repeat=n)]
        for first, second in itertools.product(words, repeat=2):
            for match, mismatch, gap in [(2, -1, -1), (3, -3, -2), (1, 0, 0)]:
                expected = max(
                    score
                    for left in range(len(first) + 1)
                    for right in range(left, len(first) + 1)
                    for other_left in range(len(second) + 1)
                    for other_right in range(other_left, len(second) + 1)
                    for score in self.alignment_scores(
                        first[left:right], second[other_left:other_right], match, mismatch, gap
                    )
                )
                self.assertEqual(
                    smith_waterman(first, second, match=match, mismatch=mismatch, gap=gap), expected
                )
        self.assertEqual(smith_waterman("GGTTGACTA", "TGTTACGG"), 9)
        self.assertEqual(smith_waterman("🙂a", "🙂b"), 2)

    def test_invalid(self):
        for scores in [
            {"match": 0},
            {"match": True},
            {"match": 1.0},
            {"mismatch": 1},
            {"gap": 1},
            {"gap": False},
            {"mismatch": -1.0},
        ]:
            with self.assertRaises(ValueError):
                smith_waterman("", "", **scores)
        for args in [(None, ""), ("", []), (b"a", "a")]:
            with self.assertRaises(ValueError):
                smith_waterman(*args)

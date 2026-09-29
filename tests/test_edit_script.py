import unittest
from itertools import product

from algorithm_lab.edit_script import edit_script
from algorithm_lab.levenshtein import levenshtein


class Tests(unittest.TestCase):
    def test_diagonal_ties_preserve_replace_alignment(self):
        self.assertEqual(
            edit_script("ab", "ba"), (2, [("replace", "a", "b"), ("replace", "b", "a")])
        )
        self.assertEqual(edit_script("aa", "a"), (1, [("delete", "a", ""), ("equal", "a", "a")]))
        self.assertEqual(edit_script("a", "aa"), (1, [("insert", "", "a"), ("equal", "a", "a")]))

    def test_composed_and_decomposed_unicode_remain_distinct(self):
        source, target = "é", "e\u0301"
        distance, operations = edit_script(source, target)
        self.assertEqual(distance, 2)
        self.assertEqual(operations, [("insert", "", "e"), ("replace", "é", "\u0301")])
        self.assertEqual(edit_script("🙂", ""), (1, [("delete", "🙂", "")]))
        self.assertEqual(edit_script("", "🙂"), (1, [("insert", "", "🙂")]))

    def test_alignment_and_distance(self):
        words = ["".join(p) for n in range(4) for p in product("ab", repeat=n)] + ["é🙂"]
        for a in words:
            for b in words:
                distance, operations = edit_script(a, b)
                self.assertEqual("".join(op[1] for op in operations), a)
                self.assertEqual("".join(op[2] for op in operations), b)
                self.assertEqual(sum(op[0] != "equal" for op in operations), distance)
                self.assertEqual(distance, levenshtein(a, b))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            edit_script([], "")

import itertools
import re
import unittest

from algorithm_lab.regex_match import regex_match


class Tests(unittest.TestCase):
    def test_stdlib_regex_oracle_for_valid_grammar(self):
        texts = ["".join(chars) for n in range(5) for chars in itertools.product("ab", repeat=n)]
        texts += ["🙂", "a\nb", "\n"]
        for size in range(5):
            for tokens in itertools.product(["a", "b", ".", "a*", "b*", ".*"], repeat=size):
                pattern = "".join(tokens)
                compiled = re.compile(pattern, re.DOTALL)
                for text in texts:
                    self.assertEqual(
                        regex_match(text, pattern), compiled.fullmatch(text) is not None
                    )

    def test_other_metacharacters_are_literal(self):
        for text in ["a+b", "[x]", "a?", "a|b", "\\", "^$"]:
            self.assertTrue(regex_match(text, text))
        self.assertFalse(regex_match("b", "a|b"))
        self.assertTrue(regex_match("+++", "+*"))
        self.assertTrue(regex_match("\n", "."))
        self.assertFalse(regex_match("abc", "ab"))

    def test_invalid_even_empty_text(self):
        for pattern in ["*", "*a", "a**", ".**", "a*b**", None, []]:
            with self.assertRaises(ValueError):
                regex_match("", pattern)
        with self.assertRaises(ValueError):
            regex_match(None, "")

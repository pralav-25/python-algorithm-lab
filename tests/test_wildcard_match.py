import itertools
import re
import unittest

from algorithm_lab.wildcard_match import wildcard_match


class WildcardTests(unittest.TestCase):
    def test_regex_translation_oracle(self):
        texts = ["".join(p) for n in range(5) for p in itertools.product("ab", repeat=n)]
        patterns = ["".join(p) for n in range(5) for p in itertools.product("ab?*", repeat=n)]
        for pattern in patterns:
            expression = "".join(
                ".*" if c == "*" else "." if c == "?" else re.escape(c) for c in pattern
            )
            for text in texts:
                self.assertEqual(
                    wildcard_match(text, pattern), re.fullmatch(expression, text) is not None
                )
        self.assertTrue(wildcard_match(chr(10), "?"))
        self.assertTrue(wildcard_match("[a]", "[a]"))

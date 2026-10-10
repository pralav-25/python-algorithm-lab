import itertools
import unittest

from algorithm_lab.boolean_parenthesization import boolean_parenthesization


class Tests(unittest.TestCase):
    @staticmethod
    def evaluations(expression):
        if len(expression) == 1:
            return [expression == "T"]
        outcomes = []
        for split in range(1, len(expression), 2):
            for left, right in itertools.product(
                Tests.evaluations(expression[:split]),
                Tests.evaluations(expression[split + 1 :]),
            ):
                operator = expression[split]
                outcomes.append(
                    left and right
                    if operator == "&"
                    else left or right
                    if operator == "|"
                    else left != right
                )
        return outcomes

    def test_enumerate_all_expression_trees(self):
        self.assertEqual(boolean_parenthesization(""), (0, 0))
        for size in range(1, 5):
            for literals in itertools.product("TF", repeat=size):
                for operators in itertools.product("&|^", repeat=size - 1):
                    expression = literals[0] + "".join(
                        operator + literal
                        for operator, literal in zip(operators, literals[1:], strict=True)
                    )
                    outcomes = self.evaluations(expression)
                    self.assertEqual(
                        boolean_parenthesization(expression),
                        (outcomes.count(False), outcomes.count(True)),
                    )

    def test_invalid(self):
        for expression in [None, True, "T&", "&T", "T&&F", "TF", "1", "T | F", "T+F"]:
            with self.assertRaises(ValueError):
                boolean_parenthesization(expression)

"""Return half-open bounds of the earliest longest balanced parentheses substring.

Input must be a string containing only '(' and ')'; other input raises ValueError.
No nonempty valid substring returns (0, 0). Stack-based scan: O(n) time and space.

>>> longest_valid_parentheses(')()())')
(1, 5)
"""


def longest_valid_parentheses(text):
    if not isinstance(text, str) or any(c not in "()" for c in text):
        raise ValueError("text must contain only parentheses")
    stack, best = [-1], (0, 0)
    for index, char in enumerate(text):
        if char == "(":
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            elif index - stack[-1] > best[1] - best[0]:
                best = (stack[-1] + 1, index + 1)
    return best

"""Check (), [], and {} nesting in O(n) time and O(n) worst-case stack space.

Other characters are ignored. This is a bracket checker, not a language parser:
brackets inside quoted strings or comments still participate in matching.

>>> balanced_brackets('sum([a, {b: c}])')
True
>>> balanced_brackets('([)]')
False
"""


def balanced_brackets(text: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs and (not stack or stack.pop() != pairs[char]):
            return False
    return not stack

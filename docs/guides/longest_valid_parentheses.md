# Locate a longest balanced parentheses span

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_valid_parentheses.py)

## Reasoning

A stack records unmatched opening positions and the boundary before the current valid region. Matching a close reveals the start boundary of a valid suffix, while an unmatched close resets the region. Tracking the longest such suffix produces slice coordinates rather than merely validating the whole string.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_valid_parentheses import longest_valid_parentheses
>>> text = "(()())("
>>> start, stop = longest_valid_parentheses(text)
>>> start, stop, text[start:stop]
(0, 6, '(()())')
>>> longest_valid_parentheses(")))")
(0, 0)
>>> longest_valid_parentheses("()(()")
(0, 2)

```

## Boundary to remember

Only opening and closing parentheses are accepted. Other bracket kinds or ordinary text require a different parser. A result of (0, 0) means no nonempty valid span exists.

## Practice exercise

Choose the earliest of two equally long balanced spans separated by an unmatched close. Check every candidate with an independent running-balance parser.

```pycon
>>> from algorithm_lab.longest_valid_parentheses import longest_valid_parentheses
>>> text = ")((())))(()())("
>>> bounds = longest_valid_parentheses(text)
>>> bounds, text[bounds[0] : bounds[1]]
((1, 7), '((()))')
>>> def balanced(fragment):
...     balance = 0
...     for char in fragment:
...         balance += 1 if char == "(" else -1
...         if balance < 0:
...             return False
...     return balance == 0
>>> spans = [
...     (start, stop)
...     for start in range(len(text))
...     for stop in range(start + 1, len(text) + 1)
...     if balanced(text[start:stop])
... ]
>>> assert bounds == min(spans, key=lambda span: (-(span[1] - span[0]), span[0]))

```

The extra close resets the usable start boundary, so the two six-character spans cannot be joined. A zero final balance alone is insufficient: an interval that becomes negative partway through is invalid. The independent parser checks that prefix condition and the earliest-start tie.

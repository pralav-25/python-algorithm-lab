# Locate a longest balanced parentheses span

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_valid_parentheses.py)

## Reasoning

A stack records unmatched opening positions and the boundary before the current valid region. Matching a close reveals the start boundary of a valid suffix, while an unmatched close resets the region. Tracking the longest such suffix produces slice coordinates rather than merely validating the whole string.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_valid_parentheses import longest_valid_parentheses
>>> text = '(()())('
>>> start, stop = longest_valid_parentheses(text)
>>> start, stop, text[start:stop]
(0, 6, '(()())')
>>> longest_valid_parentheses(')))')
(0, 0)
>>> longest_valid_parentheses('()(()')
(0, 2)

```

## Boundary to remember

Only opening and closing parentheses are accepted. Other bracket kinds or ordinary text require a different parser. A result of (0, 0) means no nonempty valid span exists.

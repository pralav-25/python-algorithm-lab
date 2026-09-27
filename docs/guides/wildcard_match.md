# Match an entire name with star and question mark

[Guide index](../README.md) · [Implementation](../../algorithm_lab/wildcard_match.py)

## Reasoning

A question mark consumes exactly one character. A star either consumes nothing or extends the characters already consumed by that same star. Dynamic programming combines those possibilities without exponential backtracking, and the final cell asks whether the complete text was consumed.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.wildcard_match import wildcard_match
>>> wildcard_match("image-07.png", "image-??.png")
True
>>> wildcard_match("image-007.png", "image-??.png")
False
>>> wildcard_match("notes.txt", "*.txt")
True
>>> wildcard_match("a", "[ab]")
False
>>> wildcard_match("", "*")
True

```

## Boundary to remember

Only ? and * are operators. Brackets and backslashes are literal characters, so this is neither a regular-expression engine nor a complete shell glob implementation.

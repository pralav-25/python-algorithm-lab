# Match an entire string against literals, dot wildcards and star repetition.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/regex_match.py)

## Reasoning

Dynamic programming tracks whether each text prefix matches each pattern prefix. A star either consumes zero copies of its preceding token or consumes one matching character and keeps that token active.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.regex_match import regex_match

print(repr(regex_match('aab', 'c*a*b')))  # True
```

## Boundary to remember

The matcher supports only literal characters, dot, and star, and it requires the entire text to match. Leading and adjacent stars are invalid; there is no escaping syntax.

## Practice exercise

Validate a complete short identifier with an optional repeated prefix and a wildcard character.

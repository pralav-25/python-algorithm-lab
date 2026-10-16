# Return the fewest inserted characters needed to make a palindrome.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_insertions_palindrome.py)

## Reasoning

For an interval, matching end characters can stay in place and leave the inner interval. If the ends differ, insert a copy of one endpoint and solve the smaller interval that would then be mirrored; the recurrence returns only the minimum count.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.minimum_insertions_palindrome import minimum_insertions_palindrome

print(repr(minimum_insertions_palindrome('mbadm')))  # 2
```

## Boundary to remember

Existing characters remain in order, and insertions may be placed anywhere. The result is a count, so when multiple palindromes are optimal no reconstruction tie rule is needed.

## Practice exercise

Find the minimum edits by insertion needed to turn a short label into a palindrome without reordering its original letters.

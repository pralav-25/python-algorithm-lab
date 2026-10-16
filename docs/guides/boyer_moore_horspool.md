# Find exact substring matches with Boyer-Moore-Horspool shifts.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/boyer_moore_horspool.py)

## Reasoning

Compare the pattern from right to left. After a mismatch, the character immediately beyond the aligned window determines how far the next alignment can safely move. A last-occurrence table makes these shifts cheap while still checking every reported match exactly.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.boyer_moore_horspool import boyer_moore_horspool

print(repr(boyer_moore_horspool('bananana', 'ana')))  # [1, 3, 5]
```

## Boundary to remember

Overlapping matches are included. An empty pattern matches all n+1 boundaries, and Unicode characters are compared literally without normalization.

## Practice exercise

Search a long log line for every occurrence of a short token, including matches that overlap.

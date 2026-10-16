# Find exact substring matches using Sunday's look-ahead shifts.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/sunday_search.py)

## Reasoning

After checking one alignment, inspect the text character immediately after the pattern window. The next occurrence of that character in the pattern determines a safe shift; if it is absent, the whole pattern can move past it.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.sunday_search import sunday_search

print(repr(sunday_search('aaaa', 'aa')))  # [0, 1, 2]
```

## Boundary to remember

All overlapping matches are returned in order, and an empty pattern matches every boundary. Characters are literal Unicode code points with no normalization.

## Practice exercise

Find every overlapping occurrence of a short marker in a longer text using look-ahead shifts.

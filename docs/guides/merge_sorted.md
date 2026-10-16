# Merge two ascending iterables into a new list, retaining duplicates.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/merge_sorted.py)

## Reasoning

Keep one cursor in each ascending input and repeatedly emit the smaller next key. When keys tie, consuming from the first input first gives a deterministic stable merge across both streams.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.merge_sorted import merge_sorted

print(repr(merge_sorted([1, 3, 3], [2, 3, 5])))  # [1, 2, 3, 3, 3, 5]
```

## Boundary to remember

Sortedness is assumed rather than checked. Duplicates remain, each key is evaluated once, and the returned list does not mutate either input.

## Practice exercise

Merge two ordered event feeds while preserving duplicates and keeping the first feed ahead on equal keys.

# Return the length of the longest consecutive run in an integer iterable.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_consecutive.py)

## Reasoning

A run only needs to be expanded from its smallest member. If x-1 is present, x is inside another run and should not start a scan; otherwise walk upward until the run ends.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.longest_consecutive import longest_consecutive

print(repr(longest_consecutive([100, 4, 200, 1, 3, 2, 2])))  # 4
```

## Boundary to remember

Duplicates do not extend a run, signed integers are supported, and the original iterable is preserved by working with a set copy.

## Practice exercise

Measure the longest uninterrupted sequence of integer identifiers even when input order is arbitrary.

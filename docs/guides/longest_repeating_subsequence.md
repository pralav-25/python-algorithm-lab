# Return the length of a subsequence repeated at distinct aligned indices.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_repeating_subsequence.py)

## Reasoning

Run a longest-common-subsequence recurrence between the string and itself, but forbid matching a position to itself. The distinct-index rule lets two subsequence occurrences share characters in value while using separate source positions.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.longest_repeating_subsequence import longest_repeating_subsequence

print(repr(longest_repeating_subsequence('aabebcdd')))  # 3
```

## Boundary to remember

Only the length is returned. The two copies may overlap in the original string, but each aligned pair must use different indices.

## Practice exercise

Count the length of the longest repeated pattern that can be read twice in order from one string.

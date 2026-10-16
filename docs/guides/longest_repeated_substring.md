# Find a longest substring occurring at least twice, allowing overlaps.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_repeated_substring.py)

## Reasoning

Compare the common prefixes of pairs of suffixes. A repeated substring is exactly a shared prefix of two different suffix starts, and the implementation retains the longest one while applying a deterministic earliest-start tie rule.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.longest_repeated_substring import longest_repeated_substring

print(repr(longest_repeated_substring('banana')))  # 'ana'
```

## Boundary to remember

Overlapping occurrences are allowed. The result is one substring, not a set of all repeats; equal-length ties prefer the earliest start in the original text.

## Practice exercise

Find the longest repeated fragment in a short DNA or log string while allowing the copies to overlap.

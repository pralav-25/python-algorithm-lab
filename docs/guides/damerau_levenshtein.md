# Compute unrestricted unit-cost Damerau-Levenshtein distance.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/damerau_levenshtein.py)

## Reasoning

Insertion, deletion, and substitution use the familiar edit-distance recurrence. Unrestricted adjacent transpositions require remembering the last row and column where each character appeared; that lets a transposition jump across an intervening substring without treating it as a restricted one-time swap.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.damerau_levenshtein import damerau_levenshtein

print(repr(damerau_levenshtein('CA', 'ABC')))  # 2
```

## Boundary to remember

This is unrestricted Damerau-Levenshtein distance, so one substring may participate in several edits. It differs from optimal string alignment, which limits repeated edits to the same substring.

## Practice exercise

Measure the edits needed to transform a mistyped two-character code into a target where one transposition is useful.

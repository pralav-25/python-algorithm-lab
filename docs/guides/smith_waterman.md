# Return the optimal local alignment score with linear gap penalties.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/smith_waterman.py)

## Reasoning

Each local-alignment cell takes the best of starting fresh at zero, extending a match or mismatch diagonally, or adding a gap. Resetting negative paths prevents a poor prefix from reducing the score of a later matching region.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.smith_waterman import smith_waterman

print(repr(smith_waterman('GGTTGACTA', 'TGTTACGG')))  # 9
```

## Boundary to remember

A match score must be positive, while mismatch and gap scores are nonpositive. The function returns only the best score, not the aligned substring or its coordinates.

## Practice exercise

Find the strongest matching region between two strings when unrelated prefixes and suffixes should not lower the score.

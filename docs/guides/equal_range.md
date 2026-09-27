# Count repeated keys with two binary boundaries

[Guide index](../README.md) · [Implementation](../../algorithm_lab/equal_range.py)

## Reasoning

One binary search finds the first position not smaller than the target; another finds the first position greater than it. Their half-open interval contains exactly the equal keys. Subtracting the boundaries counts duplicates without scanning them, even when the duplicate block is very large.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.equal_range import equal_range
>>> scores = [10, 20, 20, 20, 40]
>>> start, stop = equal_range(scores, 20)
>>> scores[start:stop], stop - start
([20, 20, 20], 3)
>>> equal_range(scores, 30)
(4, 4)
>>> equal_range([], 20)
(0, 0)

```

## Boundary to remember

An absent target produces equal boundaries at its insertion point, not -1. The input must already be sorted according to the same ordering used for the search.

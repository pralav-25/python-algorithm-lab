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

## Practice exercise

Insert a new score immediately after all existing copies of the same score. Use the upper boundary and confirm that the table remains sorted.

```pycon
>>> from algorithm_lab.equal_range import equal_range
>>> scores = [3, 7, 7, 7, 12]
>>> start, stop = equal_range(scores, 7)
>>> scores.insert(stop, 7)
>>> scores
[3, 7, 7, 7, 7, 12]
>>> assert stop - start == 3
>>> assert equal_range(scores, 7) == (1, 5)

```

The original stop is the first index greater than seven, so inserting there places the new item after the existing equal block. The count before insertion uses the old boundaries, which must be recomputed after changing the sequence.

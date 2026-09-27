# Track reachable totals with a bitset

[Guide index](../README.md) · [Implementation](../../algorithm_lab/subset_sum.py)

## Reasoning

Bit position s represents whether total s is reachable. Shifting the current bitset by a new value represents adding that value to every previously reachable total; OR keeps both choices. Updating from the old bitset once per value enforces the rule that each occurrence can be used at most once.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.subset_sum import subset_sum
>>> subset_sum([4, 9, 13], 17)
True
>>> subset_sum([4], 8)
False
>>> subset_sum([4, 4], 8)
True
>>> subset_sum([], 0)
True
>>> subset_sum([10**50], 3)
False

```

## Boundary to remember

The target controls memory, even if there are very few values. Negative values are outside this representation, and the empty subset already reaches zero.

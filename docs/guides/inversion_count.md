# Measure how far a ranking is from sorted

[Guide index](../README.md) · [Implementation](../../algorithm_lab/inversion_count.py)

## Reasoning

When merging two sorted halves, choosing a smaller right-hand value skips every remaining value in the left half. Those skipped pairs are all inversions, so one comparison counts many pairs at once. This gives an n log n count without explicitly materializing every out-of-order pair.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.inversion_count import inversion_count
>>> ranks = [4, 1, 3, 2]
>>> inversion_count(ranks)
4
>>> brute = sum(ranks[i] > ranks[j] for i in range(len(ranks)) for j in range(i+1, len(ranks)))
>>> assert inversion_count(ranks) == brute
>>> inversion_count([2, 2, 2])
0

```

## Boundary to remember

Equal values are not inversions. The count describes pairwise disorder, not the number of arbitrary swaps required to sort a list.

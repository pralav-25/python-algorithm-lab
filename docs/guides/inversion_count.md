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
>>> brute = sum(ranks[i] > ranks[j] for i in range(len(ranks)) for j in range(i + 1, len(ranks)))
>>> assert inversion_count(ranks) == brute
>>> inversion_count([2, 2, 2])
0

```

## Boundary to remember

Equal values are not inversions. The count describes pairwise disorder, not the number of arbitrary swaps required to sort a list.

## Practice exercise

Compute the greatest possible pairwise disorder for a ranking with repeated scores. Start in descending order and subtract equal-score pairs from the total pair count.

```pycon
>>> from collections import Counter
>>> from math import comb
>>> from algorithm_lab.inversion_count import inversion_count
>>> descending = [5, 5, 2, 2, 1]
>>> possible_pairs = comb(len(descending), 2)
>>> tied_pairs = sum(comb(count, 2) for count in Counter(descending).values())
>>> inversion_count(descending), possible_pairs - tied_pairs
(8, 8)
>>> assert inversion_count(sorted(descending)) == 0

```

Every unequal pair in a nonincreasing ranking is an inversion, but the two equal-score pairs contribute nothing. This counting argument supplies an independent expected value. Treating a tie as an inversion would incorrectly return all ten possible pairs.

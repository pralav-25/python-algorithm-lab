# Encode a permutation with skipped factorial blocks

[Guide index](../README.md) · [Implementation](../../algorithm_lab/permutation_rank.py)

## Reasoning

At each position, count the unused smaller values that could have appeared there. Each such choice precedes an entire factorial-sized block of suffix permutations. The resulting mixed-radix digits form a Lehmer code, which uniquely determines the lexicographic rank.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.permutation_rank import permutation_rank
>>> from itertools import permutations
>>> orders = list(permutations(range(4)))
>>> assert all(permutation_rank(order) == rank for rank, order in enumerate(orders))
>>> permutation_rank([3, 2, 1, 0])
23
>>> permutation_rank([])
0

```

## Boundary to remember

The input must be a permutation of consecutive integers starting at zero. Repeated values belong to multiset permutation enumeration and need different ranking rules.

## Practice exercise

Encode a named ordering by first mapping its labels to a fixed sorted
alphabet, then verify the skipped factorial blocks by hand.

```pycon
>>> from algorithm_lab.permutation_rank import permutation_rank
>>> from math import factorial
>>> alphabet = ["amber", "blue", "cyan", "denim"]
>>> ordering = ["cyan", "amber", "denim", "blue"]
>>> labels = {name: index for index, name in enumerate(alphabet)}
>>> encoded = [labels[name] for name in ordering]
>>> encoded
[2, 0, 3, 1]
>>> permutation_rank(encoded)
13
>>> assert permutation_rank(encoded) == 2 * factorial(3) + 0 * factorial(2) + 1 * factorial(1)

```

The first choice skips two blocks of six arrangements. After those
values are removed, the third choice skips one remaining suffix block;
ranks depend on this fixed alphabet, not the labels' arrival order.

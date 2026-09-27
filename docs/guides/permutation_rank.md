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

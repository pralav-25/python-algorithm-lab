# Locate a selection in lexicographic enumeration

[Guide index](../README.md) · [Implementation](../../algorithm_lab/combination_rank.py)

## Reasoning

For each chosen position, count combinations beginning with each smaller still-available choice. Binomial counts skip those entire blocks at once. Adding the skipped block sizes yields the zero-based position without generating all previous combinations.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.combination_rank import combination_rank
>>> from itertools import combinations
>>> choices = list(combinations(range(6), 3))
>>> chosen = [1, 3, 5]
>>> rank = combination_rank(6, chosen)
>>> assert choices[rank] == tuple(chosen)
>>> combination_rank(6, [0, 1, 2]), combination_rank(6, [])
(0, 0)

```

## Boundary to remember

The input must be strictly increasing and drawn from range(n). The order is lexicographic, which differs from some combinatorial-number-system rank conventions.

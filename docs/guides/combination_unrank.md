# Jump directly to a ranked selection

[Guide index](../README.md) · [Implementation](../../algorithm_lab/combination_unrank.py)

## Reasoning

Candidate first choices divide the lexicographic list into blocks whose sizes are binomial coefficients. Subtract whole block sizes until the desired rank lies in one block, then repeat for the next position. This lets a caller access a sample of combinations without walking through earlier answers.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.combination_unrank import combination_unrank
>>> from itertools import combinations
>>> choices = list(combinations(range(6), 3))
>>> assert all(tuple(combination_unrank(6, 3, rank)) == choice for rank, choice in enumerate(choices))
>>> combination_unrank(6, 3, 0)
[0, 1, 2]
>>> combination_unrank(6, 0, 0)
[]

```

## Boundary to remember

Ranks run from zero through C(n,k)-1. The empty combination is a real single result at rank zero, not an absence of combinations.

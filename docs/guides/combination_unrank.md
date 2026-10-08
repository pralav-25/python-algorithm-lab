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

## Practice exercise

Build the second four-entry page of the lexicographic two-item catalog for five items, starting at zero-based rank four.

```pycon
>>> from itertools import combinations
>>> from algorithm_lab.combination_unrank import combination_unrank
>>> page = [combination_unrank(5, 2, rank) for rank in range(4, 8)]
>>> page
[[1, 2], [1, 3], [1, 4], [2, 3]]
>>> assert page == [list(row) for row in list(combinations(range(5), 2))[4:8]]

```

Unranking reaches each requested selection directly, so a large catalog does not need to enumerate all preceding pages. The small explicit catalog here serves only as an independent check of the paging convention.

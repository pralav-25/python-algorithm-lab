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

## Practice exercise

Encode a selected three-person team from an alphabetically ordered roster. Compare its rank with a small explicit list of every possible team.

```pycon
>>> from itertools import combinations
>>> from algorithm_lab.combination_rank import combination_rank
>>> roster = ["Ada", "Bo", "Cy", "Dee", "Eli", "Fay"]
>>> selected = ["Bo", "Dee", "Fay"]
>>> indices = [roster.index(person) for person in selected]
>>> rank = combination_rank(len(roster), indices)
>>> all_teams = list(combinations(roster, 3))
>>> assert all_teams[rank] == tuple(selected)
>>> assert rank == list(combinations(range(6), 3)).index(tuple(indices))

```

The rank depends on roster order and team size. Store those conventions alongside the integer if it will be decoded later; the rank alone cannot identify names or distinguish catalogs of different sizes.

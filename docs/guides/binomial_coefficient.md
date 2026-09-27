# Count teams without enumerating them

[Guide index](../README.md) · [Implementation](../../algorithm_lab/binomial_coefficient.py)

## Reasoning

Choosing k members from n ignores order, so enumerating permutations would overcount by k factorial. The multiplicative recurrence builds the exact combination count through small integral divisions. Symmetry between choosing members and choosing who stays out reduces the number of arithmetic steps.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.binomial_coefficient import binomial_coefficient
>>> from itertools import combinations
>>> binomial_coefficient(8, 3)
56
>>> assert binomial_coefficient(8, 3) == len(list(combinations(range(8), 3)))
>>> assert binomial_coefficient(100, 2) == binomial_coefficient(100, 98)
>>> binomial_coefficient(3, 4), binomial_coefficient(0, 0)
(0, 1)

```

## Boundary to remember

The count assumes distinct positions or people. Repeated values in a list are still distinct choices unless the application explicitly deduplicates them first.

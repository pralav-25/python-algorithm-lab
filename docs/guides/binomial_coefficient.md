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

## Practice exercise

Count every possible committee from six people, including the empty committee. Combine the counts for each size and explain the result.

```pycon
>>> from algorithm_lab.binomial_coefficient import binomial_coefficient
>>> size_counts = [binomial_coefficient(6, size) for size in range(7)]
>>> size_counts
[1, 6, 15, 20, 15, 6, 1]
>>> assert sum(size_counts) == 2**6

```

Each person independently joins or stays out, yielding 64 subsets. Summing the disjoint size categories counts the same subsets a second way.

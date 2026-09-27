# Recover an increasing progression with gaps

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_increasing_subsequence.py)

## Reasoning

For every achievable length, keep the smallest possible tail. A smaller tail leaves more room for future observations, so replacing a tail cannot reduce the best length. Predecessor links are needed to reconstruct a real subsequence: the tail table alone is not necessarily a path through the original input.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_increasing_subsequence import longest_increasing_subsequence
>>> values = [8, 2, 5, 3, 7]
>>> result = longest_increasing_subsequence(values)
>>> len(result), all(a < b for a, b in zip(result, result[1:]))
(3, True)
>>> remaining = iter(values)
>>> assert all(any(item == wanted for item in remaining) for wanted in result)
>>> longest_increasing_subsequence([4, 4, 4])
[4]

```

## Boundary to remember

Increasing means strictly increasing here, so repeated values do not extend the result. Several longest answers can exist; the chosen answer is deterministic but not promised to be lexicographically smallest.

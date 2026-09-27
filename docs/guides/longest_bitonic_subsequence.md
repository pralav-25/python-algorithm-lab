# Recover an increasing trend followed by a decline

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_bitonic_subsequence.py)

## Reasoning

For every potential peak, combine the longest increasing subsequence ending there with the longest decreasing subsequence beginning there. Subtract one because the peak belongs to both pieces. The best peak and predecessor links reconstruct a single sequence that rises and then falls.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_bitonic_subsequence import longest_bitonic_subsequence
>>> result = longest_bitonic_subsequence([1, 4, 2, 5, 3, 1])
>>> len(result)
5
>>> peak = result.index(max(result))
>>> assert all(a < b for a, b in zip(result[:peak], result[1 : peak + 1]))
>>> assert all(a > b for a, b in zip(result[peak:], result[peak + 1 :]))
>>> longest_bitonic_subsequence([2, 2, 2])
[2]

```

## Boundary to remember

Both slopes are strict, so equal values cannot extend a slope. Either side may be empty, meaning a purely increasing or purely decreasing subsequence is also valid.

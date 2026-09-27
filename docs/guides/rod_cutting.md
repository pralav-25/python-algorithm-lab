# Choose cuts that sell the entire rod

[Guide index](../README.md) · [Implementation](../../algorithm_lab/rod_cutting.py)

## Reasoning

Try each possible first piece and add its price to the best revenue for the remaining length. Reconstructing those first-piece choices returns the actual lengths to sell. This is an unbounded reuse problem because the same piece length may be selected several times.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.rod_cutting import rod_cutting
>>> prices = [2, 5, 7, 8]
>>> revenue, pieces = rod_cutting(prices)
>>> revenue, pieces
(10, [2, 2])
>>> assert sum(pieces) == len(prices) and sum(prices[length - 1] for length in pieces) == revenue
>>> rod_cutting([-2, -3])
(-3, [2])
>>> rod_cutting([])
(0, [])

```

## Boundary to remember

The entire rod must be sold, even if all prices are negative. That requirement differs from a knapsack that may leave capacity unused and choose a zero-value empty solution.

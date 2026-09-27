# Match a pair to a fixed budget

[Guide index](../README.md) · [Implementation](../../algorithm_lab/two_sum.py)

## Reasoning

While scanning prices, store earlier values and ask whether the current price has a complementary earlier value. Looking up the complement before recording the current item prevents using one item twice. Keeping the first index for a repeated price makes the returned pair deterministic.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.two_sum import two_sum
>>> prices = [8, 4, 6, 4]
>>> pair = two_sum(prices, 10)
>>> pair
(1, 2)
>>> assert sum(prices[index] for index in pair) == 10
>>> two_sum([5], 10) is None
True
>>> two_sum([5, 5], 10)
(0, 1)

```

## Boundary to remember

This returns one pair of original indices, not every possible pair. A single item worth half the budget cannot form a pair with itself, while two equal-priced items can.

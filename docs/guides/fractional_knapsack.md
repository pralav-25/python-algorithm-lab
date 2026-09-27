# Allocate capacity by value density

[Guide index](../README.md) · [Implementation](../../algorithm_lab/fractional_knapsack.py)

## Reasoning

When arbitrary fractions are allowed, replacing any lower-density allocation with an equal weight of a higher-density item cannot decrease value. Sorting by value per weight and filling in that order is therefore optimal. Exact rational fractions avoid rounding an allocation over its capacity.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.fractional_knapsack import fractional_knapsack
>>> items = [(4, 20), (6, 18)]
>>> value, fractions = fractional_knapsack(items, 7)
>>> value, fractions
(Fraction(29, 1), [Fraction(1, 1), Fraction(1, 2)])
>>> assert sum(weight * part for (weight, _), part in zip(items, fractions)) == 7
>>> assert sum(price * part for (_, price), part in zip(items, fractions)) == value

```

## Boundary to remember

This greedy argument depends on divisibility. It does not solve the 0/1 knapsack problem where an item must be taken whole or omitted.

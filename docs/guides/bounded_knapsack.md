# Respect limited quantities while maximizing value

[Guide index](../README.md) · [Implementation](../../algorithm_lab/bounded_knapsack.py)

## Reasoning

Binary grouping replaces a bounded stock count with bundles whose quantities can represent every allowed choice. Each bundle then behaves like a 0/1 item in a capacity dynamic program. This reduces the work compared with treating every available copy as a separate item.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.bounded_knapsack import bounded_knapsack
>>> from itertools import product
>>> items = [(2, 3, 2), (3, 6, 1)]
>>> bounded_knapsack(items, 7)
12
>>> brute = max(3 * a + 6 * b for a, b in product(range(3), range(2)) if 2 * a + 3 * b <= 7)
>>> assert bounded_knapsack(items, 7) == brute
>>> bounded_knapsack([(1, -3, 10)], 5)
0

```

## Boundary to remember

Each item is a (weight, value, count) triple, and this API returns only the optimal value. Taking nothing is allowed, so negative-valued inventory need not be used.

## Practice exercise

A warehouse has effectively unlimited two-unit boxes worth seven each and one three-unit box worth twelve. Find the best load under capacity seven.

```pycon
>>> from algorithm_lab.bounded_knapsack import bounded_knapsack
>>> inventory = [(2, 7, 10**12), (3, 12, 1)]
>>> bounded_knapsack(inventory, 7)
26
>>> assert bounded_knapsack(inventory, 7) == bounded_knapsack([(2, 7, 3), (3, 12, 1)], 7)

```

Only three two-unit boxes could fit even without the other item. Two such boxes plus the three-unit box earn 26; three two-unit boxes earn only 21. Stock beyond the capacity-imposed bound cannot improve the result.

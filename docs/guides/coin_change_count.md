# Count payments without counting coin order

[Guide index](../README.md) · [Implementation](../../algorithm_lab/coin_change_count.py)

## Reasoning

Process denominations in an outer loop and reachable amounts in ascending order. Reusing the current denomination permits unlimited copies, while fixing denomination order prevents a payment from being recounted for every ordering of its coins. The initial count at amount zero represents the empty payment.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.coin_change_count import coin_change_count
>>> from itertools import product
>>> coin_change_count([2, 3, 5], 10)
4
>>> brute = sum(2*a + 3*b + 5*c == 10 for a, b, c in product(range(6), range(4), range(3)))
>>> assert coin_change_count([2, 3, 5], 10) == brute
>>> coin_change_count([2, 2], 4), coin_change_count([], 0)
(1, 1)

```

## Boundary to remember

Counting payments is different from minimizing the number of coins. Duplicate denomination entries are ignored; they do not represent distinct coin types or a limited supply.

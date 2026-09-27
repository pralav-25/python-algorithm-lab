# Count valid balanced structures without listing them

[Guide index](../README.md) · [Implementation](../../algorithm_lab/catalan_number.py)

## Reasoning

Catalan numbers count several recursively balanced structures, including well-formed parentheses and full binary tree shapes. Choosing the structure surrounding the first matched pair separates the remaining work into two smaller balanced structures. The implementation uses an exact multiplicative recurrence to compute the count efficiently.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.catalan_number import catalan_number
>>> from math import comb
>>> catalan_number(4)
14
>>> assert all(catalan_number(n) == comb(2 * n, n) // (n + 1) for n in range(9))
>>> catalan_number(0)
1

```

## Boundary to remember

For parentheses, n counts pairs rather than characters. Catalan counts are not the count of every string containing n opening and n closing parentheses, because prefixes must also be balanced.

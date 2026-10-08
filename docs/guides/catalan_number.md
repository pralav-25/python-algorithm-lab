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

## Practice exercise

Count balanced strings containing three opening and three closing parentheses by enumerating all opening-position choices and enforcing prefix balance.

```pycon
>>> from itertools import combinations
>>> from algorithm_lab.catalan_number import catalan_number
>>> candidates = [
...     tuple(1 if i in openings else -1 for i in range(6)) for openings in combinations(range(6), 3)
... ]
>>> balanced = [row for row in candidates if all(sum(row[:stop]) >= 0 for stop in range(1, 7))]
>>> len(candidates), len(balanced)
(20, 5)
>>> assert len(balanced) == catalan_number(3)

```

Equal total counts leave twenty candidates. Requiring every prefix to contain at least as many openings as closings removes the strings that close too early, leaving the five Catalan structures.

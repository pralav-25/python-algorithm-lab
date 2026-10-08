# Multiply polynomials by combining degree pairs

[Guide index](../README.md) · [Implementation](../../algorithm_lab/polynomial_multiply.py)

## Reasoning

Multiplying a term of degree i by one of degree j contributes to degree i+j. Accumulating every such pair is a discrete convolution of the coefficient lists. Integer arithmetic preserves the algebraic identity exactly, and trimming high-degree zeros gives one canonical representation of the product.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.polynomial_multiply import polynomial_multiply
>>> from algorithm_lab.polynomial_evaluate import polynomial_evaluate
>>> left, right = [1, 1], [1, -1]
>>> product = polynomial_multiply(left, right)
>>> product
[1, 0, -1]
>>> assert all(
...     polynomial_evaluate(product, x) == polynomial_evaluate(left, x) * polynomial_evaluate(right, x)
...     for x in [-2, 0, 3]
... )
>>> polynomial_multiply([0], [1, 2])
[]

```

## Boundary to remember

Coefficients are ordered from constant term upward. The zero polynomial is an empty list, so output length need not equal the sum of input lengths minus one.

## Practice exercise

Count the sum outcomes of two three-sided dice by multiplying their
count-generating polynomials, then compare with explicit outcomes.

```pycon
>>> from algorithm_lab.polynomial_multiply import polynomial_multiply
>>> from itertools import product
>>> from collections import Counter
>>> die = [0, 1, 1, 1]
>>> counts = polynomial_multiply(die, die)
>>> counts
[0, 0, 1, 2, 3, 2, 1]
>>> outcomes = Counter(a + b for a, b in product(range(1, 4), repeat=2))
>>> assert counts == [outcomes[total] for total in range(7)]
>>> assert sum(counts) == 3 * 3

```

A coefficient's degree represents the sum, while its value counts ways
to obtain it. Low-degree zeroes remain necessary placeholders: removing
them would relabel the outcomes rather than canonicalize the polynomial.

# Express an exact rational through Euclidean quotients

[Guide index](../README.md) · [Implementation](../../algorithm_lab/continued_fraction.py)

## Reasoning

Taking the floor separates a rational into an integer part and a remaining fractional part. Inverting the remainder repeats the process, producing the same quotient structure as Euclid’s algorithm. The canonical representation avoids an unnecessary trailing one, so equivalent rational inputs agree.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.continued_fraction import continued_fraction
>>> continued_fraction(7, 3)
[2, 3]
>>> continued_fraction(-7, 3)
[-3, 1, 2]
>>> assert continued_fraction(14, 6) == continued_fraction(7, 3)
>>> continued_fraction(6, 3)
[2]

```

## Boundary to remember

For negative rationals, floor is different from truncation toward zero. Only the first coefficient may be negative; later coefficients describe positive reciprocal remainders.

## Practice exercise

Expand the negative rational minus seven thirds, then reconstruct it from the resulting terms with exact arithmetic.

```pycon
>>> from fractions import Fraction
>>> from algorithm_lab.continued_fraction import continued_fraction
>>> terms = continued_fraction(-7, 3)
>>> terms
[-3, 1, 2]
>>> reconstructed = Fraction(terms[-1])
>>> for term in reversed(terms[:-1]):
...     reconstructed = term + 1 / reconstructed
>>> assert reconstructed == Fraction(-7, 3)

```

The leading term uses floor division, so it is minus three rather than truncating toward zero to minus two. Later terms remain positive, retaining the canonical continued-fraction convention for a negative input.

# Build rational approximations from successive prefixes

[Guide index](../README.md) · [Implementation](../../algorithm_lab/continued_fraction_convergents.py)

## Reasoning

A new continued-fraction term updates the numerator and denominator from their two predecessors. This recurrence yields the value of every prefix without repeatedly evaluating nested reciprocals from scratch. Fractions keep each approximation exact and already reduced.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.continued_fraction_convergents import continued_fraction_convergents
>>> from fractions import Fraction
>>> approximations = continued_fraction_convergents([3, 7, 16])
>>> approximations
[Fraction(3, 1), Fraction(22, 7), Fraction(355, 113)]
>>> assert approximations[-1] == Fraction(3) + 1 / (Fraction(7) + Fraction(1, 16))
>>> continued_fraction_convergents([])
[]

```

## Boundary to remember

Every term after the first must be positive. An arbitrary integer sequence is not automatically a valid simple continued fraction.

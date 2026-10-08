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

## Practice exercise

The first five terms of the continued fraction for the square root of two are one followed by four twos. Check the last convergent's exact Pell identity.

```pycon
>>> from algorithm_lab.continued_fraction_convergents import continued_fraction_convergents
>>> approximations = continued_fraction_convergents([1, 2, 2, 2, 2])
>>> approximations[-1]
Fraction(41, 29)
>>> p, q = approximations[-1].numerator, approximations[-1].denominator
>>> assert p * p - 2 * q * q == -1
>>> assert all(abs(value.numerator**2 - 2 * value.denominator**2) == 1 for value in approximations)

```

The exact residual alternates between one and minus one across these convergents. This supplies an integer certificate of their closeness to the irrational root without comparing rounded decimal representations.

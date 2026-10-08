# Recover a certificate for the greatest common divisor

[Guide index](../README.md) · [Implementation](../../algorithm_lab/extended_gcd.py)

## Reasoning

Euclid’s remainder steps preserve the set of integer combinations of the two inputs. Tracking the coefficients through those same steps gives a certificate a*x + b*y = gcd(a,b). Such coefficients are the bridge from divisibility to modular inverses and linear Diophantine equations.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.extended_gcd import extended_gcd
>>> import math
>>> a, b = -84, 30
>>> divisor, x, y = extended_gcd(a, b)
>>> divisor, a * x + b * y
(6, 6)
>>> assert divisor == math.gcd(a, b)
>>> extended_gcd(0, 0)
(0, 1, 0)

```

## Boundary to remember

The coefficient pair is not unique; verify the identity instead of expecting a particular pair. The returned gcd is nonnegative even when an input is negative.

## Practice exercise

Find an integer solution to `18*x + 30*y = 12`, then derive another solution using the homogeneous step and verify both certificates.

```pycon
>>> from algorithm_lab.extended_gcd import extended_gcd
>>> a, b, target = 18, 30, 12
>>> divisor, x, y = extended_gcd(a, b)
>>> assert target % divisor == 0
>>> x, y = x * (target // divisor), y * (target // divisor)
>>> assert a * x + b * y == target
>>> another = (x + b // divisor, y - a // divisor)
>>> assert a * another[0] + b * another[1] == target

```

Scaling the Bezout coefficients solves any target divisible by the gcd. The added step contributes `a*(b/g) - b*(a/g) = 0`, yielding a family of integer solutions; positivity constraints would need a separate check.

# Undo multiplication in modular arithmetic

[Guide index](../README.md) · [Implementation](../../algorithm_lab/modular_inverse.py)

## Reasoning

An inverse x satisfies a*x congruent to one modulo m. Extended Euclid supplies such an x exactly when the gcd of a and m is one. Reducing the resulting coefficient modulo m chooses the unique nonnegative representative of all equivalent inverses.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.modular_inverse import modular_inverse
>>> inverse = modular_inverse(7, 26)
>>> inverse
15
>>> assert (7 * inverse) % 26 == 1
>>> modular_inverse(-7, 26)
11
>>> assert (-7 * modular_inverse(-7, 26)) % 26 == 1

```

## Boundary to remember

Ordinary division is not valid modulo a number. If the multiplier and modulus share a factor, an inverse does not exist and this function raises ValueError.

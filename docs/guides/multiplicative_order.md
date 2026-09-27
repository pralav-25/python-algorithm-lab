# Find the cycle length of repeated modular multiplication

[Guide index](../README.md) · [Implementation](../../algorithm_lab/multiplicative_order.py)

## Reasoning

Starting from one, repeatedly multiply by an invertible residue modulo m. The first return to one gives its multiplicative order. Minimality matters: a later exponent that also returns one is a multiple of the order, not necessarily the order itself.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.multiplicative_order import multiplicative_order
>>> base, modulus = 3, 7
>>> order = multiplicative_order(base, modulus)
>>> order
6
>>> assert pow(base, order, modulus) == 1
>>> assert all(pow(base, exponent, modulus) != 1 for exponent in range(1, order))
>>> multiplicative_order(1, 19)
1

```

## Boundary to remember

The base must be coprime to the modulus. This direct educational search may perform many modular multiplications; it does not factor the group order to accelerate large cases.

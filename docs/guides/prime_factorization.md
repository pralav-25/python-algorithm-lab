# Decompose an integer into prime multiplicities

[Guide index](../README.md) · [Implementation](../../algorithm_lab/prime_factorization.py)

## Reasoning

Repeatedly dividing out a factor records its multiplicity and shrinks the remaining problem. After trial factors pass the square root of the remainder, any remainder greater than one must itself be prime. The factor map provides an exact reconstruction certificate by multiplying prime powers.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.prime_factorization import prime_factorization
>>> from math import prod
>>> factors = prime_factorization(300)
>>> factors
{2: 2, 3: 1, 5: 2}
>>> assert prod(prime**exponent for prime, exponent in factors.items()) == 300
>>> prime_factorization(1)
{}

```

## Boundary to remember

Trial division is a teaching approach for modest integers. Large semiprimes can require impractical work; exact arithmetic alone does not make the method suitable for cryptographic-size factorization.

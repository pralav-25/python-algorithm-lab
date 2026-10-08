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

## Practice exercise

Use the prime exponents of seven hundred fifty-six to count all its
positive divisors, and verify the count by direct divisibility checks.

```pycon
>>> from algorithm_lab.prime_factorization import prime_factorization
>>> from math import prod
>>> value = 756
>>> factors = prime_factorization(value)
>>> factors
{2: 2, 3: 3, 7: 1}
>>> divisor_count = prod(exponent + 1 for exponent in factors.values())
>>> divisor_count
24
>>> assert divisor_count == sum(value % divisor == 0 for divisor in range(1, value + 1))
>>> assert prod(prime**exponent for prime, exponent in factors.items()) == value

```

A divisor independently chooses each prime exponent from zero through
its recorded maximum. This makes the count a product of exponent counts,
so treating repeated factors as distinct primes would overcount.

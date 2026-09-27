# Enumerate primes by crossing out composites

[Guide index](../README.md) · [Implementation](../../algorithm_lab/prime_sieve.py)

## Reasoning

A composite number has a prime factor no larger than its square root. Once a prime p is reached, smaller multiples of p have already been marked by smaller factors, so marking can start at p squared. A dense flag array is efficient when many primality answers are needed up to one bound.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.prime_sieve import prime_sieve
>>> primes = prime_sieve(17)
>>> primes
[2, 3, 5, 7, 11, 13, 17]
>>> assert all(all(p % divisor for divisor in range(2, p)) for p in primes)
>>> prime_sieve(1)
[]

```

## Boundary to remember

The bound is inclusive, and zero and one are not primes. A sieve allocates storage across the whole interval; it is not the right tool for testing one extremely large integer.

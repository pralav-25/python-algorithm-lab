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

## Practice exercise

Find twin-prime pairs below fifty and verify the complete prime list
with independent trial division, including a prime-square boundary.

```pycon
>>> from algorithm_lab.prime_sieve import prime_sieve
>>> from math import isqrt
>>> primes = prime_sieve(49)
>>> expected = [
...     candidate
...     for candidate in range(2, 50)
...     if all(candidate % divisor for divisor in range(2, isqrt(candidate) + 1))
... ]
>>> assert primes == expected
>>> prime_set = set(primes)
>>> twins = [(prime, prime + 2) for prime in primes if prime + 2 in prime_set]
>>> twins
[(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
>>> assert 49 not in prime_set and prime_sieve(47)[-1] == 47

```

Seven's square must be marked even when it equals the inclusive limit.
Checking the entire expected list catches missing primes as well as
false positives; set membership then finds each twin pair once.

# Find primes inside a narrow interval

[Guide index](../README.md) · [Implementation](../../algorithm_lab/segmented_sieve.py)

## Reasoning

First find the small primes needed to mark composites, then mark only the requested interval. The first multiple to mark must lie inside the interval and be at least the prime’s square. This avoids allocating flags for every integer below the starting bound.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.segmented_sieve import segmented_sieve
>>> segmented_sieve(20, 40)
[23, 29, 31, 37]
>>> segmented_sieve(2, 3)
[2]
>>> segmented_sieve(0, 2), segmented_sieve(7, 7)
([], [])
>>> assert segmented_sieve(40, 50) == [41, 43, 47]

```

## Boundary to remember

The interval is half-open: start is included and stop is excluded. Memory still includes base primes up to the square root of the upper bound, so a narrow interval near a huge number is not free.

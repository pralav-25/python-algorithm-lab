# Build divisor lists for a whole interval

[Guide index](../README.md) · [Implementation](../../algorithm_lab/divisor_sieve.py)

## Reasoning

Every positive d is a divisor of d, 2d, 3d, and so on. Appending d to those multiples constructs all divisor lists together and naturally keeps them sorted. This shares work across many queries instead of separately trial-dividing every number.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.divisor_sieve import divisor_sieve
>>> divisors = divisor_sieve(12)
>>> divisors[12]
[1, 2, 3, 4, 6, 12]
>>> assert all(divisors[n] == [d for d in range(1, n + 1) if n % d == 0] for n in range(1, 13))
>>> divisors[0], divisors[1]
([], [1])

```

## Boundary to remember

The output includes a list for every index through the inclusive limit. Index zero is empty because the set of positive divisors of zero is not finite.

# Record square-free factor parity

[Guide index](../README.md) · [Implementation](../../algorithm_lab/mobius_sieve.py)

## Reasoning

The Mobius function vanishes when a square of a prime divides the input. Otherwise its sign records whether the number of distinct prime factors is even or odd. A sieve shares factor information across an entire range, enabling divisor-sum identities and inversion formulas.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.mobius_sieve import mobius_sieve
>>> mu = mobius_sieve(12)
>>> mu[1], mu[6], mu[12]
(1, 1, 0)
>>> assert all(sum(mu[d] for d in range(1, n+1) if n % d == 0) == int(n == 1) for n in range(1, 13))
>>> mobius_sieve(0)
[0]

```

## Boundary to remember

Index zero is an unused sentinel. The meaningful identity sums mu(d) over positive divisors and equals one only for n=1; zero values do not mean the number has no factors.

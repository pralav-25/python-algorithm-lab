# Count the invertible residue classes

[Guide index](../README.md) · [Implementation](../../algorithm_lab/euler_totient.py)

## Reasoning

For each distinct prime factor p of n, remove the fraction of candidates divisible by p. Repeated powers of that prime require no additional distinct exclusion step. The result counts residues relatively prime to n and therefore also counts invertible residue classes modulo n.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.euler_totient import euler_totient
>>> from math import gcd
>>> euler_totient(30)
8
>>> assert euler_totient(30) == sum(gcd(value, 30) == 1 for value in range(1, 31))
>>> euler_totient(13), euler_totient(1)
(12, 1)

```

## Boundary to remember

Factoring by trial division dominates the cost for large inputs. The convention phi(1)=1 is intentional even though modular arithmetic modulo one behaves differently from larger moduli.

## Practice exercise

Count invertible clock multipliers modulo twenty. List them directly and verify Euler's exponent identity for every listed multiplier.

```pycon
>>> from math import gcd
>>> from algorithm_lab.euler_totient import euler_totient
>>> multipliers = [value for value in range(20) if gcd(value, 20) == 1]
>>> multipliers
[1, 3, 7, 9, 11, 13, 17, 19]
>>> assert len(multipliers) == euler_totient(20)
>>> assert all(pow(value, euler_totient(20), 20) == 1 for value in multipliers)

```

Only coprime residues have modular inverses. Euler's identity applies to those residues; it must not be asserted for a multiplier such as two that shares a factor with the clock modulus.

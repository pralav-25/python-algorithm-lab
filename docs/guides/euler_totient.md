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

# Combine repeating schedules with compatible offsets

[Guide index](../README.md) · [Implementation](../../algorithm_lab/chinese_remainder.py)

## Reasoning

Each constraint defines a repeating set of integer times. Merging two schedules requires their offsets to agree modulo the gcd of their periods. Extended Euclid then finds one shared time, and the least common multiple gives the new repeating period. Coprime periods are a convenient special case rather than a requirement.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.chinese_remainder import chinese_remainder
>>> constraints = [(1, 4), (3, 6)]
>>> time, period = chinese_remainder(constraints)
>>> time, period
(9, 12)
>>> assert all(time % modulus == remainder for remainder, modulus in constraints)
>>> assert all((time + period) % modulus == remainder for remainder, modulus in constraints)
>>> chinese_remainder([])
(0, 1)

```

## Boundary to remember

A returned solution is the smallest nonnegative representative, not necessarily a strictly positive time. Incompatible constraints raise ValueError instead of producing a misleading partial answer.

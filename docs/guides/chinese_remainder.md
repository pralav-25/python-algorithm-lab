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

## Practice exercise

Two repeating jobs run at offsets two modulo five and four modulo seven. Find their first shared run at or after time 100.

```pycon
>>> from algorithm_lab.chinese_remainder import chinese_remainder
>>> first, period = chinese_remainder([(2, 5), (4, 7)])
>>> first, period
(32, 35)
>>> deadline = 100
>>> cycles = max(0, (deadline - first + period - 1) // period)
>>> next_run = first + cycles * period
>>> next_run
102
>>> assert next_run % 5 == 2 and next_run % 7 == 4 and next_run - period < deadline

```

The solver returns one representative and the repeating period. A ceiling division advances that representative past the deadline without scanning each time.

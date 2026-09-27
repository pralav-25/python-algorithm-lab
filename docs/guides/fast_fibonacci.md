# Advance a recurrence by doubling its index

[Guide index](../README.md) · [Implementation](../../algorithm_lab/fast_fibonacci.py)

## Reasoning

A pair of consecutive Fibonacci values determines the values at twice their index. Processing the index bits therefore reaches F(n) in logarithmically many doubling steps instead of n sequential additions. The result is still an exact Python integer, whose size grows with the requested index.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.fast_fibonacci import fast_fibonacci
>>> fast_fibonacci(12)
144
>>> n = 100
>>> assert fast_fibonacci(n + 2) == fast_fibonacci(n + 1) + fast_fibonacci(n)
>>> fast_fibonacci(0), fast_fibonacci(1)
(0, 1)
>>> assert fast_fibonacci(30) == 832040

```

## Boundary to remember

Logarithmic step count does not mean constant-sized arithmetic. Large results contain many bits, and multiplying them costs more than multiplying machine integers.

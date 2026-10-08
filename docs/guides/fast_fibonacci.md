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

## Practice exercise

Count ways to climb twelve stairs using steps of size one or two. Compare a small sequential count with the corresponding Fibonacci index.

```pycon
>>> from algorithm_lab.fast_fibonacci import fast_fibonacci
>>> ways = [1, 1]
>>> for stairs in range(2, 13):
...     ways.append(ways[-1] + ways[-2])
>>> ways[12], fast_fibonacci(13)
(233, 233)
>>> assert all(ways[stairs] == fast_fibonacci(stairs + 1) for stairs in range(13))

```

There is one way to climb zero stairs: take no steps. Those starting counts shift the recurrence by one, so an n-stair problem uses F(n+1), not F(n). Fast doubling can jump directly to a much larger staircase count.

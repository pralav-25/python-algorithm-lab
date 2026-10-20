# Generate reduced fractions in increasing order

[Guide index](../README.md) · [Implementation](../../algorithm_lab/farey_sequence.py)

## What the order limits

The Farey sequence of order `N` contains every reduced fraction in `[0, 1]`
whose denominator is at most `N`, in increasing order. The order bounds
denominators, not the number of items. The sequence starts at `0/1` and ends at
`1/1` for every positive order.

For example, order 5 gives:

```text
0/1, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 1/1
```

## Find the next term

Keep two consecutive terms `a/b < c/d`. Farey neighbors satisfy `bc - ad = 1`.
The next term is

```text
k = floor((N + b) / d)
next = (k*c - a) / (k*d - b)
```

The denominator `k*d - b` is the largest one produced by this recurrence that does not exceed `N`. The determinant stays one:

```text
d*(k*c - a) - c*(k*d - b) = bc - ad = 1
```

Because `k` is maximal, `d + (k*d - b) > N`. For two fractions whose
determinant is one, any reduced fraction strictly between them needs a
denominator at least as large as the sum of their denominators. No intermediate
fraction can therefore fit under the order bound. Advance the pair to `c/d` and
`next`, then repeat.

For order 5, start with `0/1` and `1/5`. Here `k = floor((5 + 1) / 5) = 1`,
so the next term is `1/4`. Using `1/5` and `1/4` as the new pair gives
`k = floor((5 + 5) / 4) = 2`, which produces `1/3`.

## Use the implementation

`farey_sequence` returns a new list of exact `Fraction` objects. Converting each
item to a numerator and denominator makes the ordering easy to inspect:

```python
from algorithm_lab.farey_sequence import farey_sequence

terms = farey_sequence(5)
pairs = [(term.numerator, term.denominator) for term in terms]
print(pairs)
```

```text
[(0, 1), (1, 5), (1, 4), (1, 3), (2, 5), (1, 2), (3, 5), (2, 3), (3, 4), (4, 5), (1, 1)]
```

Order 1 is the smallest valid input and returns just `0/1` and `1/1`. The full
list has quadratic size as `N` grows, so the implementation is useful when the
sequence itself is needed; it is not a constant-memory iterator.

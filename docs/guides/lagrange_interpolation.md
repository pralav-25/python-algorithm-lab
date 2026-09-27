# Evaluate the unique low-degree curve through exact points

[Guide index](../README.md) · [Implementation](../../algorithm_lab/lagrange_interpolation.py)

## Reasoning

Each Lagrange basis polynomial equals one at its own sample x-coordinate and zero at every other sample coordinate. Weighting these basis polynomials by the sample y-values therefore reproduces all supplied points. Exact rational arithmetic avoids rounding the basis products.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.lagrange_interpolation import lagrange_interpolation
>>> points = [(0, 2), (1, 3), (2, 6)]
>>> lagrange_interpolation(points, 3)
Fraction(11, 1)
>>> assert all(lagrange_interpolation(points, x) == y for x, y in points)
>>> assert lagrange_interpolation(list(reversed(points)), 3) == 11

```

## Boundary to remember

Distinct x-coordinates are required. Interpolating a polynomial through observations is an algebraic operation; extrapolated values are not evidence that a physical process follows that polynomial.

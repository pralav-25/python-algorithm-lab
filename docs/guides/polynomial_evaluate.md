# Evaluate coefficients with Horner’s rule

[Guide index](../README.md) · [Implementation](../../algorithm_lab/polynomial_evaluate.py)

## Reasoning

A polynomial can be nested so each step multiplies the accumulated higher-degree part by x and adds the next coefficient. This uses one multiply-add step per coefficient instead of separately forming every power. Reading coefficients in reverse bridges the API’s increasing-degree order and the nested evaluation.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.polynomial_evaluate import polynomial_evaluate
>>> coefficients, x = [2, 0, -3, 1], 4
>>> polynomial_evaluate(coefficients, x)
18
>>> assert polynomial_evaluate(coefficients, x) == sum(
...     c * x**degree for degree, c in enumerate(coefficients)
... )
>>> polynomial_evaluate([], 4), polynomial_evaluate(coefficients, 0)
(0, 2)

```

## Boundary to remember

The first coefficient is the constant term, not the leading coefficient. This routine accepts integer coefficients and integer evaluation points; exact rational polynomials use other APIs in the library.

# Exclude each factor without dividing by it

[Guide index](../README.md) · [Implementation](../../algorithm_lab/product_except_self.py)

## Reasoning

The product excluding a position is the product of everything to its left times everything to its right. One pass writes prefix products; a reverse pass multiplies in suffix products. Avoiding division handles zeros naturally and retains exact integer arithmetic.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.product_except_self import product_except_self
>>> product_except_self([2, 3, 5])
[15, 10, 6]
>>> product_except_self([2, 0, 5])
[0, 10, 0]
>>> product_except_self([0, 3, 0])
[0, 0, 0]
>>> product_except_self([9])
[1]

```

## Boundary to remember

An empty product equals one, so a singleton input produces [1]. Two zeros make every result zero; one zero leaves only the product at that zero’s position potentially nonzero.

## Practice exercise

Compute signed exclusion products and verify each by explicitly
multiplying the remaining factors, then replace a negative factor with zero.

```pycon
>>> from algorithm_lab.product_except_self import product_except_self
>>> from math import prod
>>> factors = [-2, 3, -4, 5]
>>> outputs = product_except_self(iter(factors))
>>> outputs
[-60, 40, -30, 24]
>>> assert outputs == [prod(factors[:index] + factors[index + 1 :]) for index in range(len(factors))]
>>> factors[2] = 0
>>> product_except_self(factors)
[0, 0, -30, 0]

```

Excluding a negative factor can change the sign of the product. After
introducing one zero, only the output excluding that zero survives, and
it retains the negative sign of the remaining factors.

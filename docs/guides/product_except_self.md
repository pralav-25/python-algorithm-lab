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

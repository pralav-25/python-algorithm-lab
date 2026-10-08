# Choose multiplication parentheses before multiplying

[Guide index](../README.md) · [Implementation](../../algorithm_lab/matrix_chain.py)

## Reasoning

Matrix multiplication is associative, but intermediate dimensions change the number of scalar products. For every consecutive subchain, try each final split and combine the optimal costs of its two halves. This optimization operates on dimensions alone; it does not need to construct or multiply the matrices.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.matrix_chain import matrix_chain
>>> cost, order = matrix_chain([5, 10, 3, 12])
>>> cost, order
(330, '((A1 @ A2) @ A3)')
>>> assert cost == 5 * 10 * 3 + 5 * 3 * 12
>>> assert cost < 10 * 3 * 12 + 5 * 10 * 12
>>> matrix_chain([5, 10])
(0, 'A1')

```

## Boundary to remember

The dimensions list has one more entry than the number of matrices. Reordering matrices is not allowed: only parentheses change. The result models dense scalar multiplication, not hardware-specific runtime.

## Practice exercise

Optimize a four-matrix chain with dimensions 8, 2, 7, 3, and 5. Check all five possible parenthesizations by their scalar multiplication counts.

```pycon
>>> from algorithm_lab.matrix_chain import matrix_chain
>>> cost, order = matrix_chain([8, 2, 7, 3, 5])
>>> cost, order
(152, '(A1 @ ((A2 @ A3) @ A4))')
>>> all_costs = [
...     8 * 2 * 7 + 8 * 7 * 3 + 8 * 3 * 5,
...     2 * 7 * 3 + 8 * 2 * 3 + 8 * 3 * 5,
...     8 * 2 * 7 + 7 * 3 * 5 + 8 * 7 * 5,
...     2 * 7 * 3 + 2 * 3 * 5 + 8 * 2 * 5,
...     7 * 3 * 5 + 2 * 7 * 5 + 8 * 2 * 5,
... ]
>>> all_costs
[400, 210, 497, 152, 255]
>>> assert cost == min(all_costs)

```

Multiplying A2 and A3 first produces a 2-by-3 intermediate; combining it with A4 yields a 2-by-5 intermediate before the final product. Enumerating the five Catalan choices confirms the unique cheapest order. Always associating to the left would cost 400 instead.

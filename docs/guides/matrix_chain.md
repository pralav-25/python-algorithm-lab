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

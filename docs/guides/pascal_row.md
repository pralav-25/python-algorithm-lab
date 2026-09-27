# Generate all fixed-size subset counts for one set

[Guide index](../README.md) · [Implementation](../../algorithm_lab/pascal_row.py)

## Reasoning

Neighboring binomial coefficients in a row are related by an exact multiplicative ratio. Starting from one constructs the desired row directly, without storing every earlier row of Pascal’s triangle. The symmetry and row sum provide convenient independent checks.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.pascal_row import pascal_row
>>> pascal_row(5)
[1, 5, 10, 10, 5, 1]
>>> row = pascal_row(12)
>>> assert row == row[::-1] and sum(row) == 2**12
>>> pascal_row(0)
[1]

```

## Boundary to remember

Row numbering begins at zero. Values are exact integers, so large rows grow in both number of entries and integer bit length.

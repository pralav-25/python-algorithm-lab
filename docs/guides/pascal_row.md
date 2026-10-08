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

## Practice exercise

Count three-person committees from eight people that include at least
one of two designated leaders, and check by direct enumeration.

```pycon
>>> from algorithm_lab.pascal_row import pascal_row
>>> from itertools import combinations
>>> all_committees = pascal_row(8)[3]
>>> no_leaders = pascal_row(6)[3]
>>> with_leader = all_committees - no_leaders
>>> with_leader
36
>>> assert with_leader == sum(
...     any(person < 2 for person in committee) for committee in combinations(range(8), 3)
... )

```

Coefficient three counts subsets of size three, not ordered seating
arrangements. Subtracting committees drawn entirely from the other six
people avoids double-counting those that contain both leaders.

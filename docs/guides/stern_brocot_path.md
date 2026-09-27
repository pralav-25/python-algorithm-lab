# Locate a positive fraction by mediant comparisons

[Guide index](../README.md) · [Implementation](../../algorithm_lab/stern_brocot_path.py)

## Reasoning

The Stern–Brocot tree places a mediant between two bounding fractions. Moving left or right narrows the bounds toward a target positive rational. Runs of identical directions can be compressed using Euclidean division, avoiding an enormous list of individual steps for ratios near an extreme.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.stern_brocot_path import stern_brocot_path
>>> stern_brocot_path(3, 2)
[('R', 1), ('L', 1)]
>>> assert stern_brocot_path(6, 4) == stern_brocot_path(3, 2)
>>> stern_brocot_path(1, 1)
[]
>>> stern_brocot_path(1000001, 1)
[('R', 1000000)]

```

## Boundary to remember

Directions begin at 1/1, and equivalent unreduced fractions share a path. The run counts are part of the representation: a count of a million is not a million separately stored moves.

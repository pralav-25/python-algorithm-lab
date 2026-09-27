# Keep only the outermost points of a cloud

[Guide index](../README.md) · [Implementation](../../algorithm_lab/convex_hull.py)

## Reasoning

After sorting points, build lower and upper boundary chains. Whenever the newest point makes a chain turn inward, its previous endpoint cannot be an extreme hull vertex and is removed. Integer cross products decide turn direction exactly, including for large coordinates.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.convex_hull import convex_hull
>>> points = [(0, 0), (3, 0), (3, 2), (0, 2), (1, 1), (0, 0)]
>>> convex_hull(points)
[(0, 0), (3, 0), (3, 2), (0, 2)]
>>> assert convex_hull(list(reversed(points))) == convex_hull(points)
>>> convex_hull([(0, 0), (1, 1), (2, 2)])
[(0, 0), (2, 2)]

```

## Boundary to remember

Interior points along a straight hull edge are omitted. The first vertex is not repeated at the end, and fully collinear input reduces to its two extreme endpoints.

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

## Practice exercise

Translate a point cloud by a fixed integer vector. Check that the hull translates by the same vector and that an interior point stays off the boundary.

```pycon
>>> from algorithm_lab.convex_hull import convex_hull
>>> cloud = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]
>>> translated = [(x - 7, y + 3) for x, y in cloud]
>>> assert convex_hull(translated) == [(x - 7, y + 3) for x, y in convex_hull(cloud)]
>>> assert (-5, 5) not in convex_hull(translated)

```

Translation preserves orientation and lexicographic comparisons because every coordinate receives the same offset. It therefore changes neither which points are extreme nor the returned boundary order.

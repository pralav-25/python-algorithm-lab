# Classify points with a boundary-aware crossing test

[Guide index](../README.md) · [Implementation](../../algorithm_lab/point_in_polygon.py)

## Reasoning

A ray leaving a point crosses a simple polygon boundary an odd number of times from the inside and an even number from the outside. Careful endpoint rules prevent counting a vertex twice. Testing whether the point lies on an edge first makes boundary inclusion an explicit choice.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.point_in_polygon import point_in_polygon
>>> polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]
>>> point_in_polygon((2, 1), polygon), point_in_polygon((5, 1), polygon)
(True, False)
>>> point_in_polygon((4, 1), polygon)
True
>>> point_in_polygon((4, 1), polygon, include_boundary=False)
False
>>> assert point_in_polygon((2, 1), polygon[::-1])

```

## Boundary to remember

The polygon must be simple and supplied in boundary order. Boundary points are included by default; applications that require strict interior membership must request otherwise.

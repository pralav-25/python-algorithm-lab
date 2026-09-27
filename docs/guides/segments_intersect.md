# Distinguish crossings, contact, and collinear overlap

[Guide index](../README.md) · [Implementation](../../algorithm_lab/segments_intersect.py)

## Reasoning

Orientation signs tell which side of one segment’s line contains the endpoints of the other. Opposite signs on both segments identify a proper crossing. Zero orientation requires an additional bounding-box check to recognize endpoint contact and collinear overlap without accepting distant collinear points.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.segments_intersect import segments_intersect
>>> segments_intersect((0, 0), (4, 0), (2, 0), (6, 0))
True
>>> segments_intersect((0, 0), (1, 0), (2, 0), (3, 0))
False
>>> segments_intersect((1, 1), (1, 1), (0, 0), (2, 2))
True
>>> segments_intersect((0, 0), (2, 2), (0, 2), (2, 0))
True

```

## Boundary to remember

Segments are closed, so touching at an endpoint counts. Zero-length segments are also allowed; they intersect when their single point lies on the other segment.

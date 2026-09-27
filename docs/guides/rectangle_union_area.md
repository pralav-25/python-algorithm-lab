# Count overlapping rectangular coverage only once

[Guide index](../README.md) · [Implementation](../../algorithm_lab/rectangle_union_area.py)

## Reasoning

All rectangle side coordinates divide the plane into vertical slabs. Inside one slab, the active rectangles have a constant union of y-intervals, so covered height times slab width gives its area. Summing slab areas handles overlaps and duplicates without counting any covered region twice.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.rectangle_union_area import rectangle_union_area
>>> rectangles = [(0, 0, 3, 2), (2, 1, 5, 3)]
>>> rectangle_union_area(rectangles)
11
>>> assert rectangle_union_area(rectangles) == 6 + 6 - 1
>>> assert rectangle_union_area(rectangles + rectangles) == 11
>>> rectangle_union_area([])
0

```

## Boundary to remember

Only axis-aligned rectangles with positive width and height are accepted. This straightforward slab algorithm favors readability over the asymptotic efficiency of a segment-tree sweep for very large collections.

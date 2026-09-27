# Sum signed edge contributions to an exact area

[Guide index](../README.md) · [Implementation](../../algorithm_lab/polygon_area.py)

## Reasoning

Each directed polygon edge contributes a cross product to the shoelace sum. Contributions inside the boundary combine into twice the signed area, and taking the absolute value removes the orientation sign. Returning a Fraction preserves half-unit areas exactly for integer-coordinate polygons.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.polygon_area import polygon_area
>>> triangle = [(0, 0), (5, 0), (0, 3)]
>>> polygon_area(triangle)
Fraction(15, 2)
>>> assert polygon_area(triangle[::-1]) == polygon_area(triangle)
>>> assert polygon_area(triangle + [triangle[0]]) == polygon_area(triangle)
>>> polygon_area([(0, 0), (1, 1)])
Fraction(0, 1)

```

## Boundary to remember

Vertices must follow the boundary of a simple polygon. Sorting arbitrary points lexicographically does not make a valid boundary, and self-intersections are not validated by this routine.

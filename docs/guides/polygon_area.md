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

## Practice exercise

Compute the area of a concave region as two nonoverlapping rectangles,
then translate every vertex far from the origin and check invariance.

```pycon
>>> from algorithm_lab.polygon_area import polygon_area
>>> outline = [(0, 0), (5, 0), (5, 2), (2, 2), (2, 4), (0, 4)]
>>> area = polygon_area(outline)
>>> area
Fraction(14, 1)
>>> assert area == 5 * 2 + 2 * 2
>>> translated = [(x + 10**20, y - 10**20) for x, y in outline]
>>> assert polygon_area(translated) == area

```

The bounding rectangle has area twenty, but the missing upper-right
corner removes six units. Translation changes individual cross products,
yet their extra terms cancel; exact integers avoid cancellation rounding.

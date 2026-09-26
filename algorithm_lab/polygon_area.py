"""Exact unsigned area of a simple polygon by the shoelace formula.

Vertices are boundary-ordered integer pairs excluding bool. Either orientation
and an optional repeated closing vertex are accepted. Fewer than three points
or a degenerate polygon returns Fraction(0). Simplicity is assumed, not checked.
O(n) arithmetic operations and O(n) space; the input is not mutated.

>>> polygon_area([(0, 0), (3, 0), (0, 1)])
Fraction(3, 2)
"""

from fractions import Fraction

from algorithm_lab._geometry import point


def polygon_area(vertices):
    vertices = list(map(point, vertices))
    if len(vertices) < 3:
        return Fraction(0)
    twice = sum(
        a[0] * b[1] - a[1] * b[0]
        for a, b in zip(vertices, vertices[1:] + vertices[:1], strict=True)
    )
    return Fraction(abs(twice), 2)

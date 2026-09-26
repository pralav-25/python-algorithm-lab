"""Exact ray-crossing membership in a simple integer polygon.

Vertices must contain at least three boundary-ordered integer pairs (bool excluded).
The polygon is assumed simple. Either orientation is accepted. Boundary points
are included by default; include_boundary must be bool. O(n) time and space.

>>> point_in_polygon((1, 1), [(0, 0), (2, 0), (2, 2), (0, 2)])
True
"""

from algorithm_lab._geometry import cross, on_segment, point


def point_in_polygon(query, vertices, *, include_boundary=True):
    p, vertices = point(query), list(map(point, vertices))
    if len(vertices) < 3:
        raise ValueError("polygon requires at least three vertices")
    if not isinstance(include_boundary, bool):
        raise ValueError("include_boundary must be bool")
    inside = False
    for a, b in zip(vertices, vertices[1:] + vertices[:1], strict=True):
        if on_segment(a, b, p):
            return include_boundary
        if (a[1] > p[1]) != (b[1] > p[1]) and (cross(a, b, p) > 0) == (b[1] > a[1]):
            inside = not inside
    return inside

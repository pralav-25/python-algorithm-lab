"""Exact intersection predicate for two closed integer line segments.

Endpoint contact, collinear overlap and zero-length segments count as intersections.
Coordinates are integers excluding bool. Constant arithmetic operations and space.

>>> segments_intersect((0, 0), (2, 2), (0, 2), (2, 0))
True
"""

from algorithm_lab._geometry import cross, on_segment, point


def segments_intersect(a, b, c, d):
    a, b, c, d = map(point, (a, b, c, d))
    if any((on_segment(a, b, c), on_segment(a, b, d), on_segment(c, d, a), on_segment(c, d, b))):
        return True
    return cross(a, b, c) * cross(a, b, d) < 0 and cross(c, d, a) * cross(c, d, b) < 0

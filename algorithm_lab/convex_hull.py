"""Monotone-chain convex hull of integer coordinate pairs.

Return distinct extreme vertices counterclockwise, starting at the lexicographic
minimum, without repeating the first vertex. Collinear interior points disappear;
an entirely collinear input returns its endpoints. Empty input returns [].
Integer coordinates exclude bool. O(n log n) time and O(n) space.

>>> convex_hull([(1, 1), (0, 0), (2, 0), (2, 2), (0, 2)])
[(0, 0), (2, 0), (2, 2), (0, 2)]
"""

from algorithm_lab._geometry import cross, point


def convex_hull(points):
    points = sorted(set(map(point, points)))
    if len(points) <= 1:
        return points

    def half(rows):
        result = []
        for p in rows:
            while len(result) >= 2 and cross(result[-2], result[-1], p) <= 0:
                result.pop()
            result.append(p)
        return result

    return half(points)[:-1] + half(reversed(points))[:-1]

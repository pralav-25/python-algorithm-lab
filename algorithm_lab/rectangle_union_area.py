"""Exact area covered by axis-aligned integer rectangles using vertical slabs.

Each rectangle is (left, bottom, right, top) with left < right and bottom < top.
Coordinates exclude bool. Overlaps and duplicates count once; empty input returns
zero. O(n squared log n) time and O(n) working space. Inputs are not mutated.

>>> rectangle_union_area([(0, 0, 2, 2), (1, 1, 3, 3)])
7
"""

from algorithm_lab._validation import integer


def rectangle_union_area(rectangles):
    rows = []
    for left, bottom, right, top in rectangles:
        for value in (left, bottom, right, top):
            integer(value, "coordinate")
        if left >= right or bottom >= top:
            raise ValueError("rectangles must have positive width and height")
        rows.append((left, bottom, right, top))
    xs = sorted({x for left, _, right, _ in rows for x in (left, right)})
    area = 0
    for left, right in zip(xs, xs[1:], strict=False):
        intervals = sorted((b, t) for start, b, end, t in rows if start <= left and right <= end)
        end, height = None, 0
        for bottom, top in intervals:
            height += max(0, top - max(bottom, end)) if end is not None else top - bottom
            end = top if end is None else max(end, top)
        area += (right - left) * height
    return area

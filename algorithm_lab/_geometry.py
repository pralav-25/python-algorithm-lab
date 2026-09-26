"""Exact integer geometry helpers; booleans are not coordinates."""

from algorithm_lab._validation import integer


def point(value):
    x, y = value
    return integer(x, "x"), integer(y, "y")


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a, b, p):
    return (
        cross(a, b, p) == 0
        and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )

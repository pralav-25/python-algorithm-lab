"""Shared strict integer validation for bounded indices and discrete inputs."""


def integer(value, name="value", *, minimum=None):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return value


def index(value, size, *, allow_end=False):
    integer(value, "index", minimum=0)
    if value > size or (value == size and not allow_end):
        raise ValueError("index is out of range")
    return value

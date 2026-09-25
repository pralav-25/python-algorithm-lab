"""Finite floating-point validation and scale-safe probability normalization."""

import math


def finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("values must be finite integers or floats")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError("value exceeds the floating-point range") from exc
    if not math.isfinite(result):
        raise ValueError("values must be finite")
    return result


def probabilities(weights):
    values = [finite(value) for value in weights]
    if not values or any(value < 0 for value in values) or max(values) == 0:
        raise ValueError("weights must be nonnegative with positive total mass")
    scale = max(values)
    scaled = [value / scale for value in values]
    total = math.fsum(scaled)
    return [value / total for value in scaled]

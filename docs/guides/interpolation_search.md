# Find the first target occurrence by interpolating integer endpoints.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/interpolation_search.py)

## Reasoning

Estimate the target's position by its proportion within the endpoint values, then narrow the interval around that probe. When values are spread roughly uniformly, the estimate can be more direct than halving the index range.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.interpolation_search import interpolation_search

print(repr(interpolation_search([1, 3, 3, 5, 9], 3)))  # 1
```

## Boundary to remember

Inputs must be ascending integers and duplicates resolve to the first index. Skewed values can make probes advance slowly, so the worst case is linear rather than logarithmic.

## Practice exercise

Search a uniformly spaced integer measurement series and compare the estimated probe with the midpoint strategy.

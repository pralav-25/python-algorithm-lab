# State the interpolation convention behind a quantile

[Guide index](../README.md) · [Implementation](../../algorithm_lab/percentile.py)

## Reasoning

Sort the observations and locate q times (n-1) along their index range. If that location lies between two observations, interpolate linearly. This makes endpoints agree with the minimum and maximum and specifies the otherwise ambiguous meaning of a sample percentile.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.percentile import percentile
>>> observations = [40, 10, 30, 20]
>>> percentile(observations, 0.25)
17.5
>>> percentile(observations, 0.5)
25.0
>>> percentile(observations, 0), percentile(observations, 1)
(10.0, 40.0)
>>> assert observations == [40, 10, 30, 20]

```

## Boundary to remember

q is a fraction between zero and one, not a percentage between zero and one hundred. Different quantile conventions can legitimately return different answers on small samples.

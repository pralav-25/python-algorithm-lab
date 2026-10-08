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

## Practice exercise

Compute quantiles on a sample with duplicate zeroes, distinguishing an
interpolated position from a nearest-observation convention.

```pycon
>>> from algorithm_lab.percentile import percentile
>>> sample = [25, 0, -5, 10, 0]
>>> percentile(sample, 0.625), percentile(sample, 0.375)
(5.0, 0.0)
>>> ordered = sorted(sample)
>>> position = 0.625 * (len(sample) - 1)
>>> assert position == 2.5
>>> assert percentile(sample, 0.625) == (ordered[2] + ordered[3]) / 2
>>> assert percentile([9], 0.625) == 9.0

```

Position two and a half lies between zero and ten, so the answer is five
even though five was never observed. Duplicate endpoints can make an
interpolated segment constant; a singleton has only one possible value.

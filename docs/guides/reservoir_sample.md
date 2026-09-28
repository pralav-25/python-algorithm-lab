# Choose uniformly from a stream of unknown length

[Guide index](../README.md) · [Implementation](../../algorithm_lab/reservoir_sample.py)

## Reasoning

Fill k slots with the first k observations. For the item at zero-based
position i, draw a uniform slot in 0 through i: replace that slot only when it
lies inside the reservoir. The new item has inclusion probability k/(i + 1),
and each earlier item has that same probability after possible replacement.
The pass uses O(n) time and O(k) storage.

## Worked example

Run these statements from the repository root.

```pycon
>>> import random
>>> from algorithm_lab.reservoir_sample import reservoir_sample
>>> first = reservoir_sample(range(100), 5, rng=random.Random(17))
>>> second = reservoir_sample(range(100), 5, rng=random.Random(17))
>>> first == second and len(set(first)) == 5
True
>>> reservoir_sample(["a", "a", "b"], 9, rng=random.Random(2))
['a', 'a', 'b']
>>> stream = iter([10, 20])
>>> reservoir_sample(stream, 0), next(stream)
([], 10)

```

## Boundary to remember

Sampling is over positions, so equal values can legitimately occur more
than once. If fewer than k items arrive, all are returned in original order;
otherwise output order is unspecified. A zero-size sample consumes no input.
Inject a seeded random.Random for repeatable experiments.

# Find a minimum-coin payment when greed fails

[Guide index](../README.md) · [Implementation](../../algorithm_lab/coin_change.py)

## Reasoning

For each amount, try taking each denomination as the last coin and reuse the best result for the remaining amount. This considers combinations that a largest-coin-first strategy can miss. Predecessor choices reconstruct an actual payment once the minimum count is known.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.coin_change import coin_change
>>> payment = coin_change([1, 4, 5], 8)
>>> payment
[4, 4]
>>> assert sum(payment) == 8 and len(payment) == 2
>>> coin_change([4, 6], 3) is None
True
>>> coin_change([4, 6], 0)
[]

```

## Boundary to remember

Coins are available in unlimited quantities. A bounded wallet needs a different state model. Zero amount returns an empty payment, while an unreachable amount returns None.

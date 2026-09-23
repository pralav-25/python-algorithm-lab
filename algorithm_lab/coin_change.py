"""Return a minimum-length sorted list of coins, or None if amount is unreachable.

Coin values must be positive integers and amount a nonnegative integer. Unlimited
copies are allowed; duplicate denominations are ignored. Equal-length choices
keep the first ascending denomination considered. Time O(amount * k), space O(amount).

>>> coin_change([1, 3, 4], 6)
[3, 3]
>>> coin_change([4], 3) is None
True
"""


def coin_change(coins, amount: int) -> list[int] | None:
    if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
        raise ValueError("amount must be a nonnegative integer")
    values = list(coins)
    if any(isinstance(c, bool) or not isinstance(c, int) or c <= 0 for c in values):
        raise ValueError("coin values must be positive integers")
    values = sorted(set(values))
    counts, choices = [0] + [amount + 1] * amount, [0] * (amount + 1)
    for current in range(1, amount + 1):
        for coin in values:
            if coin > current:
                break
            if counts[current - coin] + 1 < counts[current]:
                counts[current] = counts[current - coin] + 1
                choices[current] = coin
    if counts[amount] > amount:
        return None
    result = []
    while amount:
        coin = choices[amount]
        result.append(coin)
        amount -= coin
    return sorted(result)

"""Count unordered ways to make change with unlimited coins.

Coins are positive integers; repeated denominations are deduplicated. The
target is a nonnegative integer. Bool is rejected. The empty combination
counts once for target=0. O(target*number_of_distinct_coins) time and O(target)
space, plus sorted coin storage. Return an exact count, not a reconstruction.

>>> coin_change_count([1, 2, 5], 5)
4
"""

from algorithm_lab._validation import integer


def coin_change_count(coins, target):
    integer(target, "target", minimum=0)
    coins = list(coins)
    for coin in coins:
        integer(coin, "coin", minimum=1)
    ways = [1] + [0] * target
    for coin in sorted(set(coins)):
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    return ways[target]

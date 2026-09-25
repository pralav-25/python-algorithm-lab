"""Maximum integer value with bounded item quantities.

Items are (positive weight, integer value, nonnegative count); capacity is a
nonnegative integer, excluding bool throughout. Return the maximum value;
taking nothing is allowed. Binary grouping uses O(capacity*sum(log(count+1)))
time and O(capacity) space. Counts exceeding capacity are safely capped.

>>> bounded_knapsack([(2, 3, 2), (3, 5, 1)], 5)
8
"""

from algorithm_lab._validation import integer


def bounded_knapsack(items, capacity):
    integer(capacity, "capacity", minimum=0)
    dp = [0] * (capacity + 1)
    for weight, value, count in items:
        integer(weight, "weight", minimum=1)
        integer(value, "value")
        integer(count, "count", minimum=0)
        count = min(count, capacity // weight)
        group = 1
        while count:
            take = min(group, count)
            cost, reward = take * weight, take * value
            for remaining in range(capacity, cost - 1, -1):
                dp[remaining] = max(dp[remaining], dp[remaining - cost] + reward)
            count -= take
            group *= 2
    return dp[capacity]

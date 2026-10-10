"""Return row n of the ballot-number Catalan triangle.

n is a nonnegative integer excluding bool. Entry k, for 0<=k<=n, counts paths
with n up-steps and k down-steps whose partial height never becomes negative.
The result is a new list ordered by k, so no tie choice is needed. Row 0 is [1].
Rolling sums use O(n**2) arithmetic steps and O(n) integer storage.

>>> catalan_triangle(3)
[1, 3, 5, 5]
"""

from algorithm_lab._validation import integer


def catalan_triangle(n):
    integer(n, "n", minimum=0)
    row = [1]
    for size in range(1, n + 1):
        following = [1]
        for k in range(1, size):
            following.append(following[-1] + row[k])
        following.append(following[-1])
        row = following
    return row

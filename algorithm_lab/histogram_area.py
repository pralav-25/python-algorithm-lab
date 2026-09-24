"""Maximum rectangle area in unit-width bars with nonnegative integer heights.

O(n) time and space; empty input has area zero. Equal-height bars can be joined.
Input is copied; negative/non-integer heights raise ValueError.

>>> histogram_area([2, 1, 5, 6, 2, 3])
10
"""

from algorithm_lab._validation import integer


def histogram_area(heights):
    data = [integer(h, "height", minimum=0) for h in heights]
    stack, best = [], 0
    for right, height in enumerate(data + [0]):
        left = right
        while stack and stack[-1][1] > height:
            left, previous = stack.pop()
            best = max(best, previous * (right - left))
        if not stack or stack[-1][1] < height:
            stack.append((left, height))
    return best

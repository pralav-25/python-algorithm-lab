"""Return a longest common substring, preferring the earliest start in first.

Comparison is exact over Unicode code points. Time O(len(first) * len(second)),
working space O(len(second)); empty inputs or no common character return ''.

>>> longest_common_substring('xabcdz', 'yabcq')
'abc'
"""


def longest_common_substring(first: str, second: str) -> str:
    previous, best, stop = [0] * (len(second) + 1), 0, 0
    for i, left in enumerate(first, 1):
        current = [0] * (len(second) + 1)
        for j, right in enumerate(second, 1):
            if left == right:
                current[j] = previous[j - 1] + 1
                if current[j] > best:
                    best, stop = current[j], i
        previous = current
    return first[stop - best : stop]

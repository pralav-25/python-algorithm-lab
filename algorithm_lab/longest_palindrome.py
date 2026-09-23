"""Return the longest palindromic substring; ties choose the earliest start.

Empty input returns ''. Characters are Unicode code points. Time O(n²), auxiliary
space O(1), excluding the returned slice. Both odd and even centers are examined.

>>> longest_palindrome('babad')
'bab'
>>> longest_palindrome('cbbd')
'bb'
"""


def longest_palindrome(text: str) -> str:
    start = stop = 0
    for center in range(len(text)):
        for left, right in ((center, center), (center, center + 1)):
            while left >= 0 and right < len(text) and text[left] == text[right]:
                left -= 1
                right += 1
            if right - left - 1 > stop - start:
                start, stop = left + 1, right
    return text[start:stop]

"""
2351. First Letter to Appear Twice (https://leetcode.com/problems/first-letter-to-appear-twice/)

Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:
A letter 'a' appears twice before another letter 'b' if the second occurrence of 'a' is before the second occurrence of 'b'.
s will contain at least one letter that appears twice.


Example 1:
Input: s = "abccbaacz"
Output: "c"

Example 2:
Input: s = "abcdd"
Output: "d"


Constraints:
2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.
"""

def firstLetterTwice(s: str) -> str:

    n = len(s)
    seen = [''] * n

    for i in range(n):
        if s[i] in seen:
            return s[i]
        
        else:
            seen[i] = s[i]

    return
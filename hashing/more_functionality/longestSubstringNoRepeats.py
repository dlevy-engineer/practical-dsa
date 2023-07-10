"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "bbbbb"
Output: 1

Example 3:
Input: s = "pwwkew"
Output: 3

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s: str) -> int:

    output = 0
    n = len(s)
    recent_indices = {}

    for i in range(n):
        if s[i] in recent_indices:
            output = max(output, i - recent_indices[s[i]] + 1)

        recent_indices[s[i]] = i

    return output
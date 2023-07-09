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

    # instantiate a set for O(1) retrieval
    seen = set()

    # loop over characters in the input string
    for c in s:

        # if found in set, return the current character
        if c in seen:
            return s
        
        # if not, this is a first encounter so add to the set and move on
        else:
            seen.add(c)

    return
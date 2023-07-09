"""
1941 – Check if All Characters Have Equal Number of Occurrences (https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/)

Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).


Example 1:
Input: s = "abacbc"
Output: true

Example 2:
Input: s = "aaabb"
Output: false


Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

from collections import defaultdict

def areOccurrencesEqual() -> bool:

    # instantiate a hash map
    d = defaultdict(int)

    # loop through characters in the input string and increment hash map values corresponding to each key
    for c in s:
        d[c] += 1

    # convert hash map values to a set
    counts = set(d.values())

    # there should only be one value in the set for a 'good' string
    return len(counts) == 1


from collections import Counter

def areOccurrencesEqual():
    return len(set(Counter(s).values())) == 1
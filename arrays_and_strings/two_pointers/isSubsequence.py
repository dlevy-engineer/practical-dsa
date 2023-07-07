"""
Example 4: 392 – Is Subsequence (https://leetcode.com/problems/is-subsequence/)

Given two strings s and t, return True if s is a subsequence of t, or False otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, 
while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.
"""

def isSubsequence(s: str,
                  t: str) -> bool:
    
    # instantiate pointers on the left of each respective string
    i = j = 0

    # construct a while lopop that will only run until we reach the end of one of our input iterables
    while i < len(s) and j < len(t):

        # case 1: we have found a match for the current position in the subsequence, and we need to move along in both the subsequence and the original string
        # case 2: there is no match for the current position in the subsequence, and we need to move along in the original string only

        # for the current pointer positions, increment the subsequence in case 1
        if s[i] == t[j]:
            i += 1

        # increment the original string pointer regardless of case 1 or case 2
        j += 1

    # if we still haven't made it through the subsequence when we exit the while loop, `s` is not a subsequence of `t`
    if i < len(s):
        return False
    
    # if we did make it through the subsequence, it's because `s` must be a subsequence of `t`
    else:
        return True
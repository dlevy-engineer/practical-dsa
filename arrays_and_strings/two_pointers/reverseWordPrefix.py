"""
2000 – Reverse Prefix of Word (https://leetcode.com/problems/reverse-prefix-of-word/)

Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). 
If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.


Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"


Constraints:
1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter.
"""
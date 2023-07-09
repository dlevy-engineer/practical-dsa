"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true

Example 2:
Input: sentence = "leetcode"
Output: false


Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""

def checkPangram(sentence: str) -> bool:

    # convert the input string to a set for O(1) retrieval
    letters = set(sentence)

    # check to see if every letter of the alphabet is present
    return len(letters) == 26
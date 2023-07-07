"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
 

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""

def reverseString(s: list[str]) -> None:

    # instantiate two pointers on either end of the string
    i = 0
    j = len(s) - 1

    # instantiate a temporary variable to assist with a swap
    temp = ''

    # construct a while loop that will only run until the pointers meet or cross
    while i < j:

        # hold the left element in a temporary variable
        temp = s[i]

        # set the left element equal to the right element
        s[i] = s[j]

        # set the right element equal to the former left element via the temporary variable
        s[j] = temp

        # increment the left pointer and decrement the right pointer
        i += 1
        j -= 1

    return
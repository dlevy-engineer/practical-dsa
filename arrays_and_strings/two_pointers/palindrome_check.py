# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# A string is a palindrome if it reads the same forward as backward.
# That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

def palindrome_check(s: str) -> bool:

    # instantiate a left and right pointer
    left = 0
    right = len(s) - 1

    # construct a while loop that will only run until the pointers meet or cross
    while left < right:

        # return False if we find non-matching characters
        if s[left] != s[right]:
            return False
        
        # otherwise, move the counters toward one another for the next check
        left += 1
        right -= 1

    # if we make it through the while loop, we have a palindrome
    return True
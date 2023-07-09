"""
You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3.
The longest substring with at most 2 distinct characters is "ece".
"""

from collections import defaultdict

def longestSubstringKDistinct(s: str,
                              k: int) -> int:
    
    # instantiate a left pointer and an output variable to keep track of string length
    left = output = 0
    d = defaultdict(int)

    # contruct a for loop that will slide a right pointer along the length of the input array
    for right in range(len(s)):

        # increment the hash map value referenced by the current character on the right side of the string (as the key)
        d[s[right]] += 1

        # construct a while loop that will run when our constraint is violated by
        # sliding the left pointer until our constraint is no longer violated
        while len(d) > k:

            # decrement the hash map value referenced by the current character on the left side of the string
            d[s[left]] -= 1

            # if we have a key mapping to a 0 value, remove the key-value pair from the hash map
            if d[s[left]] == 0:
                del d[s[left]]

            # move the left pointer
            left += 1

        # set the output value to the maximum between the current output value and the size of the current window
        output = max(output, right - left + 1)
    
    return output
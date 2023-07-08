"""
Example 2:
You are given a binary string s (a string containing only "0" and "1").
You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes "1111100111".
"""

def binaryFlipOnes(s: str) -> int:

    # instantiate a left pointer,  zero counter to keep track of the number of zeroes in our current window, and an output variable
    left = z = output = 0

    # construct a for loop that will slide the right pointer along the string from left to right
    for right in range(len(s)):

        # when we encounter a '0' on the right side of the string, increment the zero counter
        if s[right] == '0':
            z += 1

        # as long as we have more than one '0' in our window, slide the left counter and decrement the zero counter if we're leaving behind a '0'
        while z > 1:
            if s[left] == '0':
                z -= 1
            
            left += 1

        # update our output value to be the maximum between our previous window and our new window with 1 or fewer '0' characters
        output = max(output, right - left + 1)

    return output
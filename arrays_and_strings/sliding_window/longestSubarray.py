"""
Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.
This is the problem we have been talking about above. We will now formally solve it.
"""

def longestSubarray(nums: list[int],
                    k: int) -> int:

    # instantiate a left pointer, a variable representing the sum of the current window, and an output variable all with an initial value of 0
    left = curr = output = 0

    # instantiate a right pointer that will continually slide along the array from the left
    for right in range(len(nums)):

        # add the new right edge of the window to the current sum
        curr += nums[right]

        # construct a while loop that will increment the left pointer until the sum of the current window is equal to or less than the target
        while curr > k:
            curr -= nums[left]
            left += 1

        # compare our current answer to the length of the updated window, which is now sure to meet the sum constraint
        output = max(output, right - left + 1)

    return output
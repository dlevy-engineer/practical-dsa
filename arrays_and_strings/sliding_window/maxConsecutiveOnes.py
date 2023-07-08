"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10


Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

def maxConsecutiveOnes(nums: list[int],
                       k: int) -> int:
    
    # instantiate a left pointer, a variable to track the number of zeroes in our window, and an output variable
    left = z = output = 0

    # construct a for loop that will slide the right pointer along the input array
    for right in range(len(nums)):

        # if we encounter a zero on the right, increment the zero counter
        if nums[right] == 0:
            z += 1

        # in the case that we've exceeded our flip allotment, increment the left counter until we find a new valid array
        while z > k:
            if nums[left] == 0:
                z -= 1

            left += 1

        # set the output variable to the maximum between the current output variable and the size of the current valid window
        output = max(output, right - left + 1)

    return output
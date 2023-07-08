"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.


Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Example 2:
Input: nums = [5], k = 1
Output: 5.00000


Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

def maxAvgValSubarray(nums: list[int],
                      k: int) -> float:
    
    # instantiate a sum variable to contain the cumulative sum of the current window
    cur_sum = 0

    # construct the leftmost window
    for i in range(k):
        cur_sum += nums[i]

    # instantiate an output variable to contain the maximum sum at any point in the run
    output = cur_sum

    # slide the window, removing the leftmost number and adding the rightmost number
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        output = max(output, cur_sum)

    # return the average value of the window with the largest sum
    return round(output / k, 5)
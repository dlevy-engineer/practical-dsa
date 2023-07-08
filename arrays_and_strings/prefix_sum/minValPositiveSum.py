"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.


Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5

Example 2:
Input: nums = [1,2]
Output: 1

Example 3:
Input: nums = [1,-2,-3]
Output: 5
 

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

def minValPositiveSum(nums: list[int]) -> int:

    # instantiate a variable to hold the length of the input array
    n = len(nums)

    # instantiate a minimum positive value variable to hold the minimum positive value for a starting value at all times
    minimum = 1

    # instantiate a variable to hold the cumulative sum of the input array as we iterate through it
    cum_sum = 0

    # construct a for loop that will iterate through the input array
    for i in range(n):
        cum_sum += nums[i]

        # if we end up with a negative cumulative sum, we should check to see if we need to update the starting value 
        if cum_sum < 0:
            minimum = max(minimum, 1 - cum_sum)

    return minimum
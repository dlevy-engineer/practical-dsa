"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
 

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""

def missingNumber(nums: list[int]) -> int:

    # instantiate a variable to hold the length of the input array plus one (because there is a missing number)
    n = len(nums) + 1

    # convert the input array to a hash set to ensure O(1) time complexity for retrieval
    nums = set(nums)

    # loop over the entire range and look for the value in each iteration
    for i in range(n):

        # return the missing number
        if i not in nums:
            return i
        
    return
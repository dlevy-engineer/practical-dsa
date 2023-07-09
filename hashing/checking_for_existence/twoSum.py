"""
1 – Two Sum (https://leetcode.com/problems/two-sum/)

Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target.
You cannot use the same index twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def twoSum(nums: list[int],
           target: int) -> list[int]:
    
    # instantiate a hash map structure
    d = {}

    # construct a for loop that will traverse the entire input array
    for i in range(len(nums)):

        # retrieve the current element and calculate its theoretical complement
        n = nums[i]
        complement = target - n

        # check to see if the complenent already exists in our hash map, if so return the answer
        if complement in d:
            return [d[complement], i]
        
        # otherwise, add the current value and its index as a key-value pair to the hash map
        else:
            d[n] = i
    
    return
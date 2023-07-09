"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.


Example 1:
Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8

Example 2:
Input: nums = [9,9,8,8]
Output: -1


Constraints:
1 <= nums.length <= 2000
0 <= nums[i] <= 1000
"""

def largestUniqueNumber(nums: list[int]) -> int:

    output = -1
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        
    for k in freq:
        if freq[k] == 1:
            output = max(output, k)
            
    return output
"""
Example 4:
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
"""

def largestSubarraySum(nums: list[int],
                       k: int) -> int:
    
    cur_sum = 0
    
    for i in range(k):
        cur_sum += nums[i]

    output = cur_sum

    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        output = max(output, cur_sum)
    
    return output
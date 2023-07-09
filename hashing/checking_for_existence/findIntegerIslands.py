"""
Given an integer array nums, find all the numbers x that satisfy the following:
x + 1 is not in nums, and x - 1 is not in nums.
"""

def findIntegerIslands(nums: list[int]) -> list[int]:
    
    # convert input array to a set for O(1) retrieval
    nums = set(nums)

    # instantiate an output list
    output = []

    # loop through the set and check for existence of neighboring numbers
    for n in nums:
        if (n + 1) not in nums and (n - 1) not in nums:
            output.append(n)

    return output
"""
Example 2:
2270 – Number of Ways to Split Array (https://leetcode.com/problems/number-of-ways-to-split-array/)

Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than
or equal to the sum of the second section. The second section should have at least one number.
"""

def numWaysToSplit(nums: list[int]) -> int:

    # instantiate a variable to hold the length of the array
    n = len(nums)

    # instantiate a prefix array populated with the first value of the numbers array
    prefix = [nums[0]] * n

    # construct a for loop that will run for the length of the array (minus 1) to fill in the prefix sum values
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]

    # instantiate an output variable to hold the number of valid array splits
    output = 0

    # construct a for loop that will run for the length of the prefix array (minus 1) and increment the output if the array split is valid
    for i in range(n - 1):
        if prefix[i] < prefix[-1] - prefix[i]:
            output += 1

    return output


def numWaysToSplitPrefixless(nums: list[int]) -> int:

    # instantiate an output variable and a variable to hold the sum of the left side of the array
    left_sect = output = 0

    # instnatiate a total sum variable to make it esy to calculate the sum of the right side of the array using the sum of the left side
    total = sum(nums)

    # construct a for loop that will run through the numbers array
    for i in range(len(nums) - 1):

        # add to the cumulative left side sum
        left_sect += nums[i]

        # calculate the right side sum
        right_sect = total - left_sect

        # increment the output variable
        if left_sect >= right_sect:
            output += 1

    return output
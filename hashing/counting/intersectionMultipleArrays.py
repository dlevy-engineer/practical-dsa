"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
return the list of integers that are present in each array of nums sorted in ascending order.


Example 1:
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]

Example 2:
Input: nums = [[1,2,3],[4,5,6]]
Output: []


Constraints:
1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
"""

from collections import defaultdict

def intersectionMultipleArrays(nums: list[list[int]]) -> list[int]:

    n = len(nums)
    output = []

    # instantiate a hash map to hold integer frequency counts across the input matrix
    d = defaultdict(int)

    # construct a for loop that will traverse the rows in the input matrix
    for row in nums:

        # construct a for loop that will travser the array of numbers in each row
        for x in row:

            # increment the value in the hash map for each integer key traversed
            d[x] += 1

    # loop through the keys in the hash map
    for k in d.keys():

        # add values that appeared in each row to the output array
        if d[k] >= n:
            output.append(k)

    # return a sorted output array
    return sorted(output)
"""
Example 1:
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query.
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true].
For each query, the subarray sums are [12, 14, 12].
"""

def sumLimitQuery(nums: list[int],
                  queries: list[int],
                  limit: int) -> bool:
    
    prefix = [nums[0]] * len(nums)
    
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    output = []

    for x, y in queries:
        if prefix[y] - prefix[x - 1] < limit:
            output.append(True)

        else:
            output.append(False)
    
    return output
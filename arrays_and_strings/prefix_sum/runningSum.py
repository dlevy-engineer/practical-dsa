"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

def runningSum(nums: list[int]) -> list[int]:

    # instantiate a variable to hold the length of the input array
    n = len(nums)

    # instantiate an output array populated entirely with the first element of the input array
    output = [nums[0]] * n

    # construct a for loop that will run through the output variable from index position 1
    # populate each position with the cumulative sum to that point
    for i in range(1, n):
        output[i] = output[i - 1] + nums[i]

    return output
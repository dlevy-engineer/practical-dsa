"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

def sortedSquares(nums: list[int]) -> list[int]:

    # instantiate two pointers on either side of the number array, and an output array index to iterate backwards
    left = 0
    right = i = len(nums) - 1

    # instantiate an output list to make it easy and inexpensive to modify specific elements
    output = [0] * len(nums)

    # construct a while loop that will only run until the pointers meet or cross
    while left <= right:

        # if the absolute value of the left pointer is greater than the absolute value of the right pointer, add the square of it to the back of the output array
        if abs(nums[left]) > abs(nums[right]):
            output[i] = nums[left] ** 2
            left += 1

        # otherwise, add the square of the right pointer to the back of the output array
        else:
            output[i] = nums[right] ** 2
            right -= 1

        # iterate toward the left of the output array
        i -=1

    return output
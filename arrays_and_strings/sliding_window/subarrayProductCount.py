"""
Example 3:
713 – Subarray Product Less Than K (https://leetcode.com/problems/subarray-product-less-than-k/)

Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""

def subArrayProductCount(nums: list[int],
                         k: int) -> int:
    
    # instantiate a left pointer, a right pointer, and an output variable to keep track of the valid subarrays
    left = output = 0

    # instantiate a variable to track the cumulative product of the current window
    product = 1

# construct a for loop that will slide the right pointer along the array
    for right in range(len(nums)):

        # multiply by the rightmost integer to update the cumulative product
        product *= nums[right]

        # if we've exceeded the target, remove the leftmost integer and increment the left pointer until we're back in range
        while product >= k and left <= right:
            product //= nums[left]
            left += 1

        # update the output with the number of subarrays contained within our current valid subarray
        output += right - left + 1

    return output
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2


Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

from collections import defaultdict

def subarraySum(nums: list[int],
                k: int) -> int:

    # instantiate a prefix tracker variable and an output variable at 0
    prefix = output = 0

    # instantiate a hash map to store prefix frequencies
    freqs = defaultdict(int)
    # initialize the count of the null subarray sum, which is 0
    freqs[0] = 1

    # construct a for loop to traverse the input array
    for num in nums:

        # add the current number to our prefix variable
        prefix += num

        # if we are currently at an index with a subarray summing to k, then prefix - k must have been seen as a prefix before
        # so we add the frequency of that prefix value to our output variable
        output += freqs[prefix - k]

        # increment the current prefix frequency
        freqs[prefix] += 1

    return output
"""
Given an array of integers nums and an integer k, a continuous subarray is called nice if there are k odd numbers in it.

Return the number of nice sub-arrays.


Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2


Example 2:
Input: nums = [2,4,6], k = 1
Output: 0

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

from collections import defaultdict

def numNiceSubarrays(nums: list[int],
                     k: int) -> int:
    
    # instantiate a variable to track the number of odds seen thus far, as well as an output variable
    numodds = output = 0

    # instantiate a hash map to track the frequency of number of odds seen, and initialize the empty set [] as 0 odds seen
    freq = defaultdict(int)
    freq[0] = 1

    # construct a for loop to iterate over the input array
    for num in nums:

        # add to the number of odds seen if the current number is odd
        if num % 2 == 1:
            numodds += 1

        # if numodds - k odds have previously been seen,
        # then the frequency of that occurrence is the number of subarrays ending at the current index that have exactly k odds
        output += freq[numodds - k]

        # increment the current number of odds seen in the hash map
        freq[numodds] += 1
    
    return output
"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive).
If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division.
The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.


Example 1:
Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]

Example 2:
Input: nums = [100000], k = 0
Output: [100000]

Example 3:
Input: nums = [8], k = 100000
Output: [-1]


Constraints:
n == nums.length
1 <= n <= 105
0 <= nums[i], k <= 105
"""

def kRadiusSubarrayAverages(nums: list[int],
                            k: int) -> int:
    
    # if k is zero, we need not calculate averages, as the input array will suffice
    if k == 0:
        return nums
    
    # instantiate a variable to hold the length of the input array
    n = len(nums)

    # instantiate an averages array with -1 as the default, and a prefix array with an extra element on the left to accommodate our algorithm's logic
    avgs = [-1] * n
    prefix = [0] * (n + 1)

    # construct a prefix sum array for quick reference
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # construct a for loop that will run through the elements with valid k radius averages (not -1)
    for j in range(k, n - k):
        avgs[j] = (prefix[j + k + 1] - prefix[j - k]) // (2 * k + 1)

    return avgs
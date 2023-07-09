"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j,
and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.


Example 1:
Input: nums = [18,43,36,13,7]
Output: 54

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
"""

from collections import defaultdict

def maximumNumber(nums: list[int]) -> int:

    # define a function to retrieve the sum of the digits in a number
    def retrieveDigitSum(num):

        # start with a sum of 0
        dig_sum = 0

        # construct a while loop that will run until the number in question is fully decomposed
        while num:
            # add the ones digit to the cumulative sum
            dig_sum += num % 10

            # integer divison by 10 to remove the ones digit
            num //= 10

        return dig_sum
    
    # instantiate an output variable with the default value of -1
    output = -1

    # instantiate a hashmap to hold the most recent value associated a particular digit sum
    dig_sum_map = {}

    # loop over the input array
    for n in nums:

        # calculate the digit sum
        dig_sum = retrieveDigitSum(n)

        # if the digit sum currently exists in the hashmap, update the output value if the new sum exceeds the old sum
        if dig_sum in dig_sum_map:
            output = max(output, dig_sum_map[dig_sum] + n)

        # replace the current value mapped to this digit sum with the largest value found thus far
        dig_sum_map[dig_sum] = max(n, dig_sum_map.get(dig_sum, 0))

    return output
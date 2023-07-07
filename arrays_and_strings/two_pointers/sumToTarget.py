"""
Example 2:

Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.
This problem is similar to Two Sum (https://leetcode.com/problems/two-sum/).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""

def sumCheck(num_arr: list, 
              target: int) -> bool:
    
    # instantiate pointers on either edge of the number array
    left = 0
    right = len(num_arr) - 1

    # construct a while loop that will only run until the pointers meet or cross
    while left < right:

        # calculate the sum of the integers currently referenced by the pointers
        num_sum = num_arr[left] + num_arr[right]

        # if an undershot, increase the lower number
        if num_sum < target:
            left += 1

        # if an overshot, decrease the higher number
        elif num_sum > target:
            right -= 1

        # the only other possibility is equivalence, which returns True
        else:
            return True
        
    # if we make it all the way through the while loop, there is no integer pair that sums to the target
    return False
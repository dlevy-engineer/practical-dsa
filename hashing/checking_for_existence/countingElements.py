"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
If there are duplicates in arr, count them separately.

Example 1:
Input: arr = [1,2,3]
Output: 2

Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0


Constraints:
1 <= arr.length <= 1000
0 <= arr[i] <= 1000
"""

def countingElements(arr: list[int]) -> int:

    # convert the input array into a set for O(1) retrieval
    arr_set = set(arr)

    # instantiate a counter
    output = 0

    # loop through the values in our input array
    for num in arr:

        # increment the counter when the current value meets our counting criteria
        if num + 1 in arr_set:
            output += 1

    return output
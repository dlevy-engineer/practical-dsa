"""
Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
"""

def sortedArrayMerge(arr1: list,
                     arr2: list) -> list:
    
    # instantiate two pointers, both on the left hand side of their respective iterables
    i = j = 0

    # instantiate an output array to hold sorted elements as we iterate over the inputs
    output = []

    # construct a while loop that will only run until we reach the end of one of our input iterables
    while i < len(arr1) and j < len(arr2):

        # if the current element in array1 is smaller than that in array2, append it to the output
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1

        # otherwise, append the element in array2
        else:
            output.append(arr2[j])
            j += 1

    # if we have not completed iterating over array1, append the remaining elements to the output
    while i < len(arr1):
        output.append(arr1[i])
        i += 1

    # if we have not completed iterating over array2, append the remaining elements to the output
    while j < len(arr2):
        output.append(arr2[j])
        j += 1

    return output
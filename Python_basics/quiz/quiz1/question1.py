# Question 1: You are given a list of integers. Write a Python 
#function to find the maximum sum of any subarray that contains at least one negative number. 
#The subarray should be contiguous.
# Example:\
# Input: [2, -3, 5, -7, 2, 4, -1]\
# Output: 9 (subarray: [5, -7, 2, 4])

import numpy as np

def check_if_array_has_negative(sub_array):
    arr = np.array(sub_array)
    #print(sub_array)
    if np.any(arr < 0):
        #print("The NumPy Array has at least one negative value")
        return True
    else:
        #print("The NumPy Array does not have any negative values")
        return False


def find_max_sum_of_subarray_with_atleast_one_negative(input_array):
    maxSum = 0
    size_of_array = len(input_array)
    print(size_of_array)
    for i in range(0, size_of_array):
        currSum = 0
        for j in range(i, size_of_array):
            subArray = (input_array[i:size_of_array])
            if(check_if_array_has_negative(subArray)):
                currSum = currSum + input_array[j]
                if(currSum > maxSum):
                    maxSum = currSum
            else: 
                break
            
    return maxSum
    

numbers = str(input())
numbers = numbers.split(',')


for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

#print(numbers)
print(find_max_sum_of_subarray_with_atleast_one_negative(numbers))
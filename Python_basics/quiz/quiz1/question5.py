




def check_if_array_consecutive_numbers(sub_array):
    length_of_subarray = len(sub_array)
    element1=0
    element2=0
    element3=0
    for i in range(length_of_subarray):
        element1 = sub_array[i]
        if ((i+1) < length_of_subarray):
            element2 = sub_array[i+1] + 1
        if ((i+2) < length_of_subarray):
            element3 = sub_array[i+2] + 2
        
        if (element1 != element2 and element3 != element1 and element2 != element3 ):
            return True
        else:
            return False



def find_max_sum_of_subarray_with_no_consecutive_numbers(input_array):
    maxSum = 0
    size_of_array = len(input_array)
    print(size_of_array)
    for i in range(0, size_of_array):
        currSum = 0
        for j in range(i, size_of_array):
            subArray = (input_array[i:size_of_array])
            if(check_if_array_consecutive_numbers(subArray)):
                break
            else: 
                currSum = currSum + input_array[j]
                if(currSum > maxSum):
                    maxSum = currSum
            
    return maxSum
    

numbers = str(input())
numbers = numbers.split(',')


for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

#print(numbers)
print(find_max_sum_of_subarray_with_no_consecutive_numbers(numbers))
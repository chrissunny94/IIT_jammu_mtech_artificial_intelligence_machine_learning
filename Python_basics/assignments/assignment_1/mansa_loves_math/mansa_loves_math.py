#!/bin/python3

#import itertools

# def permute(data, i, length):
#     if i == length:
#         result.append(''.join(data) )
#     else:
#         for j in range(i, length):
#             # swap
#             data[i], data[j] = data[j], data[i]
#             permute(data, i + 1, length)
#             data[i], data[j] = data[j], data[i]


# all_combination = permute("chris", 0 , len("chris"))

# print(all_combination)


from itertools import permutations

# Initialising string
ini_str = "abc"
 
# Printing initial string
#print("Initial string", ini_str)
number_of_input = int(input())
OUTPUT_ = []
element_divisible = False
for input_x  in range(number_of_input):
    # Finding all permutation
    input_x = input()
    permutation = [''.join(p) for p in permutations(str(input_x))]
    element_divisible = False
    for element in permutation:
        if (int(element)%8 ==0):
            element_divisible = True
            break
    OUTPUT_.append(element_divisible)


for ouput in OUTPUT_:
    print(ouput)

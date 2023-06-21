#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def solve(n):
    # Write your code here
    count_of_zeros = n
    number_of_fives = 0
    output = 0
    for i in range(1,100):
        temp = i 
        #print(i)
        while (temp%5 == 0):
            number_of_fives += 1
            temp =temp/5
        if (number_of_fives == count_of_zeros):
            output = i
            break
    return output
        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input().strip())
    results = []
    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)
        results.append(result)
        #fptr.write(str(result) + '\n')

    for element in results:
        fptr.write(str(element) + '\n')
    fptr.close()

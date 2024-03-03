#!/bin/python3

import math
import os
import random
import re
import sys


    
    
def solve( input):
        lower = 0
        higher = 5 * n
        while lower <= higher:
            mid = (lower + higher) / 2
            cnt = prime_counter(5, mid)
            if cnt < input:
                lower = mid + 1
            else:
                higher = mid - 1
        return lower

def prime_counter(p, n):
    if n < p:
        return 0

    return n / p + prime_counter(p, n / p)

    

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdin
    fptr_out = sys.stdout
    
    t = int(input().strip())

    results = []
    
    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)
        results.append(result)
        #fptr_out.write(str(result) + '\n')
        # s = "%s\n" % result
        # print(s)

    for element in results:
        element= int(element)
        fptr_out.write(str(element) + '\n')
    
    fptr.close()

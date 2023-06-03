#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__      = "Chris Thaliyath"
__copyright__   = "Copyright 2023, Sum of digitst"

x=104
sum = 0
for i in str(x) :
    sum = sum + int(i)
    print (i)

print("SUM=",sum )

def sum_digits(integer):
    total = 0
    integer = abs(integer)
    while integer > 0:
        digit = integer % 10
        total += digit
        integer //= 10
    return total

def get_sum(num):
     sum = 0
     while num > 0:
         sum = sum + num % 10
         num = int(num /10)
     return sum


def sum_all(input: int) -> int:
     convert_input = str(input)
     sum = 0
     for i in convert_input:
          sum += int(i)
     return sum

x = 1074
sum=0
while x>0:
    a = x%10
    sum = sum + a
    x = x//10
print(sum)


print(sum)

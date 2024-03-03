import string
import random


n=int(input())
#l_h = input()
l_h = list(map(int, input().split()))
print(l_h)
# output_l_h = l_h.split(' ')
# print(n)
# for i in output_l_h:
#     print( i) 

 
# initializing size of string
N = 7
 
# using random.choices()
# generating random strings
res = ""
for i in range(n):
    res = ''.join(random.choices(string.ascii_letters, k=n)) + res
 
# print result
print (n)
print(l_h[0],l_h[1])
print( str(res))
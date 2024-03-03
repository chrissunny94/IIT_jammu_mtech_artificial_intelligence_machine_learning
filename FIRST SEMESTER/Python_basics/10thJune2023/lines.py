#draw parallel lines 
#find parallel lines
#n=int(input())
n =10
for i in range(n+1):
    print(i*'*')


n=10
for i in range(n):
  for i in range(i):
    print(i+1, end=" ")
  print()

for i in range(0,5):
  for j in range(i+1):
      print(j+1,end="")
  print('')



for i in range(0,10):
  for j in range(i+1,0 , -1):
      print(chr(ord('A')+i),end="")
  print('')


n =10
for i in range(n+1):
    print(int((n-i)/2)*' ',i*'*')


a = 3
for i in range(a):
    print(' ' * (a - i - 1) + '*' * (2 * i + 1))


n = 5
m = n-1

for i in range(n):
    for j in range(m):
        print(end=" ")

print()
n=10
for i in range(n):   
    print(' '*(n-i), '*'* (2*i+1))
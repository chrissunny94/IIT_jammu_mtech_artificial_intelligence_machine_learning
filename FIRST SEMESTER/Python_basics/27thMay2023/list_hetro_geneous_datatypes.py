

list = ["chris", "sunny", 10 , 20]

sum = 0
for i in list :
    if (isinstance(i , int)):
        sum = sum + i

print (sum)


v = ['vinit', 'raja', 'sohan', 10, 20]
sum = 0
for count in range (len(v)):
  if type(v[count]) == int:
    sum += v[count]
sum
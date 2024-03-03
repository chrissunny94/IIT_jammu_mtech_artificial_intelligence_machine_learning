a=[1,2,3,"aaaa",11]
sum =0
for i in a:
    try:
        sum = sum + i
    except:
         print("An exception occurred")


print (sum)

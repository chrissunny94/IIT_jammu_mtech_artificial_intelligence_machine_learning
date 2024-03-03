# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
 
# This will print every line one by one in the file
for each in file:
    print (each)


def main():
    counter = 0
    total = 0
    inputFile = open('Numbers.txt', 'r')

    for numbers in inputFile:
        print(numbers.rstrip().split())

        numbers = float(numbers.split())

        total += numbers
        counter += 1   

    print('Count:', counter)
    print('Total:', total)
    print('Average:', total / counter)

    inputFile.close()

main()


a = open('Numbers.txt', 'r')
max = -1
for text in a:
    nums = text.split()
    for i in nums:
        if max < int(i):
            max = int(i) 
print(max)

a=open('test.txt','r')
num=-1
try:
    for i in a:
        k=i.split()
        for j in k :
            if int(j) > num:
                num=int(j)
except:
    print('error')
finally:
    print('finally run')
    a.close()
print(num)
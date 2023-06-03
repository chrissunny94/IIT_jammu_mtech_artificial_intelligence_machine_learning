list=[]

list.append("chris")
print(list)
list.insert(1,2)

print(list)

#print the second highest element in the list

highest = 0
highest_count = False
# for i in list:
#     if  (i <)


# create a list
list_numbers = [2, 3, 5, 7, 9, 11]

max_element = max(list_numbers)

list_numbers.remove(max_element)

second_highest = max(list_numbers)

print(second_highest)


# 2nd max
ref = [2,3,4,5]
sec_high = -999
_high = -999
# get the highest
for num in ref:
    _high = max(num, _high)
# get second highest
for num in ref:
    if num < _high:
        sec_high = max(num, sec_high)
    
print(sec_high)



# list_of_lists = [1 , [2,4] , 6 , 999 , [999,1]]

# max_value = 0
# index = 0
# for element in list_of_lists:
#     print(element)
#     if (type(element) is list):
#         if (sum(element) >= max_value ):
#             max_value = sum(element)
#             index = list_of_lists.index(element)
#     else:
#         if( sum(element) > max_element):
#             max_value = element
#             index = list_of_lists.index(element)


# ###############
# list = [1, [2,3], [7,4]]

# def sumfunc(list):
#     sum = 0
#     if type(list) == list:
#         for x in list:
#             sum += x 
#     else:
#         sum = list
#     return sum
    
    
# largestIndex = -1  
# largest = 0
# for i in range(len(list)):
#     if sumfunc(list[i]) > largest:
#         largest = sumfunc(list[i])
#         largestIndex = i 

# print(largestIndex)



# input_email_id = input()
# output_string = input_email_id.split('@')

# print ("name Of person:",output_string[0])
# print ("name Of company:",output_string[1])
    


# Updated my code
email = "test@iitjammu.xyz.gbc"
org = email.split('@')
print(org[1].split('.')[0])


# sort list of strings
# sort according to alphabetically sort

list_of_strings = ["bosch" , "conti" , "merc" , "bmw" , "audi" , "Toyota"]
print("UnsortedList", list_of_strings)

for i in range(len(list_of_strings)):
    for j in range(len(list_of_strings)-i -1):
        if (list_of_strings[j][1] > list_of_strings[j+1][1]):
            temp = list_of_strings[j]
            list_of_strings[j] = list_of_strings[j+1]
            list_of_strings[j+1] = temp

print("SortedList", list_of_strings)


# reverse a list without using a additional list

list_of_numbers = [1,2,3,4,5,6,7]


a = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(a)):
    v = a.pop()
    a.insert(i, v)

print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index= 0
max_value = 0
for i in a:
    if i > max_value:
        max_value = i
        del a[index]
        a.insert(0, max_value)
    index+=1
print(a)
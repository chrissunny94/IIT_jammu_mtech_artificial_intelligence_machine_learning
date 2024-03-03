def find_longest_word(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


mylist = ["soumik","aaa","bbb",10,20]
sum = ""
maxlength = 0
for x in mylist:
    if(type(x)==str):
        if(len(x)>maxlength):
            maxlength = len(x)
            sum = x
print(sum)

list1=['sumit', 'kumar', 10, 20, 'TRUE']
print (list1)
lengthmax=0
lengthmin=0
for i in list1:
    if (type(i)==str):
        lengthmax=len(i)
        if(lengthmin<lengthmax):
            lengthmin=lengthmax

print (lengthmin)
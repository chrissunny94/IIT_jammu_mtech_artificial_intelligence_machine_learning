#count the number of occurances of different word in a song lyric

# a = open('nattunattu.txt', 'a')
# max = -1
# list_of_words={}
# for text in a:
#     line = text.split()
#     print(line)
#     for word in line:
#         if word not in list_of_words:
#             list_of_words[word]=1
#         else:
#             list_of_words[word]+= 1


# print (list_of_words)

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 =str1+' '+ ele
 
    # return string
    return str1


f = open("nattu_nattu_output.txt", "a+")
a = open('nattunattu.txt', 'r+')

for text in a:
    line = text.split()
    output = listToString(line) +' '+ str(line.count("Naatu"))+ "\n"
    print(output)
    f.write(output)

f.close()

        
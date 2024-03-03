
def FindlongestCommonPrefix( input_array_of_strings):
     
    size = len(input_array_of_strings)
    if (size == 0):
        return ""
 
    if (size == 1):
        return input_array_of_strings[0]
    input_array_of_strings.sort()
    
    #hack to find the smallest string amonsgst the list of strings
    minimum_length_of_string=len(input_array_of_strings[0])
    for i in range(len(input_array_of_strings)):
        minimum_length_of_string = min(minimum_length_of_string,len(input_array_of_strings[i]))
   
    count = 0
    while (count < minimum_length_of_string and
           input_array_of_strings[0][count] == input_array_of_strings[size - 1][count]):
        count =count+ 1
 
    prefix_output = input_array_of_strings[0][0: count]
    return prefix_output

input = str(input())
input_string_array = input.split(',')

output = FindlongestCommonPrefix(input_string_array)
print(output)
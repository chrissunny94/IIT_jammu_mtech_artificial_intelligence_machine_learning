input_number_of_elements = int(input())

numbers = []

numbers = str(input())
numbers = numbers.split(' ')

# for i in range(input_number_of_elements):
#     element = int(input())
#     numbers.append(element)    

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])
    
# Function takes a list as input
def Reverse(numbers):
      # Base case when the list is only one item
      if (len(numbers)==1):
         return numbers
      # Otherwise
      return Reverse(numbers[1:]) + numbers[0:1]
 
# Test function

reversed_numbers = Reverse(numbers)
reversed_numbers_string = ''
element_1 = True
for element in reversed_numbers:
    if(element_1):
        reversed_numbers_string =  str(element)
        element_1 = False
    else:
        reversed_numbers_string = reversed_numbers_string + ' ' + str(element)


print(reversed_numbers_string)
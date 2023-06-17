# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


number_of_test_cases = input()
OUTPUT_array = []
for i in range(int(number_of_test_cases)):
    INPUT_VALUE = int(input())
    FACTORIAL=factorial(INPUT_VALUE)
    SUM_OF_FACTORIAL=0
    for c in str(FACTORIAL):
        SUM_OF_FACTORIAL = SUM_OF_FACTORIAL + int(c)
        
    OUTPUT_array.append(SUM_OF_FACTORIAL)

for i in OUTPUT_array:
    print(i)
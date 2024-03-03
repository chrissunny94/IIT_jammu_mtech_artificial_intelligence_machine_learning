list =["chri" , "sunny"]

alphabet_to_find_frequency_of = 'n'

max_frequency = 0
string_with_max_frequency=""
for i in list:
    frequency = 0
    for x in i:
        if(x== alphabet_to_find_frequency_of):
            frequency+=1
        if(frequency>max_frequency):
            max_frequency=frequency
            string_with_max_frequency = i


print("string:", string_with_max_frequency , "Frequency:",max_frequency)



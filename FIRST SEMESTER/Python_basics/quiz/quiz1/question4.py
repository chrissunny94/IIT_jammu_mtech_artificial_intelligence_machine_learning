
def longest_string_after_deleting_a_charecter(input_string_array):
    number_of_words = len(input_string_array)
    max_length = -1
    max_length_word = ""
    for i in range(number_of_words):
        for charracter in input_string_array[i]:
            #print(charracter)
            word_after_charracter_removed = input_string_array[i].replace(charracter,'')
            if (max_length < len(word_after_charracter_removed)):
                max_length_word = input_string_array[i]

    return max_length_word


input = str(input())
input_string_array = input.split(',')

print(longest_string_after_deleting_a_charecter(input_string_array))
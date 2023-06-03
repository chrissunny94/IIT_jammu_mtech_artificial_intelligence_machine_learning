#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__      = "Chris Thaliyath"
__copyright__   = "Copyright 2023, Sum of digitst"


# Given a word , find the freqency of an anphabet 


Input_string = "I love India !"
Matching_alphabet = 'c'
Frequency = 0
for i in Input_string:
    if (i == Matching_alphabet):
        Frequency= Frequency+1
print("Frequency=", Frequency)


def count_character(word, character):
    count = 0
    for char in word:
        if char == character:
            count += 1
    return count

word = "india"
character = "i"
count = count_character(word, character)
print(count)


val = "iitjammu"
count = 0
for i in val:
    count = count + 1 if (i == "i") else count
print(count)

def get_i_count(value):
    sum = 0
    for char in value:
         if char == 'i':
              sum += 1
    return sum


x ="abhishek"
count=0
for a in x:
	if a=="i":
		count=count+1

print(count)


def count_occurrences(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count


def frequency_char(word, character):
	count = 0
	for ch in word:
		if ch == character:
			count += 1
	return count



i='iitjammu'
count = 0
for k in i:
    if k=='i':
        count = count+1
    else:
        pass

x = 'IIT Jammu'
count = 0
for i in x:
    if i=="I":
        count = count + 1
print(count)


string = "abbjfrirvnirnvi"
freq = 0
string1 = "i"
for char in string:
    if string1 in char:
        freq += 1
print(freq)


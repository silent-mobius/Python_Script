#!/usr/bin/env python3

# map() example
def calculateSquare(n):
      return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

## converting map object to set
numbersSquare = set(result)
print(numbersSquare)


# same with lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

## converting map object to set
numbersSquare = set(result)
print(numbersSquare)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# filter() example

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filter_vowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filtered_vowels = filter(filter_vowels, alphabets)

print('The filtered vowels are:')
for vowel in filtered_vowels:
    print(vowel)
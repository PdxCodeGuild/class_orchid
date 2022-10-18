"""
Lab 10: Version 1
Cesar Rebolled
"""


import string # import mod of string to use later. 

letters = string.ascii_lowercase # this is the list of characters.
user_input = input('Enter a word: ').lower() # takes in input string and converts it to lower case



"""
function rot13:

checking to see if character is a an empty space or punctuation, if it is
it will simply add that specific character to the cipher variable. 
Else it will assign a new variable called index which will give the index position of 
the character and then it - 13. This will give me either a + or - int. 
cipher will then be updated with index value in letters. 
If negative number it will start at the end and work back. 

"""
def rot13(input):
    cipher = '' 
    for character in input: 
        if character == ' ' or character in string.punctuation: 
            cipher += character
        else: 
            index = letters.index(character) - 13 
            cipher += letters[index]
    return cipher
    
print(rot13(user_input))


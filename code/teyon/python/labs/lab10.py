#introduction to rot13 translator
print("Welcome to ROT13 Translator!\n")

#ask the user to input a word to be translated
user_input = input("Type a word to be translated: ")

#convert all letters to lower case in the event the user inputs a uppercase letter
user_input = user_input.lower()
#print the users input 
print(f"\nYou input: {user_input}")

#convert the user_input string into a list
converted_user_input = list(user_input)

#dictionary which holds the conversion of each letter
rot13_conversion = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm',
    ' ': ' '
    }


#blank list which will hold the converted input_user list into a list of rot13 translated letters
converted_list = []

#for loop which takes each letter in the converted_user_input as it iterates through 
#and converts them and places them in the blank list above as they are converted 
for letter in converted_user_input:
    #take each letter in the list and runs it through the rot13 dictionary to compare it 
    #to a key.
    conversion = rot13_conversion[letter]
    #once a key and letter are matched the value of the key is output and added to the blank
    #converted_list list.
    converted_list.append(conversion)

#blank string with variable name rot13
rot13 = ''

#for loop that takes each converted letter in the converted_list 
# and adds it to the blank string rot13 each iteration
for letters in converted_list:
    #rot13 adding each letter to blank string each loop through
    rot13 += letters

#printing the input and translated output 
print(f"\n{user_input} converted to ROT13: {rot13}")



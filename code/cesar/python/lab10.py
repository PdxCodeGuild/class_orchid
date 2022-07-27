import string


letters = string.ascii_lowercase
user_input = input('Enter a word: ').lower()

remove_spaces = user_input.replace(' ', '')

print(remove_spaces)

def rot13(input):
    cipher = ''
    for x in input:
        index = letters.index(x) - 13 
        cipher += letters[index]
    return cipher

print(rot13(remove_spaces))
   

    


        





english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot =     ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def encryp_word(user_input):
    encryp =''
    for char in user_input:
        if char == ' ':
            encryp += char
        else:
            index = english.index(char)
            encryp += rot[index]
    return encryp

def decryp_word(user_input):
    decryp =''
    for char in user_input:
        if char == ' ':
            decryp += char
        else:
            index = rot.index(char)
            decryp += english[index]
    return decryp

#version 2####################################################
def encryp_choice_rotations(user_input, user_rotations):
    rotated = ''
    for l in user_input:
        rotations = user_rotations
        if english.index(l) + user_rotations > 25:
            rotations = (english.index(l) + user_rotations) - 26
        else:
            rotations = english.index(l) + user_rotations
        rotated += english[rotations]
    return rotated

def decryp_choice_rotations(user_input, user_rotations):
    rotated = ''
    for l in user_input:
        rotations = user_rotations
        if english.index(l) - user_rotations < 0:
            rotations = (english.index(l) - user_rotations) + 26
        else:
            rotations = english.index(l) - user_rotations
        rotated += english[rotations]
    return rotated
##############################################################

user_input = '0'

while user_input != '':
    print('\nPress enter to exit')
    user_input = input('Enter a word to encryp: ').lower()
    if user_input == '': break
    user_input_encryp = encryp_word(user_input)
    print('Encryp: ', user_input_encryp)
    
    user_input = input('Enter a word to decryp: ').lower()
    if user_input == '': break
    user_input_decryp = decryp_word(user_input)
    print('Decryp: ', user_input_decryp)

    user_rotations = int(input('Enter a number of times to rotate a word: '))
    user_input = input(f'Enter a word to encryp {user_rotations} rotations : ').lower()
    print(encryp_choice_rotations(user_input, user_rotations))
    
    user_rotations = int(input('Enter a number of times to rotate a word: '))
    user_input = input(f'Enter a word to decryp {user_rotations} rotations : ').lower()
    print(decryp_choice_rotations(user_input, user_rotations))
print('bye\n')
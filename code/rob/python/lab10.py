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

user_input = '0'

while user_input != '':
    print('\nPress enter to exit')
    user_input = input('Enter a word to encryp: ')
    if user_input == '': break
    user_input_encryp = encryp_word(user_input)
    print('Encryp: ', user_input_encryp)
    
    user_input = input('Enter a word to decryp: ')
    if user_input == '': break
    user_input_decryp = decryp_word(user_input)
    print('Decryp: ', user_input_decryp)

    #version 2####################################################
    rotations = input('Choose number of times to encryp/decryp: ')
    if rotations.isnumeric(): rotations = int(rotations)
    else: 
        print('Must be a number') 
        break
    if rotations == '': break
    
    rotated_num = rotations
    user_input = input('Enter a word to rotate: ')
    if user_input == '': break
    rotated = ''
    while rotations > 0:
        if rotations > 0:
            rotated = encryp_word(user_input)
            rotations -= 1
        if rotations > 0:
            rotated = decryp_word(user_input)
            rotations -= 1
    print(f'Rotated {rotated_num} times: ', rotated)
    ##############################################################
print('bye\n')
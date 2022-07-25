english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot =     ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

user_input = input('Enter a word to ROT+13: ')

def rotate_word(user_input):
    encryp =''
    for char in user_input:
        index = english.index(char)
        encryp += rot[index]
    return encryp

user_input_encryp = rotate_word(user_input)

print(user_input_encryp)

"""
Lab 10: ROT Cipher
"""
to_be_encrypted = input('Enter your word(s) to be enctypted: ').lower()


def encryptor(word:str):
    """takes in a word as a string and returns that string as a rot13 string"""
    english = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    ' '
]
    rot13 = [
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    ' '
]
    encrypted = []
    for letter in word:
        index = english.index(letter)
        encrypted.append(rot13[index])
        encrypted_alt = ''.join(encrypted)
    return encrypted_alt
        
    

print(encryptor(to_be_encrypted))



'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 10: ROT Cipher'''

import string

plaintext_list = []
plaintext = input("Please enter the phrase you would like to encrypt. \n")
basic = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',)
caps_list = [letter.capitalize() for letter in basic]

for char in plaintext:
    plaintext_list.append(char)

encrypted_list = []
for letter in plaintext_list:
    if letter in basic:
        i = basic.index(letter)
        cipher = basic[i+ 13]
        
    
    elif letter in caps_list:
        i = caps_list.index(letter)
        cipher = caps_list[i+13]
        
    
    else: 
        cipher = " "

    encrypted_list.append(cipher)


message = ""
for item in encrypted_list:
    message += item

print(message)




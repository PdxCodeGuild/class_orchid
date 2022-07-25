'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 10: ROT Cipher'''

plaintext_list = []
plaintext = input("Please enter the phrase you would like to encrypt. \n")
for char in plaintext:
    char = char.lower()
    plaintext_list.append(char)


basic = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)


print(plaintext_list)
encrypted_list = []
for letter in (plaintext_list):
    if letter in basic:
        i = basic.index(letter)
        cipher = basic[i+ 13]
        print(cipher)
        encrypted_list.append(cipher)

message = ""
for item in encrypted_list:
    message += item

print(message)




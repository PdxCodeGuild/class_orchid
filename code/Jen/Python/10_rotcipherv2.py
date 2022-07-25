'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 10: ROT Cipher'''

plaintext_list = []
plaintext = input("Please enter the phrase you would like to encrypt. \n")
rot = input("Please enter how many characters you would like to rotate. \n")
rot = int(rot)
if rot >= 26:
    rot = round(rot % 26)  

for char in plaintext:
    char = char.lower()
    plaintext_list.append(char)


basic = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)

encrypted_list = []

for letter in plaintext_list:
    i = basic.index(letter)
    code = basic[i + rot]
    encrypted_list.append(code)
    print(code)

   
print(encrypted_list)

message = ""
for item in encrypted_list:
    message += item

print(message)



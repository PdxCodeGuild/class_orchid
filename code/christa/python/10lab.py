# Lab 10 : ROT Cipher

# Write a program that prompts the user for a string, 
# and encodes it with ROT13. For each character, 
# find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, 
# so encryption is the same as decryption.

# look at w3schools.com for string methods and try that  

message = input("Please enter a few words or a sentence: ")

#https://www.w3schools.com/python/ref_string_maketrans.asp
rot13 = message.maketrans(    
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
)

encrypt = message.translate(rot13)
#decrypt = encrypt.translate(rot13)

print(encrypt)
#print(decrypt)


 



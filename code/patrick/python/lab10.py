


cipher1 = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


cipher2 = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"



user_string = input(f"/nPlease enter a phrase: ")

from string import punctuation
print(punctuation)


final_output = ""
for letter in (user_string):
    
    cor_num = cipher1.index(letter)
    
    final_output += cipher2[cor_num]
    
  

print("the coded messege is: ", final_output)







cipher1 = "abcdefghijklmnopqrstuvwxyz"


cipher2 = "nopqrstuvwxyzabcdefghijklm"



user_string = input(f"/nPlease enter a one word phrase: ")




final_output = ""
for letter in (user_string):
    print(letter)
    cor_num = cipher1.index(letter)
    print(cor_num)
    final_output += cipher2[cor_num]
    
  

print(final_output)




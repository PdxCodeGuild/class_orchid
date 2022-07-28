


cipher1 = " abcdefghijklmnopqrstuvwxyz"


cipher2 = " nopqrstuvwxyzabcdefghijklm"



user_string = input(f"/nPlease enter a one word phrase: ")




final_output = ""
for letter in (user_string):
    
    cor_num = cipher1.index(letter)
    
    final_output += cipher2[cor_num]
    
  

print("the coded messege is: ", final_output)




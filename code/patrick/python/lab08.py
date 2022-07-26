


print(f"\nWelcome to credit card validation")

card_number = input(f"\nPlease enter your card number for validation ")

nums = []
converted_string = []
def convert_string(string):
    converted_card_number = list(string)
    return converted_card_number
    #return converted_card_number
    #print(converted_card_number)
    
    
    #




#print(nums)
##  4556737586899855
#check_digi = nums
#print(nums)
#print(check_digi)
converted_string = convert_string(card_number) 

#print(converted_string)

   
check_number = converted_string.pop(15)

print(check_number)

#print(converted_string)

reversed_string = converted_string[::-1]

print(reversed_string)

mulitplied_list = reversed_string[: ]
mulitplied_list[::2] = [x*2 for x in mulitplied_list[::2]]


print(mulitplied_list)




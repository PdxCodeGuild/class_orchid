


print(f"\nWelcome to credit card validation")

card_number = input(f"\nPlease enter your card number for validation ")

nums = []
converted_string = []
def convert_string(string):
    converted_card_number = list(string)
    return converted_card_number
   
    
    
converted_string = convert_string(card_number) 

#print(converted_string)

   
check_number = converted_string.pop(15)

#print(check_number)

#print(converted_string)

reversed_string = converted_string[::-1]

#print(reversed_string)

mulitplied_list = reversed_string[: ]
mulitplied_list[::2] = [int(x)*2 for x in mulitplied_list[::2]]



#print(mulitplied_list)

mulitplied_list = list(mulitplied_list)

#print(type(mulitplied_list))

multiplied_list_int = []
for item in mulitplied_list:
    item = int(item)
    multiplied_list_int.append(item)

#print(multiplied_list_int)

minus_9_list = []
for item in multiplied_list_int:
    if item <= 9:
        minus_9_list.append(item)
    if item >= 9:
        item = item - 9
        minus_9_list.append(item)
        
#print(minus_9_list)

added_list = sum(minus_9_list)

int_check_num = int(check_number)
#print(type(int_check_num))
#print(added_list)

changed_added_list = added_list % 10

#print(changed_added_list)
#print(type(changed_added_list))
#print(int_check_num)
#print(type(int_check_num))


if changed_added_list == int_check_num:
    print("verification Successful")
if changed_added_list != int_check_num:
    print("unsuccessful")



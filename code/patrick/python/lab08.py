print(f"\nWelcome to credit card validation")

card_number = input(f"\nPlease enter your card number for validation ")

#print(type(card_number))
#card_number = int(card_number)




#print(card_number)
#print(type(card_number))

def convert_string(string):
    converted_card_number = list(string)
    
    #return converted_card_number
    #print(converted_card_number)
    for item in converted_card_number:
        nums = []
        nums = item.split(",")
        print(nums[0])
        #check_number = nums[-16:0:1]
        #check_number = nums.pop(-1)    
    print(nums)
    #print(nums)
    return nums
    
    #print(type(converted_card_number))


##  4556737586899855
#for num in nums:
    #num * 2


converted_string = convert_string(card_number) 


#print(type(converted_string))
#converted_string = int(converted_string)
#print(type(converted_string))
print(converted_string)
print(converted_string)



#converted_string = converted_string
#converted_string.s

#print(converted_string[::16])

# card_number = int(card_number)

#check_number = converted_string.pop((-1))

#print(converted_string)
#print(check_number)
#print(check_number)
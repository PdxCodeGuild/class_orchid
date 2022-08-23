# ask the user to enter there credit card number
credit_card = input("Please type your credit card number: ")

#create a function that validates the user credit card number
def validator():
    #convert the user input into a list
    credit_card_list = list(credit_card)
    #takes the string in each index[i] for credit card list and enumerates it adding a counter with 
    #a value in that place
    for i,number in enumerate(credit_card_list):
        #takes the newly enumerated credit_card list and typecasts each string in the list
        #into a integer
        credit_card_list[i] = int(number)
    #uses the pop method to remove the final item in the list and creates a variable to hold that last item
    check_digit = credit_card_list.pop(-1)
    
    #takes the credit card list and reverses it using a slicing method
    credit_card_list = credit_card_list[::-1]
    #take the indices and the items stored in each index and enumerates it before changes are made
    for i,num in enumerate(credit_card_list):
        #if the index is divisable by two with no remainder than it is a even number index
        if i % 2 == 0:
            #takes each index that is divisible by two without a remainder ensuring that it is an even number
            #and multiplies the item in that index by 2
            credit_card_list[i] = num * 2
    #takes the index and numbers in the credit _card_list and makes it iterable by using enumerate
    for i, num in enumerate(credit_card_list):     
        #after multiplying each even index by 2 uses if statment to find 
        # any number in the list greater than 9  
        if num > 9:
            #takes the items greater than 9 and subtracts 9 from them
            credit_card_list[i] = num - 9
    #create a variable that takes the list and finds the sum
    list_sum = sum(credit_card_list)
    
    #takes the sum of the list and use modulo ten to find the remainder
    remainder = list_sum % 10
    print(remainder)
    
    #uses if statement to check if the remainder and the check digit from earlier match
    if remainder == check_digit:
        print("THIS IS A VALID CREDIT CARD")
    else:
        print("THIS IS NOT A VALID CREDIT CARD")

#calls on the function validator to run
validator()


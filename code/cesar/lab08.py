"""
Lab 8: Credit Card Validation 

The credit card number to check is: 4556737586899855 

"""
card_number_input = list(input('Enter your credit card number: ')) # Turns the input into a list. 

def credit_card_validation(card_number):
    check_digit = int(card_number.pop()) # Pops out the last element in the list to check later. 
    card_number =  card_number[::-1] # This will reverse the list. 

    for index, number in enumerate(card_number): # This will double every other digit
        number = int(number) # converts all the numbers to an int as they were in a string before. 
        card_number[index] = number
        
        if index % 2 == 0:   # Checks to see every other index to double.        
            card_number[index] = number * 2 
    for index, number in enumerate(card_number): # This will subtract 9 from digits over 9
        if number > 9:
            card_number[index] = number - 9 
    sum = 0
    for number in card_number: # Adding all the numbers in the list of card_number 
        sum += number
        sum_check = sum % 10 # Variable sum_check to get the last digit of the sum. 
    if sum_check == check_digit: # This if will return a true or false bool. 
        return True
    else:
       return False
        
answer = credit_card_validation(card_number_input)
if answer:
    print('This is a VALID credit card number')
else:
    print('This is NOT valid credit card number')
   
    
    
    
    
   
    
         

        



    
        
        
    
 
    
        

    

   


    
            
            
       
    







    


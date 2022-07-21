# Lab 08 Credit Card Validation

cc_digits = []                       #Create an empty list to append input digits
check_digits = []                    #Creat an empty list to append pop'd digit

while len(cc_digits) < 16:       #1. get the 16 digit cc number and 
    cc_num = int(input("Please your credit number one number at a time: "))    #convert input to integer
    cc_digits.append(cc_num)                #and add to list
print(cc_digits)
#-----------------------------------------------------------------------------------------------------------#
check_digit = cc_digits.pop()                #2. slice off the last digit. That is the check digit
check_digits.append(check_digit)             #move pop'd digit to check_digit list
#------------------------------------------------------------------------------------------------------------#
cc_digits.reverse()                                   #3. Reverse the digits
#cc_digits[::2] = [2*i for i in cc_digits[::2]]     #this worked but wasn't sure how to use it to proceed with rest of code
#--------------------------------------------------------------------------------------------------------------#
worked_digits = []                           #create an empty list for modified and verified digits
for i, digit in enumerate(cc_digits):              #referenced jackalopes lab where Pete helped  
    if i % 2 == 0:                                #4. Double every other element in the reversed list
        doubled_digit = int(digit) * 2   
#---------------------------------------------------------------------------------------------------------------#  
        if doubled_digit > 9:                           #5. Subtract nine from numbers over nine
            doubled_digit = doubled_digit - 9           #used help from teclado website      
        worked_digits.append(doubled_digit)             #move new digit to worked list
    else:    
        worked_digits.append(int(digit))               #for all other digit that didn't need worked, move to worked list
#-----------------------------------------------------------------------------------------------------------#
total = check_digits[0] + sum(worked_digits)    #6. Sum all values
print(total)
#-----------------------------------------------------------------------------------------------------------#
check_var = total % 10                            #7 Take the second digit of that sum
print(check_digits)
print(check_var)
#-----------------------------------------------------------------------------------------------------------#
if check_digits == check_var:                      #8. If that matches the check digit, 
    print("Valid")                                    #the whole card number is valid
else:
    print("Invalid")                                #If it does not match check digit, invalid
#-----------------------------------------------------------------------------------------------------------#
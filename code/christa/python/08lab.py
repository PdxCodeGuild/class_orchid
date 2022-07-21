# Lab 08 Credit Card Validation

cc_digits = []
check_digits = []

#1. get the 16 digit cc number and convert input to integer and add to list
while len(cc_digits) < 16:
    cc_num = int(input("Please individually enter each digit of your credit number. Enter only one number at a time: "))
    cc_digits.append(cc_num)


#print(cc_digits)

#2. slice off the last digit. That is the check digit
check_digit = cc_digits.pop()
check_digits.append(check_digit)

#print(check_digits)


#3. Reverse the digits
cc_digits.reverse()
print(cc_digits)

#4. Double every other element in the reversed list

cc_digits[::2] = [2*i for i in cc_digits[::2]]

print(cc_digits)

while num in cc_digits > 9:
    if num > 9:
        num = num - 9
    
    
print(cc_digits)



#5. Subtract nine from numbers over nine

"""for i in cc_digits:
    if i > 9:
       i = i - 9
    
"""

#6. Sum all values


#7 Take the second digit of that sum


#8. If that matches the check digit, the whole card number is valid

#print(cc_digits)


    

# if verify_length != 16:
print('Hello and Welcome!')

numbers = input('Please enter the numbers you would like converted: ')
 
x = int(numbers)

tens_digit = x//10
    # this  returns 6 7 in the terminal when printed
ones_digit = x%10

tens = {
     1 : 'ten',
     2 : 'twenty',
     3 : 'thirty',
     4 : 'fourty',
     5 : 'fifty',
     6 : 'sixty',
     7 : 'seventy',
     8 : 'eighty',
     9 : 'ninety'
}

ones = {
     0 : 'zero',
     1 : 'one',
     2 : 'two',
     3 : 'three',
     4 : 'four',
     5 : 'five',
     6 : 'six',
     7 : 'seven',
     8 : 'eight',
     9 : 'nine',
}

teens = {
     1: 'eleven',
     2: 'twelve',
     3: 'thirteen',
     4: 'fourteen',
     5: 'fifteeen',
     6: 'sixteen',
     7: 'seventeen',
     8: 'eighteen',
     9: 'nineteen'
}

if tens_digit == 0 and ones_digit == 0 : # conversion for 0
     print(f'Your conversion is: {ones[ones_digit]}')
          
elif tens_digit == 0 and ones_digit <= 9: #ones 1-9 conversion
     print(f'your conversion is: {ones[ones_digit]}')

elif tens_digit == 1 and ones_digit == 0: #10 conversion
     print(f'Your conversion is: {tens[tens_digit]}')

elif tens_digit == 1 and ones_digit <= 9: #teens 11-19 conversion
     print(f'your conversion is: {teens[ones_digit]}')

elif tens_digit <= 9 and ones_digit == 0: # tens 20-90
     print(f'your conversion is: {tens[tens_digit]}')

elif tens_digit <= 9 and ones_digit <= 9: # tens and one 67
     print(f'your conversion is: {tens[tens_digit]}-{ones[ones_digit]}')


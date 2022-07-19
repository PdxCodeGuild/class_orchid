print('Hello and Welcome!')

number = input('Please enter the numbers you would like converted: ')
 
number = int(number)

hundreds_digit = number//100

tens_digit = number//10 %10

ones_digit = number%10

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
     1 : 'eleven',
     2 : 'twelve',
     3 : 'thirteen',
     4 : 'fourteen',
     5 : 'fifteeen',
     6 : 'sixteen',
     7 : 'seventeen',
     8 : 'eighteen',
     9 : 'nineteen'
}

tens = {
     0 : '',
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

hundreds = {
    1 : 'one hundred',
    2 : 'two hundred',
    3 : 'three hundred',
    4 : 'four hundred',
    5 : 'five hundred',
    6 : 'six hundred',
    7 : 'seven hundred',
    8 : 'eight hundred',
    9 : 'nine hundred'
}

ones_string = ''
tens_string = ''
teens_string = ''
hundreds_string = ''

if hundreds_digit == 0:

    if tens_digit == 0 and ones_digit == 0 : # conversion for 0
        ones_string = ones[ones_digit]
            
    elif tens_digit == 0 and ones_digit <= 9: #ones 1-9 conversion
        ones_string = ones[ones_digit]

    elif tens_digit == 1 and ones_digit == 0: #10 conversion
        tens_string = tens[tens_digit]

    elif tens_digit == 1 and ones_digit <= 9: #teens 11-19 conversion
        teens_string = teens[ones_digit]
        
    elif tens_digit <= 9 and ones_digit == 0: # tens 20-90
        tens_string = tens[tens_digit]

    elif tens_digit <= 9 and ones_digit <= 9: # tens and one 67
        tens_string = tens[tens_digit]+'-'
        ones_string = ones[ones_digit]

else:

    #check if number has a teen above 99.
    if tens_digit == 1 and ones_digit <= 9: #teens 11-19 conversion
        teens_string = teens[ones_digit]


    else:
        hundreds_string = hundreds[hundreds_digit]
        tens_string = tens[tens_digit]
        ones_string = ones[ones_digit]

        hundreds_string = hundreds[hundreds_digit]

        if ones_string == 'zero':
            ones_string = ''
            
            if tens_string != '':
                hundreds_string += ' '

        elif tens_string == '':
            hundreds_string += ' '

        else:
            tens_string +=  ' '

nums_String = hundreds_string + teens_string + " " +  tens_string + ones_string

print(f"Your number is {nums_String}")

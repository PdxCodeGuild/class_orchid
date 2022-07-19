# Dictionary for hundreds, tens, teens and ones to convert to words. 
hundreds = {
    0: '',
    1: 'one hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred',
    9: 'nine hundred'
}

tens = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forthy',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

ones = {

    0: ' ',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

# prompt to enter a number. Assigning to variable and typecast to int
number_to_convert = int(input(f'Hello, please enter a numeber from 0-999 to convert to words: '))


# hundreds_digits = number_to_convert // 100
# tens_digit = (number_to_convert % 100) 
# ones_digit = number_to_convert % 10

# print(hundreds_digits, tens_digit, ones_digit)

# If loop to check for int value of variable.


if number_to_convert == 0:
    output = 'zero'

elif number_to_convert < 10:
    output = ones[number_to_convert] 

elif number_to_convert < 20 and number_to_convert >= 10:
    output = teens[number_to_convert]

elif number_to_convert >= 20 and number_to_convert < 100:
    tens_digit = number_to_convert // 10
    ones_digit = number_to_convert % 10
    output = tens[tens_digit] + " " + ones[ones_digit]
    
elif number_to_convert >= 100:
    hundreds_digits = number_to_convert // 100
    tens_digit = (number_to_convert % 100) // 10
    ones_digit = number_to_convert % 10

    if tens_digit == 0:
            output = hundreds[hundreds_digits] + ' ' + ones[ones_digit]

   
            output = hundreds[hundreds_digits] + ' ' + teens[tens_digit]
     output = hundreds[hundreds_digits] + ' ' + ones[ones_digit]
    elif ones_digit == 0:
            output = hundreds[hundreds_digits] + ' ' + tens[tens_digit]
    if ones_digit == ' ':
            output = hundreds[hundreds_digits]

if number_to_convert >= 100 and tens_digit > 10 and tens_digit < 20:
    output = hundreds[hundreds_digits] + ' ' + teens[tens_digit]
            
    
output = hundreds[hundreds_digits] + ' ' + tens[tens_digit] + ' ' + ones[ones_digit]


print(output)
    




























"""
Lab 4: Version 2
Handle numbers from 0-999.
"""
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
    20: 'twenty'
}

ones = {

    0: 'ten ',
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
numbers = int(input('Hello, please enter a numeber from 0-999 to convert to words: '))

hundreds_digits = numbers // 100
tens_digit = (numbers // 10) % 10
ones_digit = numbers % 10




if numbers >= 100 and tens_digit == 1: # This will diplay the hundreds with only seen dict being called on. 
    output = hundreds[hundreds_digits] + ' ' + teens[numbers % 100]
elif numbers >= 100 and ones_digit == 0 and tens_digit > 1: # this is to output anything that is 120, 130, 140 etc.
    output = hundreds[hundreds_digits] + ' ' + tens[tens_digit]
elif numbers >= 100 and ones_digit == 0: # This is to get the output for 100, 200, 300, etc.
    output = hundreds[hundreds_digits] 
elif numbers >= 100 and tens_digit == 0: # this is to get anything that is over 100 and is 101, 102, etc.
    output = hundreds[hundreds_digits] + ' ' + ones[ones_digit]
elif numbers >= 100:
   output = hundreds[hundreds_digits] + ' ' + tens[tens_digit] + ' ' + ones[ones_digit]
elif numbers >= 10 and numbers <= 20:
    output = teens[numbers % 100]
elif numbers > 20 and ones_digit == 0:
    output = tens[tens_digit] 
elif numbers > 20:
    output = tens[tens_digit] + ' ' + ones[ones_digit]
elif numbers < 10 and numbers >= 1:
    output = ones[ones_digit]
elif numbers == 0:
    output = 'zero'

print(f'The number: {numbers} in word form is {output.upper()}') # prints out the output of the if loop and will upper to make it easier to read. 





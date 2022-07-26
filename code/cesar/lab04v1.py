"""
Lab 4: Version 1 
Handle numbers from 0-99.

"""

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
numbers = int(input('Hello, please enter a numeber from 0-99 to convert to words: '))

tens_digit = (numbers // 10) % 10
ones_digit = numbers % 10


if numbers >= 100: # This will prompt user for numbers from 0-99 if it is more than 100 
    output = 'Please enter a valid number from 0-99'
elif numbers >= 10 and numbers <= 20: # This will handle the teens
    output = teens[numbers % 100]
elif numbers > 20 and ones_digit == 0: # this handles all the 20, 30, 40, etc.
    output = tens[tens_digit] 
elif numbers > 20:
    output = tens[tens_digit] + ' ' + ones[ones_digit]
elif numbers < 10 and numbers >= 1:
    output = ones[ones_digit]
elif numbers == 0: # This handles the 0s
    output = 'zero'
print(f'{output.upper()}')









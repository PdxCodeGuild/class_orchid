import string


print('Hello and Welcome!')

numbers = input('Please enter the numbers you would like converted: ')
 
x = int(numbers)

value_1 = tens_digit = x//10
                         # this  returns 6 7 in the terminal when printed
value_2 = ones_digit = x%10

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
     9 : 'nine'
}
ones = ones[value_2]

tens = tens [value_1]

print(f'Your conversion is: {tens}-{ones}')
ones_teens = {
    0: '',
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
teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirtheen',
    14: 'fourteen',
    15: 'fiftheen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}
twentys_ninety = {
    2: 'twenty ',
    3: 'thirty ',
    4: 'forty ',
    5: 'fifty ',
    6: 'sixty ',
    7: 'seventy ',
    8: 'eighty ',
    9: 'ninety ',
}

number = input('Enter your number here: ')
number = int(number)
tens_digit = number // 10  # input // 10 gets me the first 
ones_digit = number % 10
tens_word = ''
ones_word = ''
if number >= 20:
    tens_word = twentys_ninety[tens_digit]
    ones_word = ones_teens[ones_digit]
elif number >= 10:
    ones_word = teens[number]
elif number == 0:
    ones_word = 'Zero'
    
elif number < 10:
    ones_word = ones_teens[ones_digit]
    

print(f'Your number is {tens_word}{ones_word}')





# string concatenation
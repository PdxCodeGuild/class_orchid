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
    0: ' ',
    10: ' ten',
    11: ' eleven',
    12: ' twelve',
    13: ' thirteen',
    14: ' fourteen',
    15: ' fiftheen',
    16: ' sixteen',
    17: ' seventeen',
    18: ' eighteen',
    19: ' nineteen',
}
twentys_ninety = {
    0: ' ',
    2: ' twenty ',
    3: ' thirty ',
    4: ' forty ',
    5: ' fifty ',
    6: ' sixty ',
    7: ' seventy ',
    8: ' eighty ',
    9: ' ninety ',
}
hundreds = {
    1: 'one hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred',
    9: 'nine hundred',
}
"""
Is there anyway i can single out all the 100,200,300,400, etc. inputs so my program does not keep breaking because i have no idea 
how to make a 0 key for line 59 to pull from

"""
number = input('Enter your number here: ')
number = int(number)
tens_digit = number // 10 % 10  # input // 10 gets me the first number to work with but if the input is greater than 100 i need modelous to then make that input workable
ones_digit = number % 10 
hundreds_digit = number // 100 
hundreds_word = ''
tens_word = ''
ones_word = ''
# print(hundreds_digit, tens_digit, ones_digit) this is how I solved my KeyError issue, by finding out which keys I was actually calling on
if number >= 100 and tens_digit == 1:
    hundreds_word = hundreds[hundreds_digit]
    tens_word = teens[number % 100]
    # 115 .... 115 % 100 is 115 - 100 = 15

elif number >= 100:
    hundreds_word = hundreds[hundreds_digit]
    tens_word = twentys_ninety[tens_digit]
    ones_word = ones_teens[ones_digit]

elif number >= 20:
    tens_word = twentys_ninety[tens_digit]
    ones_word = ones_teens[ones_digit]
elif number >= 10:
    ones_word = teens[number]
elif number == 0:
    ones_word = 'Zero'
elif number < 10:
    ones_word = ones_teens[ones_digit]

print(ones_digit)

final = f"{number} is {hundreds_word}{tens_word}{ones_word}"
print(final)


# print(f'Your number is {tens_word}{ones_word}')





# string concatenation
# lists for translations
translate_ones = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', ]
translate_teens = [ 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', ]
translate_tens = [ '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', ]

# receive the input
num = input('Enter a number between 0 and 99: ')

# validate the input is an integer
try:
    num = int(num)
except ValueError:
    print('You must enter an be an integer. Exiting')
    quit()

# restrict the value to 0-99
if num >= 100 or num < 0:
    print('You must enter a value between 0 and 99. Exiting')
    quit()

# perform calculations
tens_digit = num//10
ones_digit = num%10

# apply appropriate translations for respective ranges
if num < 10:
    mystr = f'{translate_ones[ones_digit]}'
elif num < 20:
    mystr = f'{translate_teens[ones_digit]}'
elif ones_digit == 0:
    mystr = f'{translate_tens[tens_digit]}'
else:
    mystr = f'{translate_tens[tens_digit]}-{translate_ones[ones_digit]}'

# print the string
print(mystr)
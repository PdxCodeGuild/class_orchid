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
if num >= 1000 or num < 0:
    print('You must enter a value between 0 and 999. Exiting')
    quit()

# perform calculations
hundreds_digit = num//100
tens_digit = num//10%10
ones_digit = num%10

# initialize the string for concatenation
mystr = ''

# handle numbers >= 100 first
if num > 99:
    mystr += f'{translate_ones[hundreds_digit]} hundred and '

# update the value (I know this is lazy)
num = num - hundreds_digit * 100

# apply appropriate translations for respective ranges
if num < 10:
    mystr += f'{translate_ones[ones_digit]}'
elif num < 20:
    mystr += f'{translate_teens[ones_digit]}'
else:
    mystr += f'{translate_tens[tens_digit]}-{translate_ones[ones_digit]}'

# print the string
print(mystr)
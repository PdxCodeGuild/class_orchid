import re, sys

input_string = sys.argv[1]
while True:
    input_string = input_string or input('Enter the time [hh:mm]: ')
    if not re.match('^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', input_string):
        print('Invalid input.')
        input_string = ''
        continue
    else: break

# lists for translations (from version one)
translate_ones = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', ]
translate_teens = [ 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', ]
translate_tens = [ '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', ]

def myfun(num):
    # perform calculations (from version one)
    tens_digit = num//10
    ones_digit = num%10

    # apply appropriate translations for respective ranges (from version one)
    if num < 10:
        mystr = f'{translate_ones[ones_digit]}'
    elif num < 20:
        mystr = f'{translate_teens[ones_digit]}'
    elif ones_digit == 0:
        mystr = f'{translate_tens[tens_digit]}'
    else:
        mystr = f'{translate_tens[tens_digit]}-{translate_ones[ones_digit]}'
    
    return mystr

parts = (input_string.split(':'))
hour = int(parts[0])
mins = int(parts[1])
mystr = ''
suf = ''

hour_str = hour > 12 and hour % 12 or hour
if mins <= 1:
    mystr = f'{myfun(mins)} minute after {myfun(hour_str)}'
elif mins < 10:
    mystr = f'{myfun(mins)} minutes after {myfun(hour_str)}'

if hour == 0 and mins == 0:
    mystr += 'midnight'
    suf += 'on the dot'
elif hour == 0:
    suf += 'minutes after midnight'
elif hour < 12:
    suf += 'in the morning'
elif hour == 12 and mins == 0:
    mystr += 'noon'
    suf += 'on the dot'
elif hour < 16:
    suf = 'in the afternoon'
else:
    suf += 'in the evening'

mystr = mystr or myfun(hour_str) + ((myfun(hour_str) and myfun(mins)) and ' ') + myfun(mins)

print(f'It is {mystr} {suf}.')
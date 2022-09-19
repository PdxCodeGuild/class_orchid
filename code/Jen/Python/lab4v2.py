'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 4: Number to Phrase'''

from unicodedata import digit


ones = {
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

tens = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety',
    }

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'forteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'ninteen',
}

changingnums = {
}

phrases = {
}

digits = (input("Choose a number you would like to convert to a phrase. "))
digits = int(digits)

if digits == 0:
    print("zero")
    quit()

if digits > 999:
    print("You have chosen an invalid input, please select a number less than 1,000")
    quit()

hundreds_digit = digits//100
changingnums['hundreds_digit'] = hundreds_digit
runtot = digits - (hundreds_digit*100)
tens_digit = runtot//10
changingnums['tens_digit'] = tens_digit
ones_digit = digits%10
changingnums['ones_digit'] = ones_digit
teens_digit = str(tens_digit) + str(ones_digit)
teens_digit = int(teens_digit)
changingnums['teens_digit'] = teens_digit

print

if hundreds_digit == 00:
    phrases['hundred'] = ""

if teens_digit == 00:
    phrases['teen'] = ""

if changingnums.get('teens_digit') == 0:
    phrases['teen'] = ""

elif changingnums.get('teens_digit') in range(1,10):
    teens_phrase = ones.get(ones_digit)
    phrases['teen'] = teens_phrase
    
elif changingnums.get('teens_digit') in range(10, 20):
    teens_phrase = teens.get(teens_digit)
    phrases['teen'] = teens_phrase
    
elif changingnums.get('teens_digit') in range(20, 100):
    ten = changingnums.get('tens_digit')
    one = changingnums.get('ones_digit')
    if  one == 0:
        phrases['ones'] = ""
        teens_phrase = tens.get(tens_digit)
        phrases['teen'] = teens_phrase
    elif one > 0:
        hyphen = str("-")
        tens_digit = str(tens.get(tens_digit))
        ones_digit = str(ones.get(ones_digit))
        teens_phrase = tens_digit + hyphen + ones_digit
        phrases['teen'] = teens_phrase

if digits >99:
    phrases['hundred'] = ones.get(hundreds_digit) + " hundred"

print(f"{phrases.get('hundred')} {phrases.get('teen')}")

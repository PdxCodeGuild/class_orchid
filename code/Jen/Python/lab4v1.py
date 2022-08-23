'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 4: Number to Phrase'''

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
digits = int(input("Choose a number you would like to convert to a phrase. "))

if digits == 0:
    print("zero")
    quit()

if digits > 99:
    print("You have chosen an invalid iput, please choose a number below 100.")
    quit()

tens_digit = digits//10
ones_digit = digits%10


if digits in range(1,10): 
    print(ones[ones_digit])
elif tens_digit == 1:
    teens_digit = digits
    print(teens[teens_digit])
elif tens_digit > 1:
    if ones_digit == 0:
        tens_phrase = tens[tens_digit]
        print(tens_phrase)
    else:
        ones_phrase = ones[ones_digit]
        tens_phrase = tens[tens_digit]
        print(f"{tens_phrase}-{ones_phrase}")


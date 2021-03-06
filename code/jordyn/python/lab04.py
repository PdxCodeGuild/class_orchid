hundreds = {
    0:'',
    1:'onehundred',
    2:'twohundred',
    3:'threehundred',
    4:'fourhundred',
    5:'fivehundred',
    6:'sixhundred',
    7:'sevenhundred',
    8:'eighthundred',
    9:'ninehundred',
}

tens = {
    0:'',
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety'
}

ones = {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
}

teens = {
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'
}

print("Number To Phrase.")

phrase = int(input("Give me a number between 0 and 999\n>"))

phrase_hundreds = phrase // 100
phrase_tens = (phrase // 10) % 10
# print(phrase // 10) #testing math logic
# print(phrase_tens) #testing math logic
phrase_ones = phrase % 10

if phrase >= 10 and phrase <= 19:
    print(f"{phrase} is written as {teens[phrase]}.")

# elif phrase > 99 or phrase < 0:
#     print("Please be sure to use numbers between 1 and 99.")

elif phrase > 999 or phrase <0:
    print("Please be sure to use numbers between 0 and 999.")

elif phrase_ones == 0 and phrase_tens == 0 and phrase_hundreds == 0:
    print(f"{phrase} is written as zero.")

else:
    phrase_combine = ''
    if phrase_ones >= 1 and phrase_tens >= 1:
        phrase_combine = str(' ' + tens[phrase_tens] + '-' + ones[phrase_ones])
        # print('ones and tens') #testing math logic
    elif phrase_ones == 0:
        phrase_combine = str(' ' + tens[phrase_tens])
        # print('ones') #testing math logic
    elif phrase_tens == 0:
        phrase_combine = str(' ' + ones[phrase_ones])
        # print('tens') #testing math logic
    print(f"{phrase} is written as {hundreds[phrase_hundreds]}{phrase_combine}.")
    # print(phrase_combine) #testing output

# elif phrase_ones == 0 and phrase_tens == 0 and phrase_hundreds != 0:
#     print(f"{phrase} is written as {hundreds[phrase_hundreds]}.")

# elif phrase_ones == 0 and phrase_tens >= 1:
#     print(f"{phrase} is written as {tens[phrase_tens]}.")

# elif phrase_ones != 0:
#     print(f"{phrase} is written as {tens[phrase_tens]}-{ones[phrase_ones]}.")
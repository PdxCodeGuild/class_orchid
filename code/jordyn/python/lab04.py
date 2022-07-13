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

phrase = int(input("Give me a number between 1 and 99\n>"))

phrase_tens = phrase // 10
phrase_ones = phrase % 10

if phrase >= 10 and phrase <= 19:
    print(f"{phrase} is written as {teens[phrase]}.")

elif phrase > 99 or phrase < 1:
    print("Please be sure to use numbers between 1 and 99.")

elif phrase_ones == 0:
    print(f"{phrase} is written as {tens[phrase_tens]}.")

elif phrase_ones != 0:
    print(f"{phrase} is written as {tens[phrase_tens]}-{ones[phrase_ones]}.")


user_input = input("\nEnter a number between 0-99 ")





phrase = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sisteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "ninteen",
    

}

phrase_2 = {
    2 : "twenty",
    3: "thirty",
    4 : "fourty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninty",

}


phrase_3 = {
    1 : "one hundred",
    2 : "two hundred",
    3 : "three hundred",
    4 : "four hundred",
    5 : "five hundred",
    6 : "six hundred",
    7 : "seven hundred",
    8 : "eight hundred",
    9 : " nine hundred",
}



x = int(user_input)
#huns_digit = x//100
if x <= 99:
    tens_digit = x//10
    ones_digit = x%10
    print(tens_digit, ones_digit)
    print(phrase_2[tens_digit] + phrase[ones_digit])
if x >= 100:
    huns_digit = x//100 
    tens_digit = x//100
    ones_digit = x%10
    print(huns_digit, tens_digit, ones_digit)
    print(phrase_3[huns_digit] + phrase_2[tens_digit] + phrase[ones_digit])







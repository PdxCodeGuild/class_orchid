user_input = input("\nEnter a number between 0-99 ")


x = int(user_input)
tens_digit = x//10
ones_digit = x%10

print(tens_digit, ones_digit)


phrase = {
    0 : "zero",
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
    16 : "sixteen",
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
    9 : "ninty"

}




x = int(user_input)
if x <= 19:
    print(phrase[x])
if x in range(20, 100): #<= 99:
    huns_digit = x//100
    tens_digit = x//10
    ones_digit = x%10
    if ones_digit == 0:
        print(phrase_2[tens_digit])
    if ones_digit != 0:
        print(tens_digit, ones_digit)
        print(phrase_2[tens_digit] + phrase[ones_digit])
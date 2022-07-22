


user_input = input("\nEnter a number between 0-999 ")





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

phrase_4 = {
    1 : "and eleven",
    2 : "and twelve",
    3 : "and thirteen",
    4 : "and fourteen",
    5 : "and fifteen",
    6 : "and sixteen",
    7 : "and seventeen",
    8 : "and eighteen",
    9 : "and ninteen",
}

phrase_5 = {
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

phrase_6 = {
    0 : "ten",
    1 : "eleven",
    2 : "twelve",
    3 : "thirteen",
    4 : "fourteen",
    5 : "fifteen",
    6 : "sisteen",
    7 : "seventeen",
    8 : "eighteen",
    9 : "ninteen",
}

phrase_7 = {
    1 : "eleven"
}


x = int(user_input)
if x <= 19:
    print(phrase[x])

if x in range(20, 100):
    tens_digit = x//10
    ones_digit = x%10
    print(tens_digit, ones_digit)
    print(phrase_2[tens_digit] + phrase[ones_digit])


if x in range(100, 110):
    huns_digit = x//100
    tens_digit = (x%100)//10
    ones_digit = x%10
    if ones_digit == 0 and tens_digit ==0:
        print(phrase_3[huns_digit])
    if ones_digit != 0 and tens_digit == 0:
        print(huns_digit, tens_digit, ones_digit)
        print(phrase_3[huns_digit] + phrase[ones_digit])





if x in range(110, 112):
    huns_digit = x//100
    tens_digit = (x%100)//10
    print(huns_digit, tens_digit)
    print(phrase_3[huns_digit] + phrase_7[tens_digit])


if x in range(112, 1000): 
    huns_digit = x//100 
    tens_digit = (x%100)//10
    ones_digit = x%10
   
    print(huns_digit, tens_digit, ones_digit)
    if tens_digit == 1 and tens_digit != 0:
        print((phrase_3[huns_digit] + phrase_6[ones_digit]))
    if ones_digit == 0 and tens_digit != 1:
        print(phrase_3[huns_digit] + phrase_2[tens_digit])
    if ones_digit !=0 and tens_digit > 1:
        print(phrase_3[huns_digit] + phrase_2[tens_digit] + phrase[ones_digit])
    
    
    
    
    
    
   



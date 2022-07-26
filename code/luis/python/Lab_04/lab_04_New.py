## Author:Andrew Jaquez
## Fixed update from previous commit
numbers_in_english_ones = {
    0 : '',
    1: 'One',
    2 :'Two',
    3 :'Three',
    4 :'Four',
    5 :'Five',
    6 :'Six',
    7 :'Seven',
    8 :'Eight',
    9 :'Nine',
    10 : 'TenTen',
      11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'nineteen'
}
numbers_in_english_tens ={
     0 : '',
    10 : "Ten",
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'nineteen',
     2 : "Twenty",
     3 : "Thirty",
     4 : "Forty",
     5 : "Fifty",
     6 : "Sixty",
     7 : "Seventy",
     8 : "Eighty",
     9 : "Ninety"
}
number_in_english_hundreds ={
    1 : "One Hundred",
    2 : "Two Hundred",
    3 : "Three Hundred",
    4 : "Four Hundred",
    5 : "Five Hundred",
    6 : "Six Hundred",
    7 : "Seven Hundred",
    8 : "Eight Hundred",
    9 : "Nine Hundred"
}
x = int(input("Enter a three digit number, from 0-999: "))

if x <= 99 and x >= 20:
    ones = x%10
    tens = x//10
    print(x, 'is',numbers_in_english_tens[tens],numbers_in_english_ones[ones])
ones = x
if x <= 9 and x >= 1:
    print(x,'is',numbers_in_english_ones[ones])
hundred = 0
tens1 = 0
ones1 = 0
hunteen = 0
if x >= 100 and x <= 999:
    ones1 = x%10
    hundred = x//100
    hunteen = x%100
    tens1 += x//10%10
    output = number_in_english_hundreds[hundred]
    if hunteen >= 10 and hunteen <= 19:
        output += f' and {numbers_in_english_tens[hunteen]}'
    else:
        if tens1 > 1:
            output += f' and {numbers_in_english_tens[tens1]}'
        if ones1 > 0:
            output += numbers_in_english_ones[ones1]
    print(output)

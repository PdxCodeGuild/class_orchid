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
    if x >= 120:
        tens1 += x//10%10
if x >= 10 and x <= 19:
    print(x,'is',numbers_in_english_tens[x])
if x == 200:
    print(x,'is ',number_in_english_hundreds[hundred])
if x >= 201 or x <= 209:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_ones[ones])
if x == 300:
    print(x,'is ',number_in_english_hundreds[hundred])
if x == 400:
    print(x,'is ',number_in_english_hundreds[hundred])
if x == 500:
    print(x,'is ',number_in_english_hundreds[hundred])
if x == 600:
    print(x,'is ',number_in_english_hundreds[hundred])
if x == 700:
    print(x,'is ',number_in_english_hundreds[hundred])
if x == 800:
    print(x,'is ',number_in_english_hundreds[hundred])
if x == 900:
    print(x,'is ',number_in_english_hundreds[hundred])
if x >= 220 and x <=299:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 320 and x <= 399:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 420 and x <= 499:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 520 and x <= 599:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 620 and x <=699:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 720 and x <=799:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 820 and x <=899:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 920 and x <=999:
    print(x,'is',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[tens1],numbers_in_english_ones[ones1])
if x >= 110 and x <=119:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 210 and x <= 219:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 310 and x <= 319:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 410 and x <= 419:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 510 and x <= 519:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 610 and x <= 619:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 710 and x <= 719:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 810 and x <= 819:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
if x >= 910 and x <= 919:
        print(x,'is ',number_in_english_hundreds[hundred],'and',numbers_in_english_tens[hunteen])
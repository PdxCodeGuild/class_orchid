numbers_in_english_ones = {
    '0':'Zero',
    '1':'One',
    '2':'Two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
}
numbers_in_english_tens ={
    '10': "ten",
    '20': "twenty",
    "30": "Thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety"


}



x = int(input("Enter a two digit number, from 0-99: "))
tens_digit = x//10
ones_digit = x%10

if tens_digit == 0 and ones_digit == 0:
    print("Zero")
elif tens_digit == 0 and ones_digit == 1:
    print("One")
elif tens_digit == 0 and ones_digit == 2:
    print("Two")
elif tens_digit == 0 and ones_digit == 3:
    print("Three")
elif tens_digit == 0 and ones_digit == 4:
    print("four")
elif tens_digit == 0 and ones_digit == 5:
    print("Five")
elif tens_digit == 0 and ones_digit == 6:
    print("Six")
elif tens_digit == 0 and ones_digit == 7:
    print("Seven")
elif tens_digit == 0 and ones_digit == 8:
    print("Eight")
elif tens_digit == 0 and ones_digit == 9:
    print("Nine")
elif tens_digit == 1 and ones_digit == 0:
    print("ten")
elif tens_digit == 1 and ones_digit == 1:
    print("eleven")
elif tens_digit == 1 and ones_digit == 2:
    print("Twelve")
elif tens_digit == 1 and ones_digit == 3:
    print("Thirteen")
elif tens_digit == 1 and ones_digit == 4:
    print("Fourteen")
elif tens_digit == 1 and ones_digit == 5:
    print("Fifteen")
elif tens_digit == 1 and ones_digit == 6:
    print("Sixteen")
elif tens_digit == 1 and ones_digit == 7:
    print("Seventeen")
elif tens_digit == 1 and ones_digit == 8:
    print("Eighteen")
elif tens_digit == 1 and ones_digit == 9:
    print("Nineteen")
elif tens_digit == 2 and ones_digit == 0:
    print(numbers_in_english_tens["20"])
elif tens_digit == 2 and ones_digit == 1:
    print(numbers_in_english_tens["20"],"-",numbers_in_english_ones['1'])
elif tens_digit == 2 and ones_digit == 2:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["2"])
elif tens_digit == 2 and ones_digit == 3:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["3"])
elif tens_digit == 2 and ones_digit == 4:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["4"])
elif tens_digit == 2 and ones_digit == 5:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["5"])
elif tens_digit == 2 and ones_digit == 6:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["6"])
elif tens_digit == 2 and ones_digit == 7:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["7"])
elif tens_digit == 2 and ones_digit == 8:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["8"])
elif tens_digit == 2 and ones_digit == 9:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["9"])
elif tens_digit == 3 and ones_digit == 10:
    print(numbers_in_english_tens["30"],)
elif tens_digit == 3 and ones_digit == 1:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["1"])
elif tens_digit == 3 and ones_digit == 2:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["2"])
elif tens_digit == 3 and ones_digit == 3:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["3"])
elif tens_digit == 3 and ones_digit == 4:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["4"])
elif tens_digit == 3 and ones_digit == 5:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["5"])
elif tens_digit == 3 and ones_digit == 6:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["6"])
elif tens_digit == 3 and ones_digit == 7:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["7"])
elif tens_digit == 3 and ones_digit == 8:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["8"])
elif tens_digit == 3 and ones_digit == 9:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["9"])
elif tens_digit == 4 and ones_digit == 0:
    print(numbers_in_english_tens["40"])
elif tens_digit == 4 and ones_digit == 1:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["1"])
elif tens_digit == 4 and ones_digit == 2:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["2"])
elif tens_digit == 4 and ones_digit == 3:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["3"])
elif tens_digit == 4 and ones_digit == 4:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["4"])
elif tens_digit == 4 and ones_digit == 5:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["5"])
elif tens_digit == 4 and ones_digit == 6:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["6"])
elif tens_digit == 4 and ones_digit == 7:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["7"])
elif tens_digit == 4 and ones_digit == 8:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["8"])
elif tens_digit == 4 and ones_digit == 9:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["9"])
elif tens_digit == 5 and ones_digit == 0:
    print(numbers_in_english_tens["50"])
elif tens_digit == 5 and ones_digit == 1:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["1"])
elif tens_digit == 5 and ones_digit == 2:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["2"])
elif tens_digit == 5 and ones_digit == 3:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["3"])
elif tens_digit == 5 and ones_digit == 4:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["4"])
elif tens_digit == 5 and ones_digit == 5:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["5"])
elif tens_digit == 5 and ones_digit == 6:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["6"])
elif tens_digit == 5 and ones_digit == 7:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["7"])
elif tens_digit == 5 and ones_digit == 8:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["8"])
elif tens_digit == 5 and ones_digit == 9:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["9"])
elif tens_digit == 6 and ones_digit == 0:
    print(numbers_in_english_tens["60"])
elif tens_digit == 6 and ones_digit == 1:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["1"])
elif tens_digit == 6 and ones_digit == 2:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["2"])
elif tens_digit == 6 and ones_digit == 3:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["3"])
elif tens_digit == 6 and ones_digit == 4:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["4"])
elif tens_digit == 6 and ones_digit == 5:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["5"])
elif tens_digit == 6 and ones_digit == 6:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["6"])
elif tens_digit == 6 and ones_digit == 7:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["7"])
elif tens_digit == 6 and ones_digit == 8:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["8"])
elif tens_digit == 6 and ones_digit == 9:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["9"])
elif tens_digit == 7 and ones_digit == 0:
    print(numbers_in_english_tens["70"])
elif tens_digit == 7 and ones_digit == 1:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["1"])
elif tens_digit == 7 and ones_digit == 2:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["2"])
elif tens_digit == 7 and ones_digit == 3:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["3"])
elif tens_digit == 7 and ones_digit == 4:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["4"])
elif tens_digit == 7 and ones_digit == 5:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["5"])
elif tens_digit == 7 and ones_digit == 6:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["6"])
elif tens_digit == 7 and ones_digit == 7:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["7"])
elif tens_digit == 7 and ones_digit == 8:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["8"])
elif tens_digit == 7 and ones_digit == 9:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["9"])
elif tens_digit == 8 and ones_digit == 0:
    print(numbers_in_english_tens["80"])
elif tens_digit == 8 and ones_digit == 1:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["1"])
elif tens_digit == 8 and ones_digit == 2:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["2"])
elif tens_digit == 8 and ones_digit == 3:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["3"])
elif tens_digit == 8 and ones_digit == 4:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["4"])
elif tens_digit == 8 and ones_digit == 5:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["5"])
elif tens_digit == 8 and ones_digit == 6:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["6"])
elif tens_digit == 8 and ones_digit == 7:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["7"])
elif tens_digit == 8 and ones_digit == 8:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["8"])
elif tens_digit == 8 and ones_digit == 9:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["9"])
elif tens_digit == 9 and ones_digit == 0:
    print(numbers_in_english_tens["90"])
elif tens_digit == 9 and ones_digit == 1:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["1"])
elif tens_digit == 9 and ones_digit == 2:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["2"])
elif tens_digit == 9 and ones_digit == 3:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["3"])
elif tens_digit == 9 and ones_digit == 4:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["4"])
elif tens_digit == 9 and ones_digit == 5:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["5"])
elif tens_digit == 9 and ones_digit == 6:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["6"])
elif tens_digit == 9 and ones_digit == 7:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["7"])
elif tens_digit == 9 and ones_digit == 8:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["8"])
elif tens_digit == 9 and ones_digit == 9:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["9"])

print(x)

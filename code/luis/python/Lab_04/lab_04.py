numbers_in_english_ones = {
    'zero': 0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}
numbers_in_english_tens ={
    "ten": 10,
    "twenty": 20,
    "Thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty":80,
    "ninety": 90,


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
elif tens_digit == 0 and ones_digit== 8:
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
    print(numbers_in_english_tens(20))

elif tens_digit == 4 and ones_digit == 0:
    print("Forty")

print(x)

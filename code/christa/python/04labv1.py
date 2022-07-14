#Number to Phrase Version1
#Create a dictionary for digits one through nineteen
digits = {'small_digits':
    {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    },

    'large_digits': {
    2: 'twenty', 3: 'thrity', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety',
    }
}
#create a dictionary for "big" digits ascending by 10's
#big_digits = {20: 'twenty', 30: 'thrity', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',}
#Ask the user to impute a number
number = input("Please enter a number ranging from 0 to 99: ")
#identify the value as an integer
number = int(number)
#break the number down into 10's and 1's to define 
tens_digit = number//10
ones_digit = number%10
#pull tens digit from big_digits dictionary
if tens_digit == 1:
    tens_answer = digits['small_digits'][number]
elif tens_digit > 1:
    tens_answer = digits['large_digits'][tens_digit]
if ones_digit >= 1 and tens_digit != 1:
    ones_answer = "-" + digits['small_digits'][ones_digit]
elif ones_digit == 0 and tens_digit == 0:
    ones_answer = digits['small_digits'][ones_digit]
    tens_answer = ""
else:
    ones_answer = ""
#pull ones digit from small_digits dictionary    
#print message 
print(f"{tens_answer}{ones_answer}")

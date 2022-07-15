#Number to Phrase Version1
#Create a dictionary for digits one through nineteen
digits = {'one':
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
    }, 
    
    'teens':
        {10: 'ten',
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

    'ten': {
    0: 'zero', 2: 'twenty', 3: 'thrity', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety',
    },
    
}
#create a dictionary for "big" digits ascending by 10's
#Ask the user for number
number = input("Please enter a number ranging from 0 to 99: ")
#identify the value as an integer
number = int(number)
#break the number down into 10's and 1's to define 
tens_digit = number//10
ones_digit =number%10

if tens_digit > 1 and number > 19:
    tens_answer = digits['ten'][tens_digit] + " "
if number >= 10 and number <=19:          #Added to V2 for teen digits
    tens_answer = digits['teens'][number] 
elif tens_digit == 0:
    tens_answer = ""

if ones_digit >= 1 and tens_digit != 1:                #pull ones digit from ones dictionary 
    ones_answer = " " + digits['one'][ones_digit]
elif ones_digit == 0 and tens_digit == 0:
    ones_answer = ""   #digits['one'][ones_digit]
    tens_answer = ""
else:
    ones_answer = ""
if number == 0:
   ones_answer = digits['one'][number]

   
#print message 
print(f"{tens_answer}{ones_answer}")
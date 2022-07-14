#Number to Phrase Version2
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
        9: 'nine',},

        'teens': {    #separated teens dictionary for V2
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

    'ten': {
    0: 'zero', 2: 'twenty', 3: 'thrity', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety',
    },
    
    'hundred': {
        1: 'one - hundred', 2: 'two - hundred', 3: 'three - hundred', 4: 'four - hundred', 5: 'five - hundred',
        6: 'six - hundred', 7: 'seven - hundred', 8: 'eight - hundred', 9: 'nine - hundred'
    },
}
#create a dictionary for "big" digits ascending by 10's
#big_digits = {20: 'twenty', 30: 'thrity', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',}
#Ask the user for number
number = input("Please enter a number ranging from 0 to 99: ")
#identify the value as an integer
number = int(number)
#break the number down into 10's and 1's to define 
hundreds_digit = number//100
tens_leftover = number%100
tens_digit = tens_leftover//10
teen_digit = tens_leftover         #added to account for teens
ones_digit = tens_leftover%10
#tens_digit = number//10
#ones_digit = number%10
#print(hundreds_digit)
#print(tens_digit)
#print(ones_digit)
#print(tens_leftover)

#pull hundreds digit from hundreds dictionary
if hundreds_digit >= 1:
    hundreds_answer = digits['hundred'][hundreds_digit] + " " + "-" + " "
elif hundreds_digit < 1:
    hundreds_answer = ""

#if tens_digit == 1:                                    #pull tens digit from tens dictionary -- NOT NEEDED FROM V1
#    tens_answer = digits['one'][tens_digit] 

if tens_digit > 1 and tens_leftover > 19:
    tens_answer = digits['ten'][tens_digit] + " "
if tens_leftover >= 10 and tens_leftover <=19:          #Added to V2 for teen digits
    tens_answer = digits['teens'][teen_digit] 
elif tens_digit == 0:
    tens_answer = ""

if ones_digit >= 1 and tens_digit != 1:                #pull ones digit from ones dictionary 
    ones_answer = " " + digits['one'][ones_digit]
elif ones_digit == 0 and tens_digit == 0:
    ones_answer = digits['one'][ones_digit]
    tens_answer = ""
else:
    ones_answer = ""
   
#print message 
print(f"{hundreds_answer}{tens_answer}{ones_answer}")


##Note to self -- need to figure out teens incorporation...
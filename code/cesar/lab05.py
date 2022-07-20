import string
import random

# dict with keys as the cards and values as their numerical value
deck = {
    "0": 0,
    "A": 11,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
# Welcome with instructions

print(f'''
Welcome! You will be prompted to enter the value of three
different cards in your hand. Please only enter the following:

A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, K, Q

Good Luck!
''')



"""
user will input the cards and they will be assiged to variable card_1-3. 
.upper()is used to account for users entering a lower case letter value.
"""
card_1 = input('What is your first card? ').upper()
card_2 = input('What is your second card? ').upper()
card_3 = input('What is your third card? ').upper()


"""
Worked with Danny Burrow (Instructor at pdx) to come up with a better way to run a check 
if the value that was input into the variable is already an int. If not it will return
and typecast it and will typecast to int. Originally I had all the numbers from
1-9 as keys int he dictionary with their int value in the value section. 
"""

def get_card_value(card): 
    if deck.get(card) == None:
        return int(card)
    else:
        return deck.get(card)
        
    

# add the total for the cards calling on the dictionaries keys and using the .upper() incase user types in a lower case letter

total = get_card_value(card_1.upper()) +  get_card_value(card_2.upper()) +  get_card_value(card_3.upper())
output = None

"""
Worked with Danny (instuctor) on Version 2 of this lab which checks to see
if there are any aces and if the total is more than 21 it will subract 10 
to account for aces being either 1 or 11. This is done with the while loop.
"""
while output is None:
    print(total)
    if total > 21:
        if card_1 == 'A' or card_2 == 'A' or card_3 == 'A':
            total -= 10
            continue
        output = '\nAlready busted!'

    if total < 17:
        output = '\nHit!'

    elif total >= 17 and total < 21:
        output = '\nStay!'

    elif total == 21:
        output = '\nBlackjack!'




print(f'''
 
Your total was: {total}
{output}
 
''')


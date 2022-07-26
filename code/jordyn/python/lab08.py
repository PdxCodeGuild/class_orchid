def list_conversion(input): #converts a string into a list
    credit_card = []
    for value in input:
        credit_card.append(int(value))
    return credit_card

def double(credit_card): #doubles every other value starting with the first
    for index,value in enumerate(credit_card):
        if index % 2 == False:
            value *= 2
            credit_card[index] = value
    return credit_card

def subtracter(credit_card): #subtracts 9 from all values above 9
    for index,value in enumerate(credit_card):
        if value > 9:
            value -= 9
            credit_card[index] = value
    return credit_card

def adder(credit_card): #converts a list of numbers into a single combined value
    total = 0
    for value in credit_card:
        total += value
    return str(total)

def check_val(card_sum,check): #checks 2 numbers and returns True/False if same/not same
    if int(card_sum) == int(check):
        return True
    else:
        return False

'''Credit Card Validation'''

print("Please enter your 16 digit card number.")
credit_string = str(input("> "))

credit_card = list_conversion(credit_string) #converts submitted string into a list
check_digit = credit_card.pop(-1) #removes the check number at end from list saves the value for later
credit_card.reverse() #reverses order
credit_card = double(credit_card) #doubles everyother number, starting with the first
credit_card = subtracter(credit_card) #subtracts from all values > 9
card_sum = adder(credit_card) #adds all values in the list into a single number and converts to string
card_sum = card_sum[-1] #removes all numbers except the final one for validation checking

validation = check_val(card_sum,check_digit) #checks the validity of the card after all other steps have been completed

if validation == True:
    print("Your card is Valid!")
elif validation == False:
    print("The card submitted is not valid.")
#Blackjack Version 1
#Card Dictionary
cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}
#Ask user for three card inputs
card_1= input("What's your first card? ")
card_2 = input("What is your second card? ")
card_3 = input("What is your third card? ")
#take the user input and pull integer from dictionary
value_1 = cards[card_1]
value_2 = cards[card_2]
value_3 = cards[card_3]
#total the integers
total_v = value_1 + value_2 + value_3
#provide conditions for advising
if total_v < 17:
    mesaage = (f'{total_v} "Hit"')
elif total_v >= 17 and total_v < 21:
    message = (f'{total_v} "Stay')
elif total_v == 21:
    message = (f'{total_v} "Blackjack!"')
else:
    message = (f'{total_v} "Already Busted"')
#print message
print(message)

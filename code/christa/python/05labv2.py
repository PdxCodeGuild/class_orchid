#Blackjack Version 1

cards = { 
    'option_1': 
    {
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
    },
    'option_2': {'A': 11,}
}

card_1 = input("What's your first card? ")
card_2 = input("What is your second card? ")
card_3 = input("What is your third card? ")

value_1 = cards['option_1'][card_1]
value_2 = cards['option_1'][card_2]
value_3 = cards['option_1'][card_3]

total_v = value_1 + value_2 + value_3

"""hand = []
count = 0

hand.append(value)"""




if total_v < 17:
    mesaage = (f'{total_v} "Hit"')
elif total_v >= 17 and total_v < 21:
    message = (f'{total_v} "Stay')
elif total_v == 21:
    message = (f'{total_v} "Blackjack!"')
else:
    message = (f'{total_v} "Already Busted"')

print(message)

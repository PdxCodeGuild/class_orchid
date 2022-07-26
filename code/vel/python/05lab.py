cards = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    
}

number_words = [
    'first',
    'second',
    'third',
]
user_cards = []
sum_of_cards = 0

for word in number_words:             # making a for loop to clean up my repeat variables 
    key = input(f'\nWhat is your {word} card?: ')
    while cards.get(key) is None:           # Trying to find a way to make an input that isn't in the 'cards' dict an 'Invalid entry'
        print('Invalid entry')
        key = input(f'\nWhat is your {word} card?: ')
    user_cards.append(key)
    sum_of_cards += cards[key]

    
if sum_of_cards < 17: 
    print('Hit!')

elif sum_of_cards >= 17 and sum_of_cards < 21:
    print('Stay')

elif sum_of_cards == 21:
    print('BLACKJACK BABY!')

else:
    print('Already busted')




fcard = input('Please enter your first card selection: ')

scard = input('Please enter your second card selection: ')

tcard = input('Please enter your third card selection: ')

info = {
    'a': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'q': 10,
    'k': 10
}

#info[fcard]
selection = info[fcard] + info[scard] + info[tcard]


if selection < 17:
    print('Hit!')

elif selection >= 17 and selection < 21:
    print('Stay.')

elif selection == 21:
    print('Blackjack!')

elif selection > 21:
    print('Already busted.')
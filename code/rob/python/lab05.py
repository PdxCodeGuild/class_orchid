options = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
}

check_options = list(options.keys())


first_card = input('\nWhat\'s your first card? ').upper()
second_card = input('What\'s your second card? ').upper()
third_card = input('What\'s your third card? ').upper()

while True:
    
    if first_card in check_options:
        
        if second_card in check_options:
            
            if third_card in check_options:
                print(f'\nCards: {first_card}, {second_card}, {third_card}')
                break
            else:
                print(f'\nThird card \'{third_card}\' is not valid, re-enter third card: ', end='')
                third_card = input()
        else:
            print(f'\nSecond card \'{second_card}\' is not valid, re-enter second card: ', end='')
            second_card = input()
    else:
        print(f'\nFirst card \'{first_card}\' is not valid, re-enter first card: ', end='')
        first_card = input()

total = options[first_card] + options[second_card] + options[third_card]

def get_cards(card_one, card_two, card_three):
    not_ace = []
    if card_one != 'A':
        not_ace.append(True)
        not_ace.append(card_one)
    if card_two != 'A':
        if len(not_ace) == 0:
            not_ace.append(True)
        not_ace.append(card_two)
    if card_three != 'A':
        if len(not_ace) == 0:
            not_ace.append(True)
        not_ace.append(card_three)
    return not_ace

def handle_ace(cards):
    total = []
    if len(cards) != 0:
        total.append(True)
        total.append(options[cards[1]] + options[cards[2]])
    else:
        total.append(False)
        
    return total
count = 0
if first_card == 'A' or second_card == 'A' or third_card == 'A':
    check = handle_ace(get_cards(first_card, second_card, third_card))
    if check[0] == True and check[1] < 11:
        total += 10

print(f'Total: {total}')

if total < 17:
    print('Move: Hit\n')
elif total >= 17 and total < 21:
    print('Move: Stay\n')
elif total == 21:
    print('Blackjack!\n')
elif total > 21:
    print('Already Busted\n')

# Accepted input
accepted = [ 'a', 'j', 'q', 'k', '2', '3', '4', '5', '6', '7', '8', '9', '10' ]

# Translation values for face card names and loop iterations
translations = { 'a': 1, 'j': 10, 'q': 10, 'k': 10, }

def translate(val):
    '''Translate user input.'''
    try:
        val = int(val)
    except ValueError:
        val = translations[val]
    return val

# initialize total
total = 0
aces = 0

# Input three cards
while True:
    val = input(f'Enter which card you drew: ').lower()
    if val in accepted:
        if val == 'a': aces += 1
        val = translate(val)
        total += val
        if total == 21 or total + aces * 10 == 21 or total + (aces - 1) * 10 == 21:
            print(f'{total} Blackjack!')
            break
        if total < 7:
            print(f'{total} Hit')
        elif total >= 7 and total < 21:
            print(f'{total} Stay')
        elif total > 21 :
            print(f'{total} Busted!')
            break
    else:
        print('Accepted values: a, j, q, k, [2-10]')

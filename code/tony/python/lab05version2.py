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
score = 0 # running score
aces = 0 # running total of aces dealt
blackjack = False # running blackjack status

# input each card
while True:
    val = input(f'Enter which card you drew: ').lower()
    if val in accepted:
        if val == 'a': aces += 1
        val = translate(val)
        score += val
        for i in range(1,aces):
            if blackjack: break
            # consider each ace dealt, valued at both 1 and 11
            blackjack = score + (aces - i) * 10 == 21
        blackjack = blackjack or score == 21
        if blackjack:
            print('Blackjack!')
            break
        if score < 17:
            print('Hit')
        elif score < 21:
            print('Stay')
        elif score > 21 :
            print('Busted!')
            break
    else:
        print('Accepted values: a, j, q, k, [2-10]')

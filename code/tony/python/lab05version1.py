# Accepted input
accepted = [ 'a', 'j', 'q', 'k', '2', '3', '4', '5', '6', '7', '8', '9', '10' ]

# Translation values for face card names and loop iterations
values = { 'a': 1, 'j': 10, 'q': 10, 'k': 10, }
iteration_string = ['first','second','third']

# Initialize values
total = 0
i = 0

# Input three cards
while i < 3:
    val = input(f'What\'s your {iteration_string[i]} card? ').lower()
    if not val in accepted:
        print('Accepted values: a, j, q, k, [2-10]')
        continue
    if val in values.keys():
        val = values.get(val)
    i += 1
    total += int(val)

# Give blackjack advice
if total < 17:
    print(f'{total} Hit')
elif total >= 17 and total < 21:
    print(f'{total} Stay')
elif total == 21:
    print(f'{total} Blackjack!')
elif total > 21:
    print(f'{total} Already Busted!')
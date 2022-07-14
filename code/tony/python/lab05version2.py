# Accepted input
accepted = [ 'a', 'j', 'q', 'k', '2', '3', '4', '5', '6', '7', '8', '9', '10' ]

# Translation values for face card names and loop iterations
values = { 'a': 11, 'j': 10, 'q': 10, 'k': 10, }
iteration_string = ['first','second','third']

# Initialize values
totals = [0]
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
    totals[0] += int(val)
    if val == 11 and len(totals) < 2:
        totals.append(totals[0])
    if val == 11:
        totals[1] += 1

# Give blackjack advice
for total in totals:
    if total < 17:
        print(f'{total} Hit')
    elif total >= 17 and total < 21:
        print(f'{total} Stay')
    elif total == 21:
        print(f'{total} Blackjack!')
    elif total > 21:
        print(f'{total} Already Busted!')
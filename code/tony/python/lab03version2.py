coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1),
]

# accept user input
dollars = float(input('Enter a dollar amount: '))

# multiply by 100 to avoid float precision problem
dollars = int(dollars * 100)

str = ''
for key, value in coins:
    amt = dollars // value
    dollars = dollars - amt * value
    str += f'{amt} {key}(s), '

print(str)

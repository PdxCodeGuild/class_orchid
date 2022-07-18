

#  VERSION 2

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('twen', 20),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]


def make_ch(total):
    output = ''
    for coin in coins:
        count = total // coin[1] 
        total -= (coin[1] * count)
        if count > 0:
           
            output += f'{count} {coin[0]}, '
    return output
    



amount = []

# total = input('\nEnter a dollar amount here: ')
total = float(input('\nEnter a dollar amount here: ')) * 100


    
print(make_ch(total))


 




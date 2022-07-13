# Lab 3: Make Change 


def make_ch(total, coins):
    output = ''
    for coin in coins:
        count = total // coin[1] 
        total = total - (coin[1] * count)
        if count > 0:
           
            output += f'{count} {coin[0]}, '
    return output
    
# at this point i need to make 



coins = [
    ('half-dollar', .50),
    ('quarter', .25),
    ('twen', .20),
    ('dime', .10),
    ('nickel', .5),
    ('penny', .1)
]
amount = []

# total = input('\nEnter a dollar amount here: ')
total = float(input('\nEnter a dollar amount here: '))

    
print(make_ch(total, coins))


# for item in coins:
    # print(item[1])

# print(coins[0][1])
 




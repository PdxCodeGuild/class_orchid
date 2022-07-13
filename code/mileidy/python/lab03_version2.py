
converter ={
    'pennies': 100
}

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

dollar_amount = input('Please enter the total dollar amount: ')

dollar_amount = int(dollar_amount)

f_conversion = dollar_amount * converter['pennies'] 

s_conversion = f_conversion // coins



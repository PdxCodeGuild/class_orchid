# Lab 3: Make Change 
# VERSION 1




coins = {
    "quarter": 25,
    "dime": 10,
    "nickel": 5,
    "penny": 1,

}
# lets turn 1.36 into a whole number to begin the op
# dollar_value = 1.36

total = float(input('\nEnter a dollar amount: '))
dollar_value_in_pennies = total * 100
output = ''
for coin in coins:
    count = dollar_value_in_pennies // coins[coin] # what can I do to make the input floor divived 
    dollar_value_in_pennies -= (coins[coin] * count)
    if count > 0:
        output += f'{count} {coin}, '
print(output) 




# print(coins['dime']) # = 10
# coin = 'dime'
# print(coins[coin]) # which is the same as line 30, because coin = 'dime' 








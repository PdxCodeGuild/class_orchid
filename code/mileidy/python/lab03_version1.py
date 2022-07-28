dollar_amount = input('Please enter the total dollar amount: ')

dollar_amount = float(dollar_amount)

quarters = dollar_amount // 0.25
#print(quarters)

dollar_amount -= quarters * .25 
#print(dollar_amount)

dimes = dollar_amount // 0.10

dollar_amount -= dimes * 0.10

nickles = dollar_amount // 0.05

dollar_amount -= nickles * 0.05

pennies = dollar_amount // 0.01

dollar_amount -= pennies * 0.01

print(f'{quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies.')
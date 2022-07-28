total = input('\nEnter a dollar amount: ')
pennies = ''

for index in total:
    if index != '.':
        pennies += index

pennies = int(pennies)

quaters = pennies // 25
dimes = (pennies - (quaters * 25)) //  10
nickels = (pennies - ((quaters * 25) + (dimes * 10))) // 5
pennies = (pennies - ((quaters * 25) + (dimes * 10) + (nickels * 5))) // 1

if quaters > 1 and quaters != 0:
    print(f'{quaters} quarters', end='')
elif quaters == 1:
    print(f'{quaters} quarter', end='')
if dimes > 1 and dimes != 0:
    print(f', {dimes} dimes', end='')
elif dimes == 1:
    print(f', {dimes} dime', end='')
if nickels > 1 and nickels != 0:
    print(f', {nickels} nickels', end='')
elif nickels == 1:
    print(f', {nickels} nickel', end='')
if pennies != 0 and pennies > 1:
    print(f', and {pennies} pennies', end='')
elif pennies == 1:
    print(f', and {pennies} penny', end='')

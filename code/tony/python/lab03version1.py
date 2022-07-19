# accept user input
dollars = float(input('Enter a dollar amount: '))

# multiply by 100 to avoid float precision problem
dollars = int(dollars * 100)

# calculate quarters and update remaining
quarters = dollars // 25
dollars = dollars - quarters * 25

# calculate dimes and update remaining
dimes = dollars // 10
dollars = dollars - dimes * 10

# calculate nickels and pennies
nickels = dollars // 5
pennies = dollars - nickels * 5

print(f'{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies')
'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 3: Make Change'''

amount = input("Enter a dollar amount. $")
amount = float(amount)
amtpennies = amount * 100

quarters = amtpennies // 25

runningtotal = (amtpennies - (quarters * 25))

dimes = runningtotal // 10

runningtotal = (runningtotal - (dimes * 10))

nickles = runningtotal // 5

runningtotal = (runningtotal - (nickles * 5))

pennies = runningtotal

print(f"{int(quarters)} quarters, {int(dimes)} dimes, {int(nickles)} nickles, {int(pennies)} pennies.")
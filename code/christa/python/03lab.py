#Version1 Lab03
#Version2 added the tuple however did not use in lab
"""coins = [
('half-dollar', 50)
('quarter', 25), 
('dime', 10),
('nickel', 5),
('penny', 1)
]"""
#coin names and their amounts
quarter = 25
dime = 10
nickel = 5
penny = 1

#defining the variable to be converted
x = input("Enter a dollar amount: ")
x = float(x)
#formula to calculate variable to convertable amount
y = x*100

#separate equations to using floor division // and modulus % to convert dollar *100 to coins
#if y >= 25:
quarters = y//quarter
d = y%quarter
dimes = d//dime
n = d%dime
nickels = n//nickel
p = n%nickel
pennies = p//penny
message = (f'There are {quarters} quarters, {dimes} dimes, {nickels}, nickels, and {pennies} pennies')

print(message)






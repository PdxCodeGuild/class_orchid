
user_input = float(input('Enter a dollar amount: ')) # Takes in an input with variable 

value_in_pennies = user_input * 100 # breaks the input to pennies and renames it 

# if, elif, else loops to determind what code block the values in pennies will run. 

if value_in_pennies >= 25: # if the value is greater than or equal to .25 (in this case 25 considering it in pennies)

    num_quarter = value_in_pennies // 25
    value_in_pennies -= (num_quarter * 25)

    num_dime = value_in_pennies // 10
    value_in_pennies -= (num_dime * 10)

    num_nickle = value_in_pennies // 5
    value_in_pennies -= (num_nickle * 5)

    num_penny = value_in_pennies // 1

    print(f'''

    {num_quarter} quarters
    {num_dime} dimes
    {num_nickle} nickles
    {num_penny} pennies

    ''')

elif value_in_pennies >= 10:

    num_dime = value_in_pennies // 10
    value_in_pennies -= (num_dime * 10)

    num_nickle = value_in_pennies // 5
    value_in_pennies -= (num_nickle * 5)

    num_penny = value_in_pennies // 1
    
    print(f'''

    {num_dime} dimes
    {num_nickle} nickles
    {num_penny} pennies

    ''')

elif value_in_pennies >= 5:

    num_nickle = value_in_pennies // 5
    value_in_pennies -= (num_nickle * 5)
    
    print(f'''

    {num_nickle} nickles
    
    ''')

elif value_in_pennies >= 1:

    num_penny = value_in_pennies // 1
    print(f'''
    
    {num_penny} pennies

    ''')
    
else:
     print('goodbye')













#Ask the user to input a dollar amount they will be broken down into change
amount_entered = input("\nPlease enter a dollar amount: ")

#convert the amount entered as a string into a float number
amount_in_pennies = float(amount_entered)


#complete floor division to find out how many quaters make up the amount
quaters = amount_in_pennies // .25
#convert float into integer
quaters = int(quaters)
#Get the amount the quaters make up so we can remove that amount from the amount entered by the user
quaters_value = quaters * .25
#Remove the quater value amount from the whole number
amount_in_pennies -= quaters_value


#complete floor division to find out how many dimes make up the amount
dimes = amount_in_pennies // .10
#convert float into integer
dimes = int(dimes)
#Get the amount the dimes make up so we can remove that amount from the amount entered by the user
dimes_value = dimes * .10
#Remove the dimes value amount from the whole number
amount_in_pennies -= dimes_value


#complete floor division to find out how many nickels make up the amount
nickels = amount_in_pennies // .05
#convert float into integer
nickels = int(nickels)
#Get the amount the nickels make up so we can remove that amount from the amount entered by the user
nickels_value = nickels * .05
#Remove the nickel value amount from the whole number
amount_in_pennies -= nickels_value


#complete floor division to find out how many pennies make up the amount
pennies = amount_in_pennies // .01
#convert float into integer
pennies = int(pennies)
#Get the amount the pennies make up so we can remove that amount from the amount entered by the user
pennies_value = pennies * .01
#Remove the pennies value amount from the whole number
amount_in_pennies -= pennies_value


# print out the final amounts of quaters, dimes, nickels and pennies that make up the change in the users input
print(f"{quaters} Quaters, {dimes} Dimes, {nickels} Nickels, {pennies} Pennies")
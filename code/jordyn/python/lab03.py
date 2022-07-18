quarter = 25 #penny values
dime = 10
nickel = 5
penny = 1

print("How much money do you have?")

change = float(input("$")) * 100 #converts to floor divisible value

change_q = change // quarter #quantity of quarters
change_q_r = change % quarter #remainder of change, 'r' is remainder

change_d = change_q_r // dime #quantity of dimes
change_d_r = change_q_r % dime #remainder of change

change_n = change_d_r // nickel #quantity of nickels
change_n_r = change_d_r % nickel #remainder of change

change_p = change_n_r // penny #redundant oh well, will always equal the value of change_n_r


print(f'From ${change / 100}, you have {int(change_q)} quarters, {int(change_d)} dime, {int(change_n)} nickels, and {int(change_p)} pennies.')
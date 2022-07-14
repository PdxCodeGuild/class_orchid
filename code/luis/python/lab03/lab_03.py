number_of_quarte = 0
number_of_dimes = 0
number_of_nickles = 0
number_of_penny = 0 
number_half_dollar = 0
total_in_pennies = 0

total_amount = input("Enter a dollar amount: ")
total_in_pennies = float(total_amount) / 0.01

if total_in_pennies >= 50:
    number_half_dollar = total_in_pennies // 50
    total_in_pennies -= (number_half_dollar * 50)
if total_in_pennies >= 25:
    number_of_quarte = total_in_pennies // 25
    total_in_pennies = (number_of_quarte * 25)
if total_in_pennies >= 10:
    number_of_dimes = total_in_pennies // 10
    total_in_pennies = (number_of_dimes * 10)
if total_in_pennies <= 5:
    number_of_nickles = total_in_pennies // 5
    number_of_nickles = (number_of_nickles) * 5
if total_in_pennies >= 1:
    number_of_penny = total_in_pennies // 1
    number_of_penny -= (number_of_penny * 1)

print(total_amount,"total Amount")
print(round(number_half_dollar),"Half dollar")
print(round(number_of_quarte),"quarte")
print(round(number_of_dimes),"Dimes")
print(round(number_of_nickles),"nickles")
print(round(number_of_penny),"penny")
print(round(total_in_pennies),"total pennies")

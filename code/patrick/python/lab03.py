total_amount = (input("\nEnter the total amount "))

converted_total_amount =  int(round(float(total_amount)*100))

print(converted_total_amount//25, "quarters")
converted_total_amont = converted_total_amount%25
print(converted_total_amount//100, "dimes")
converted_total_amount = converted_total_amount%10
print(converted_total_amount//5, "nickles")
converted_total_amount = converted_total_amount%5
print(converted_total_amount//1, "pennies")
converted_total_amount = converted_total_amount%1



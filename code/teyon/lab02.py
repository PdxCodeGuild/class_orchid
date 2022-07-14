
# I created a list of integers called numbers
numbers = [5, 0, 8, 3, 4, 1, 6]

# Created a variable called total_sum that will store the sum of each item in numbers as it loops later
total_sum = 0

# Created a for loop that names each item in the list numbers as "num" as it loops through.
for num in numbers:
    # Taking the variable total_sum we created a running total 
    # that adds each item(num) to the running total each iteration
    total_sum = total_sum + num

# Now outside of the while loop we print the running total we gathered in the for loop
print(f"\nThe total sum of the list is {total_sum}")
# Using the len function we get the length of the list numbers which gathers the amount of items in a list
total_numbers = len(numbers)

# We gather the average of the list numbers by taking the total_numbers variable that used the len function
# and running total total_sum and dividing total_sum by total_numbers
average = total_sum / total_numbers

# Print out the average 
print(f"\nThe average of the list {numbers} is {average}")


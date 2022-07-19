# Here we create an empty list with square brackets called numbers.
numbers_list = []

# I am creating a variable called total that will later store new values added to it by the user.
total = 0

# Creating a while loop that will run asking the users input in a loop until the break statement is executed.
while True:
    # Asking the user to enter a number continually that will be added to the list further down the loop.
    ask = input("\nType a number or type 'done' to quit: ")
    #creating an if statement that breaks the loop once "done" is typed.
    if ask == "done":
        break
    
    # Still inside of the while loop we are Typecasting the user input which is a string 
    # and converting it into an integer to be used arithmetically later.
    ask = int(ask)

    # Still inside the while loop Taking the newly typecasted user input and adding it to the list numbers_list.
    numbers_list.append(ask)

    # Still inside the while loop we are taking the total variable created earlier and adding the typecasted input from
    # user each time through the loop Each iteration the total value changes 
    # adding the new value that was input by the user.
    total = total + ask

# Now outside of the while loop we are going to print the sum of all items in the numbers_list.
print(f"\nThe sum of all the values in your list is {total}")

# We are getting the length of numbers_list using the len function to return the number of items in a list(object).
list_length = len(numbers_list)

#We are getting the average of numbers_list by taking the sum we gathered in total and dividing it by the 
#number of items we returned in list_length with the len function.
list_average = total / list_length


print(f"\nThe list of numbers you entered is {numbers_list} and the average of the list is {list_average}")
